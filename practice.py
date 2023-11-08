import requests

api_key = 'b92b48d2-60c5-4645-b9cf-6e7535b4ff12'
word = 'bintang'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)