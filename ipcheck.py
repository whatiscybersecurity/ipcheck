#    (
#     \
#      )
# ##-------->           Simple Console-Based App to interact with abuseipdb's API 
#      )                https://github.com/whatiscybersecurity    
#     /
#    (

# This script uses the AbuseIPDB API to check if an IP address has been reported for abusive behavior.

import requests  # Used for making HTTP requests to the API

def check_ip(ip_address, api_key):
    # Function to check an IP address using the AbuseIPDB API
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    headers = {
        'Accept': 'application/json',
        'Key': api_key  # API key for authentication
    }
    
    params = {
        'ipAddress': ip_address,  # IP address to check
        'maxAgeInDays': '90'  # Consider reports from the last 90 days
    }
    
    try:
        # Make a GET request to the API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()['data']  # Extract the 'data' part of the JSON response
        
        # Print various pieces of information about the IP address
        print(f"\nResults for IP: {data.get('ipAddress', 'N/A')}")
        print(f"Abuse Confidence Score: {data.get('abuseConfidenceScore', 'N/A')}%")
        print(f"Total Reports: {data.get('totalReports', 'N/A')}")
        print(f"Last Reported: {data.get('lastReportedAt', 'Never')}")
        print(f"Country: {data.get('countryName', 'N/A')} ({data.get('countryCode', 'N/A')})")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Domain: {data.get('domain', 'N/A')}")
        print(f"Usage Type: {data.get('usageType', 'N/A')}")
        
        # Check if the IP is whitelisted
        if data.get('isWhitelisted', False):
            print("This IP is whitelisted.")
        
        # Print report categories if there are any reports
        if int(data.get('totalReports', 0)) > 0:
            print("\nReports Summary:")
            for category in data.get('reportCategories', []):
                print(f"- {category}")
        else:
            print("\nNo abuse reports found for this IP.")
        
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        print(f"An error occurred: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error details: {e.response.text}")
    except KeyError as e:
        # Handle any errors in parsing the JSON response
        print(f"Error parsing API response: {e}")

if __name__ == "__main__":
    # This block runs when the script is executed directly (not imported)
    api_key = input("Enter your AbuseIPDB API key: ")  # Prompt user for API key
    ip_to_check = input("Enter the IP address to check: ")  # Prompt user for IP address
    check_ip(ip_to_check, api_key)  # Call the check_ip function with user inputs

# Note: This script requires an API key from AbuseIPDB (https://www.abuseipdb.com/)
# The script provides a simple command-line interface to check IP addresses for potential abuse
# It displays information such as abuse confidence score, location, and report details if available
