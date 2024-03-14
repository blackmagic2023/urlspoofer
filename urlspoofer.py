import requests

def mask_url(long_url):
    endpoint = "https://is.gd/create.php"
    payload = {
        "format": "json",
        "url": long_url
    }
    
    response = requests.get(endpoint, params=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get('shorturl')
    else:
        return None

if __name__ == "__main__":
    long_url = input("Enter the URL to mask: ")
    
    masked_url = mask_url(long_url)
    if masked_url:
        print("Masked URL:", masked_url)
    else:
        print("Failed to mask URL. Please check your input and try again.")
