import requests

r=requests.post('https://serene-wildwood-35121.herokuapp.com/oauth/changeUrl',{'clientId':'5bd4a7a54789560015311a2d','secret':'6268d306d1ff54e199bafa466b5d612eb132eb98456fe598846f66616b5a485fa13ed86b817b9f9534d1558ee7ce596574fa17c60eae07547bba3d7648214b9c','url':'http://127.0.0.1:2020/library/index/'})

print r