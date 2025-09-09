# Import libraries
import requests
from urllib.parse import urlencode

# Set parameters
parameters = { 'publisher' : 3805, 'user_ip' : '68.183.210.8', 'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36', 'keyword' : '', 'location' : '', 'limit' : '50', 'page' : '3' }

# Set URL
url = 'https://api.whatjobs.com/api/v1/jobs.json?%s' % urlencode(parameters)

# Exec and return the result
response = requests.get(url)

# Dump the result
print (response.content)
