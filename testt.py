import requests

payload = {'login':'secret_login','password':'secret_pass'}
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)

res = response.cookies.get('auth_cookie')
print(res)
print(dict(response.cookies))