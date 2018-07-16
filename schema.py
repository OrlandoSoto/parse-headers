#! /usr/bin/python
import json

from server import schemas

def create_index(db_name):
    schema = getattr(schemas, db_name, {})
    print db_name
    url = '/%s' % db_name
    body = json.dumps(schema)
    print body
    print "\n"


if __name__ == "__main__":
    create_index('history')
    create_index('search')
    create_index('autocomplete')
