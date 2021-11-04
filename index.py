import json
import glob

def generate_indexes():
    coins = []
    
    for filename in glob.glob('./coins/*/*.json'):
        with open(filename) as fcoin:
            coin = json.loads(fcoin.read())

            if 'id' in coin:
                id = coin['id']
                name = coin['name']
                symbol = coin['symbol']
                url = coin.get('url', '')
                github_org = coin.get('github_org', None)
                
                coins.append((id, name, symbol, url, github_org))

    with open('./INDEX.md', 'w') as f:
        f.write(f'|Index|Symbol|Name|\n')
        f.write('|---|---|---|\n')

        for idx, c in enumerate(coins):
            id, name, symbol, _, _ = c
            f.write(f'|{idx+1}|[{symbol.upper()}](./coins/{id[0]}/{id}.json)|{name}|\n')


    orgs = {}
    for c in coins:
        id, name, symbol, _, github_org = c
        if github_org:
            github_org = github_org.lower()

            if github_org not in orgs:
                orgs[github_org] = dict(
                    id=id,
                    name=name,
                    symbol=symbol.upper()
                )

    with open('./coins/meta.json', 'w') as f:
        f.write(
            json.dumps(
                dict(
                    total_cryptos=len(coins),
                    orgs=orgs
                ),
                indent=4))

if __name__ == '__main__':
    generate_indexes()