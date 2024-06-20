from pprint import pprint

import requests

"""
get -> data olamiz
post -> data yuboramiz
"""
data = requests.get("http://146.190.164.45/api/v1/tracker/actvities/")

pprint(data.json())
