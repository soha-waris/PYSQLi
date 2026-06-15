import requests
import random
from config import USER_AGENTS, TIMEOUT, MAX_RETRIES
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def send_request(url, method="GET", data=None, proxy=None, cookies=None):
    """Robust HTTP request with retries and rotation"""
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    proxies = {"http": proxy, "https": proxy} if proxy else None
    
    for attempt in range(MAX_RETRIES):
        try:
            if method.upper() == "POST":
                response = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=TIMEOUT, cookies=cookies)
            else:
                response = requests.get(url, headers=headers, proxies=proxies, timeout=TIMEOUT, cookies=cookies)
            
            return response
        except requests.exceptions.RequestException:
            if attempt == MAX_RETRIES - 1:
                return None
    return None

def parse_url_parameters(url):
    """Extract parameters from URL for testing"""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return {k: v[0] for k, v in params.items()} if params else {}
