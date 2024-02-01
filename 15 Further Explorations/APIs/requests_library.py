import requests
import json
import sys

# Get the URL from the command line
url = sys.argv[1]

# Make the request and check for errors
response = requests.get(url)
if response.status_code != 200:
    print("Error:", response.status_code)
    sys.exit(0)

# Display the response text
print(json.dumps(response.json()) + "\n")
