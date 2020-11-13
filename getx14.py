import requests

r = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2', auth=('user', 'pass'))
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