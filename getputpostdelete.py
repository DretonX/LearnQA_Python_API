import requests

response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type')

print(f'without method  - {response.text}')

response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')

print(f'with request HEAD - {response.text}')

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

list_req = ['POST', 'GET', 'DELETE', 'PUT']
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

methods = {'POST': requests.post, 'GET': requests.get, 'DELETE': requests.delete, 'PUT': requests.put}

for method in list_req:
    if method == 'GET':
        payload = {'method': method}
        response = methods[method](url, params=payload)  # передаем параметры через params для GET-запроса
    else:
        payload = {'method': method}
        response = methods[method](url, data=payload)  # передаем параметры через data для остальных запросов
    print(f'{response.text} - {method}')
