import requests
from bs4 import BeautifulSoup


def scrape_jobs(role="data scientist"):
    url = f"https://www.indeed.com/jobs?q={role.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception("Blocked or failed request")

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = []

        for div in soup.find_all("a", attrs={"data-jk": True})[:5]:
            title = div.get_text(strip=True)

            jobs.append({
                "role": title,
                "company": "Unknown"
            })

        if not jobs:
            raise Exception("No jobs found")

        return jobs

    except Exception as e:
        print("⚠️ Scraping failed, using fallback data")

        # fallback dataset
        return [
            {"company": "Google", "role": "Data Scientist"},
            {"company": "Amazon", "role": "ML Engineer"},
            {"company": "Microsoft", "role": "Data Analyst"},
        ]