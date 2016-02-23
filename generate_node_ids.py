#!/usr/bin/env python

import dockercloud
import sys

num_tokens = 1
if len(sys.argv) == 2:
    num_tokens = int(sys.argv[1])

def get_token():
    token = ""
    try:
        json = dockercloud.api.http.send_request("POST", "api/infra/v1/token")
        if json:
            token = json.get("token", "")
    except Exception as e:
        print >>sys.stderr, e
        sys.exit(EXCEPTION_EXIT_CODE)

    return token

print '---'
print 'nodes:'
for num in range(0,num_tokens):
    print '  -', get_token()
