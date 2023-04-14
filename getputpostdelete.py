import requests

payload = {'method': 'GET'}
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)

print(response.text)

payload = {'method': 'PUT'}
response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data=payload)

print(response.text)

payload = {'method': 'POST'}
response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=payload)

print(response.text)

payload = {'method': 'DELETE'}
response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data=payload)

print(response.text)
