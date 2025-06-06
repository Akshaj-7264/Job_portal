import os
import requests

def get_adzuna_jobs(query="software developer", results_per_page=20):
    ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')
    ADZUNA_APP_KEY = os.getenv('ADZUNA_APP_KEY')

    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        print("❌ Missing Adzuna credentials in environment variables.")
        return []

    base_url = 'https://api.adzuna.com/v1/api/jobs/in/search/1'
    params = {
        'app_id': ADZUNA_APP_ID,
        'app_key': ADZUNA_APP_KEY,
        'results_per_page': results_per_page,
        'what': query,
        'content-type': 'application/json'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise error if status is not 200
        data = response.json()
        return data.get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"🌐 Adzuna API request failed: {e}")
        return []
