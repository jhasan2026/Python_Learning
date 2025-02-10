import json
from urllib.request import urlopen

with urlopen("https://api.currencyapi.com/v3/latest?apikey=cur_live_4ehlx24pUA76E3voEUCuzDY7vR79zHCKpqpoaXks") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data,indent=2))
# #
# # print(len(data['data']))
#
for item in data['data']:
    print(item['code'])