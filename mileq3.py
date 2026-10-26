import pandas as pd 
def load_ticekt_sales(file_path):
    df=pd.read_csv(file_path)
    return df[["sale_id", "event_id","buyer_name","buyer_email","tickets","ticket_price", "discount_pct"]]
def clean_ticket_sales(df):
    dup=df.copy()
    dup=dup.dropna(subset=["buyer_email"])
    dup=dup.drop_duplicates(subset=["sale_id"],keep="first")
    return dup
def merge_with_events(df,ref_file):
    df1=pd.read_csv(ref_file)
    return pd.merge(df,df1,on="event_id",how="inner")
def add_net_ticket_value(df):
    dup=df.copy()
    dup["net_ticket_value"]=(dup["tickets"]*dup["ticket_price"]*(1-(dup["discount_pct"])/100)).round(2)
    return dup
def aggregate_by_category(df):
    dup=df.copy()
    return dup.groupby("category")["net_ticket_value"].agg(["mean","sum","count"]).rename(columns={"mean":"avg_net_ticket_value","sum":"total_net_ticket_revenue","count":"valid_sale_count"}).reset_index()
def finalize_summary(df):
    dup=df.copy()
    dup=dup[["category","avg_net_ticket_value","total_net_ticket_revenue","valid_sale_count"]].copy()
    dup['avg_net_ticket_value']=(dup['avg_net_ticket_value']).round(2)
    dup["total_net_ticket_revenue"]=(dup["total_net_ticket_revenue"]).round(2)
    return dup.sort_values("category").reset_index(drop=True)
if __name__ == "__main__":
    df=load_ticekt_sales("sales.csv")
    print(df)
    df=clean_ticket_sales(df)
    print(df)
    df=merge_with_events(df,"events.csv")
    print(df)
    df=add_net_ticket_value(df)
    print(df)
    df=aggregate_by_category(df)
    print(df)
    df=finalize_summary(df)
    print(df)
    


