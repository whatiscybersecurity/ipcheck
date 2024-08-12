# ipcheck

A simple Python tool to check IP addresses using the AbuseIPDB API. You can do domains and more, but as of 8/11/24, this is the start of a bigger project I have in mind. I will update this tool with more features as soon as timely possible.

## Description

ipcheck allows you to quickly retrieve information about an IP address, including potential abuse reports. It uses the AbuseIPDB API to fetch:

- Abuse confidence score
- Number of reports
- Country of origin
- ISP
- Usage type

## Requirements

- Python 3.6+
- requests library

## Installation

Choose one of the following methods:

### Option 1: Local Installation

1. Copy the entire code from `ip_check_tool.py`.
2. Paste it into a new file on your local machine.
3. Save the file as `ipcheck.py` (or any name you prefer).

### Option 2: Clone the Repository

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ipcheck.git
   ```

After installation, install the required library:
```
pip install requests
```

## Usage

1. Get a (FREE) API key from [AbuseIPDB](https://www.abuseipdb.com/).
2. Run the script:
   ```
   python ipcheck.py
   ```
   (Use the filename you chose if different)
3. Enter your API key when prompted. I prefer inputting the key manually every time in my current workflow. Adjust as needed.
5. Enter the IP address to check.

## Example Output

```
Results for IP: 192.0.2.1
Abuse Confidence Score: 0%
Total Reports: 0
Last Reported: Never
Country: United States (US)
ISP: Example ISP
Domain: example.com
Usage Type: Data Center/Web Hosting/Transit

No abuse reports found for this IP.
```

## License

This project is open source and available under the [MIT License](LICENSE).
