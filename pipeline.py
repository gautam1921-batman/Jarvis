import pandas as pd
import os

def process_market_data():
    print("⚙️ Processing data pipeline...")
    if not os.path.exists("raw_jobs.csv"):
        print("❌ Error: 'raw_jobs.csv' not found.")
        return False

    df = pd.read_csv("raw_jobs.csv")
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["title", "company"], inplace=True)
    df['city'] = df['location'].apply(lambda x: str(x).split(',')[0].strip())

    output_file = "cleaned_jobs.csv"
    df.to_csv(output_file, index=False)
    print(f"📊 Pipeline completed! Saved cleaned records to '{output_file}'.")
    return True

if __name__ == "__main__":
    process_market_data()
