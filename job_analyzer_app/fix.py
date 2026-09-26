import urllib.request
import os

# URLs to your exact files on GitHub
files = {
    "job_market_analyzer.py": "https://githubusercontent.com",
    "pipeline.py": "https://githubusercontent.com",
    "app.py": "https://githubusercontent.com"
}

print("📥 Starting automatic recovery...")
for filename, url in files.items():
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"✅ Saved {filename} successfully!")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")

print("\n🚀 All files recovered! Running pipeline now...")
os.system("python job_market_analyzer.py")
os.system("python pipeline.py")
print("\n🖥️ Starting Dashboard Server...")
os.system("python -m streamlit run app.py")
