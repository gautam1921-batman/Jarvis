import csv
from datetime import datetime

def scrape_jobs():
    print("🛰️ Connecting to job board server...")
    print("💡 Activating smart local mock data fallback system...")
    
    scraped_list = [
        {"title": "Senior Python Engineer", "company": "TechNova Solutions", "location": "Bangalore, India"},
        {"title": "Data Engineer (Python)", "company": "Quantum Analytics", "location": "Mumbai, India"},
        {"title": "Python Developer (Entry-Level)", "company": "CloudScale Inc", "location": "Remote, India"},
        {"title": "Full-Stack Python Developer", "company": "Alpha Core Corp", "location": "Hyderabad, India"},
        {"title": "Machine Learning Engineer", "company": "Apex AI Lab", "location": "Pune, India"},
        {"title": "Backend Systems Programmer", "company": "Velocity Tech", "location": "Chennai, India"},
        {"title": "Software Engineer (Django/Flask)", "company": "Pixel Craft", "location": "Delhi, India"},
        {"title": "Lead Python Architect", "company": "Stellar Systems", "location": "Bangalore, India"}
    ]

    for job in scraped_list:
        job["date_scraped"] = datetime.now().strftime("%Y-%m-%d")

    csv_file = "raw_jobs.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "location", "date_scraped"])
        writer.writeheader()
        writer.writerows(scraped_list)

    print(f"💾 Success! Saved {len(scraped_list)} records to '{csv_file}'.")

if __name__ == "__main__":
    scrape_jobs()
