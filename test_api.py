#!/usr/bin/env python3
"""
Test script to debug RapidAPI integration issues
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_rapidapi_key():
    """Test if the RapidAPI key is valid"""
    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        print("❌ RAPIDAPI_KEY not found in environment")
        return False

    print(f"🔑 Testing API key: {api_key[:10]}...")

    # Test with a simple JSearch API call
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": "software developer",
        "page": "1",
        "num_pages": "1",
        "country": "US"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"📡 JSearch API Response Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ API key is valid")
            print(f"📊 Response contains {len(data.get('data', []))} jobs")
            return True
        elif response.status_code == 401:
            print("❌ API key is invalid or expired")
            return False
        elif response.status_code == 429:
            print("❌ Rate limit exceeded")
            return False
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error testing API: {e}")
        return False

def test_linkedin_api():
    """Test LinkedIn Jobs API"""
    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        return False

    url = "https://linkedin-jobs-search.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"🔗 LinkedIn API Response Status: {response.status_code}")

        if response.status_code == 200:
            print("✅ LinkedIn API accessible")
            return True
        else:
            print(f"❌ LinkedIn API failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error testing LinkedIn API: {e}")
        return False

def test_indeed_api():
    """Test Indeed API"""
    api_key = os.environ.get('RAPIDAPI_KEY')
    if not api_key:
        return False

    url = "https://indeed12.p.rapidapi.com/jobs/search"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "indeed12.p.rapidapi.com"
    }
    params = {
        "query": "software developer",
        "location": "United States"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"🏢 Indeed API Response Status: {response.status_code}")

        if response.status_code == 200:
            print("✅ Indeed API accessible")
            return True
        else:
            print(f"❌ Indeed API failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error testing Indeed API: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing RapidAPI Integration")
    print("=" * 50)

    # Test API key validity
    api_valid = test_rapidapi_key()
    print()

    if api_valid:
        # Test different APIs
        test_linkedin_api()
        print()
        test_indeed_api()
    else:
        print("❌ Cannot test other APIs due to invalid API key")