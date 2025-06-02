import requests

def is_url_reachable(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def format_string(s):
    return s.strip().title()

def calculate_percentage(part, total):
    if total == 0:
        return 0
    return (part / total) * 100

