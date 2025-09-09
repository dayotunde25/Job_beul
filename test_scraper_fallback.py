#!/usr/bin/env python3
"""
Test script to verify the scraper fallback mechanism
"""

import os
import sys
from dotenv import load_dotenv

# Add the app directory to the path
sys.path.append('.')

load_dotenv()

def test_scraper_fallback():
    """Test the scraper with fallback mechanism"""
    from app.utils import scrape_jobs_from_api

    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        print("❌ RAPIDAPI_KEY not found")
        return

    print("🔍 Testing scraper fallback mechanism")
    print("=" * 50)

    # Test with JSearch (should fail and fallback)
    print("Testing JSearch with fallback...")
    result = scrape_jobs_from_api(
        api_key=api_key,
        host='jsearch.p.rapidapi.com',
        source='jsearch',
        query='software developer',
        location='New York',
        country='us'
    )

    if result:
        if 'data' in result:
            jobs = result['data']
            print(f"✅ Success! Retrieved {len(jobs)} jobs")
            if jobs:
                print(f"Sample job: {jobs[0].get('job_title', 'N/A')} at {jobs[0].get('employer_name', 'N/A')}")
                print(f"Source: {jobs[0].get('source', 'N/A')}")
        else:
            print(f"✅ Success! Retrieved data: {type(result)}")
    else:
        print("❌ Failed to retrieve any data")

if __name__ == "__main__":
    test_scraper_fallback()