#! /usr/bin/python
import urllib3
import re

next_re = re.compile(r'<(.*)>; rel="next"')

gh_api_pool = urllib3.connection_from_url('https://api.github.com', maxsize=50, block=True)


#print gh_api_pool

resp = gh_api_pool.request('get', '/orgs/cfpb/repos', headers = {'User-Agent': 'cfpb-tiresias'})

print resp.headers

print ('\n')
links = resp.getheader('Link')

print ('\n')
my_list = links.split(",")

for item in my_list:
    if 'rel="next"' in item:
        next_match = next_re.match(item)
        print next_match.groups()[0]





#for item in my_dict:
#    print item