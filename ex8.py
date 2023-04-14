import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1) создаем задачу
response = requests.get(url)
result = response.json()
token = result["token"]
seconds = result["seconds"]
print(f"Task is created, token is {token}, it will take {seconds} seconds to complete")

# 2) делаем запрос с token до того, как задача готова
payload = {"token": token}
response = requests.get(url, params=payload)
result = response.json()
status = result["status"]

print(f"Status for token {token} before task is completed is {status}")

# 3) ждем нужное количество секунд
print(f"Waiting {seconds} seconds for task to be completed")
time.sleep(seconds)

# 4) делаем запрос с token после того, как задача готова
payload = {"token": token}
response = requests.get(url, params=payload)
result = response.json()
status = result["status"]
if status == "Job is ready":
    print(f"Task for token {token} is completed")
    if "result" in result:
        print(f"Task result: {result['result']}")
    else:
        print("Task result is not ready yet")
else:
    print(f"Error getting result for token {token}: {result['error']}")
