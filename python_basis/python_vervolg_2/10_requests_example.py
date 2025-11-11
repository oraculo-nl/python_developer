# Voorbeeld externe module: requests (vereist 'pip install requests')
try:
    import requests
    resp = requests.get("https://api.github.com", timeout=5)
    print("Status:", resp.status_code)
    print("RateLimit:", resp.headers.get("X-RateLimit-Limit"))
except ImportError:
    print("Module 'requests' niet geïnstalleerd. Voer uit: pip install requests")
