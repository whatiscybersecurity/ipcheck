#    (
#     \
#      )
# ##-------->           Simple "GUI" to interact with abuseipdb's API 
#      )                https://github.com/whatiscybersecurity    
#     /
#    (


import requests

def check_ip(ip_address, api_key):
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        
        print(f"\nResults for IP: {data.get('ipAddress', 'N/A')}")
        print(f"Abuse Confidence Score: {data.get('abuseConfidenceScore', 'N/A')}%")
        print(f"Total Reports: {data.get('totalReports', 'N/A')}")
        print(f"Last Reported: {data.get('lastReportedAt', 'Never')}")
        print(f"Country: {data.get('countryName', 'N/A')} ({data.get('countryCode', 'N/A')})")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Domain: {data.get('domain', 'N/A')}")
        print(f"Usage Type: {data.get('usageType', 'N/A')}")
        
        if data.get('isWhitelisted', False):
            print("This IP is whitelisted.")
        
        if int(data.get('totalReports', 0)) > 0:
            print("\nReports Summary:")
            for category in data.get('reportCategories', []):
                print(f"- {category}")
        else:
            print("\nNo abuse reports found for this IP.")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error details: {e.response.text}")
    except KeyError as e:
        print(f"Error parsing API response: {e}")

if __name__ == "__main__":
    api_key = input("Enter your AbuseIPDB API key: ")
    ip_to_check = input("Enter the IP address to check: ")
    check_ip(ip_to_check, api_key)
