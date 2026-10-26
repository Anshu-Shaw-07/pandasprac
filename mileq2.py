import pandas as pd
def load_service_requests(file_path):
    df=pd.read_csv(file_path)

    return df[["request_id", "service_id", "customer_name","email", "phone","quoted_fee", "discount_pct"]]
def clean_service_requests(df):
   df=df.dropna(subset="email")
   return df.drop_duplicates(subset="request_id",keep="first")
def merge_with_services(requests_df, ref_file_path):
    cat=pd.read_csv(ref_file_path)
    return pd.merge(requests_df,cat, on="service_id",how="inner")
def add_net_quoted_fee(df):
   df=df.copy()
   df["net_quoted_fee"]=(df["quoted_fee"] *(1 - df["discount_pct"] / 100)).round(2)
   return df
def aggregate_by_service(df):
 return df.groupby("service_name")["net_quoted_fee"].agg(["mean","count"]).rename(columns={"mean":"avg_net_quoted_fee","count":"request_count"}).reset_index()
def finalize_summary(df):
   df=df[["service_name","avg_net_quoted_fee", "request_count"]].copy()
   df["avg_net_quoted_fee"]=df["avg_net_quoted_fee"].round(2)
   return df.sort_values("service_name").reset_index(drop=True)
   
    
if __name__ == '__main__':
 df=load_service_requests("service_requests.csv")
 #print(df)
 df=clean_service_requests(df)
 #print(df)
 df=merge_with_services(df,"service_catalogue.csv")
 #print(df)
 df=add_net_quoted_fee(df)
 #print(df)
 df=aggregate_by_service(df)
 #print(df)
 df=finalize_summary(df)
 print(df)