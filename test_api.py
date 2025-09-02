import requests

# Base URL for your FastAPI app
BASE_URL = "http://127.0.0.1:8000"  # works inside Codespaces

def test_root():
    """Test the root endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/", timeout=5)  # prevent hanging
        print("\n[ROOT ENDPOINT TEST]")
        print("Status Code:", r.status_code)
        print("Response:", r.json())
    except Exception as e:
        print("Error testing root:", e)

def test_docs():
    """Test the docs endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/docs", timeout=5)
        print("\n[DOCS ENDPOINT TEST]")
        print("Status Code:", r.status_code)
        print("Response (truncated):", r.text[:200], "...")
    except Exception as e:
        print("Error testing docs:", e)

def test_redoc():
    """Test the redoc endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/redoc", timeout=5)
        print("\n[REDOC ENDPOINT TEST]")
        print("Status Code:", r.status_code)
        print("Response (truncated):", r.text[:200], "...")
    except Exception as e:
        print("Error testing redoc:", e)

if __name__ == "__main__":
    test_root()
    test_docs()
    test_redoc()
