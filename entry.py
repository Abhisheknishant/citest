import requests
from submodule import abc

print("Hello, world!")

r = requests.get("https://baidu.com")
print(r.content)

print(abc)