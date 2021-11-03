import json
import glob

yes,no = 0,0
countries = {}
for filename in glob.glob('./coins/*/*.json'):
    with open(filename) as fcoin:
        coin = json.loads(fcoin.read())
        if coin.get('country_origin'):
            yes += 1
            c = coin.get('country_origin')
            countries[c] = countries.get(c, [])
            countries[c].append(coin.get('name'))
        else:
            no += 1

        print(yes, no)

print(countries['VN'])

# import json
# import glob

# cats = set([])
# for filename in glob.glob('./coins/*/*.json'):
#     with open(filename) as fcoin:
#         coin = json.loads(fcoin.read())
#         if coin.get('categories'):
#             cats |= set(coin.get('categories'))

# print(cats)
