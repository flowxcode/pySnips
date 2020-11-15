# this is a get sandbox for the requests module, simple test for fiddler wireshark and http proxy intercepter tools.

import requests

# url = 'http://www.google.com'

# proxy = '127.0.0.1:8866'
# proxy2 = '127.0.0.1:8866'
# #requests.get(url, proxies={"http":proxy1,"http":proxy2})
# requests.get(url, proxies={"http":proxy})

#------------------------

r = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
r.status_code
#200
r.headers['content-type']
#application/json; charset=utf8'
r.encoding
#'utf-8'
r.text
#'{"type":"User"...'
r.json()
#{'private_gists': 419, 'total_private_repos': 77, ...}

print(r.json())
