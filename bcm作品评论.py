import requests
from concurrent.futures import ThreadPoolExecutor
id = input("作品id: ")
url="https://api.codemao.cn/creation-tools/v1/works/"+id
cishu=input("数量：")
cishu=int(cishu)
def execute_action(i):
    a = requests.get(url)
    print(i, a.json())
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(execute_action, range(cishu))
