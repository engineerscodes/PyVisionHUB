import requests

url = "https://vtop2.vitap.ac.in/vtop/"
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
               "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
           }

r = requests.get(url,headers=headers)

redirected_url = r.url

print(f"Redirected URL {redirected_url}")

r=requests.get(redirected_url,headers=headers)
print(f"Response Cookies {r.cookies}")
print(r.text)