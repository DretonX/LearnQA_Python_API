#ex10
# def test_my_input():
#     phrase = input("Set a phrase: ")
#     assert len(phrase) < 15, f"Phrase '{phrase}' is too long"

#ex11
# import requests
#
# def test_homework_cookie():
#     response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
#     cookies_name = "HomeWork"
#     expected_cookie_value = "hw_value"
#
#     assert cookies_name in response.cookies, f"Cannot find cookie with name '{cookies_name}' in the last response"
#     assert response.cookies[cookies_name] == expected_cookie_value, f"Cookie value is not '{expected_cookie_value}'"
#
#     print(f"The value of the '{cookies_name}' cookie is '{response.cookies[cookies_name]}")

#ex12

# import requests
# def test_headers():
#     url = 'https://playground.learnqa.ru/api/homework_header'
#     response = requests.get(url)
#     headers = response.headers
#     header_name = "x-secret-homework-header"
#     header_value = headers.get(header_name)
#     print(f'Header name is "{header_name}", header value is "{header_value}"')
#     assert header_name in headers, f"Cannot find header with name '{header_name}' in the last response"
#     assert headers[header_name] == header_value, f"Header value is not '{header_value}'"

#ex13



#ex14
