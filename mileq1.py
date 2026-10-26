
import pandas as pd


def load_student_enquiries(file_path):
    df = pd.read_csv(file_path)
    return df[[
        "enquiry_id", "course_id", "student_name",
        "email", "phone", "quoted_fee", "discount_pct"
    ]]


def clean_enquiry_data(df):
    df = df.dropna(subset=["email"])
    return df.drop_duplicates(subset=["enquiry_id"], keep="first")


def merge_with_courses(enquiries_df, ref_file_path):
    courses = pd.read_csv(ref_file_path)
    return pd.merge(enquiries_df, courses, on="course_id", how="inner")


def add_net_quoted_fee(df):
    df = df.copy()
    df["net_quoted_fee"] = (
        df["quoted_fee"] * (1 - df["discount_pct"] / 100)
    ).round(2)
    return df


def aggregate_by_course(df):

    return df.groupby("course_name")["net_quoted_fee"].agg(
    ["mean", "count"]
).rename(columns={
    "mean": "avg_net_quoted_fee",
    "count": "enquiry_count"
}).reset_index()


def finalize_summary(df):
    df = df[[
        "course_name", "avg_net_quoted_fee", "enquiry_count"
    ]].copy()
    df["avg_net_quoted_fee"] = df["avg_net_quoted_fee"].round(2)
    return df.sort_values("course_name").reset_index(drop=True)


if __name__ == "__main__":
    df = load_student_enquiries("training_enquiries.csv")
    print(df)
    df = clean_enquiry_data(df)
    
    
    
    print(df)
    df = merge_with_courses(df,"training_courses.csv")
    print(df)
    df = add_net_quoted_fee(df)
    print(df)
    df = aggregate_by_course(df)
    print(df)
    df = finalize_summary(df)

    print(df)

