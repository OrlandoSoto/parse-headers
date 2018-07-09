#! /usr/bin/python
import urllib3

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
        item_to_split = str(item)
        print item_to_split
        print item.rstrip()







#for item in my_dict:
#    print item