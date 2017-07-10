## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests

import requests
import json
import sys

api_key = "YOUR_API_KEY"
domain = "YOUR_DOMAIN"
password = "x"

# Id of the ticket to be updated
ticket_id = str(sys.argv[1])

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password))

if r.status_code == 200:
  #print "Request processed successfully, the response is given below" + r.content
  parsed = json.loads(r.content)
  print("---------")
  print "ID: " + str(parsed["id"])
  print "Subject: " + parsed["subject"]
  print "Description: " + parsed["description_text"]
  print "Emails: " + str(parsed["cc_emails"])
  print("---------")
  
else:
  print "Failed to read ticket, errors are displayed below,"
  response = json.loads(r.content)
  print response["errors"]

  print "x-request-id : " + r.headers['x-request-id']
  print "Status Code : " + r.status_code
