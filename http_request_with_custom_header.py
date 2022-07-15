# Description: 
# Python script to make HTTP request with custom header by using the standard urllib library

# Usage:
# python3 [script]

from urllib.request import Request, urlopen

req = Request("https://postman-echo.com/get")
req.add_header("Content-Type", "application/json")
req.add_header("Custom-Header", "Maxat")

content = urlopen(req).read()
status = urlopen(req).status

print("Request content: \n",  content)
print("Request status: \n",  status)