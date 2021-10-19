import time
import requests
from time import sleep as ss

num = input("Enter Number >>> ")
num2 = input("Enter Number >>> +98")

# # {"phoneNumber":num}

# url = "https://snappfood.ir/customer/app-dl/send"
# cellphone=num
co = 0
while True:

    send = requests.post("https://snappfood.ir/auth/login_with_no_pass",data={"cellphone":num,"captcha":"111"})
    co = co + 1
    print(f"[{co}] {send}")
    ss(5)
    if co == 6:
        break


url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata={"cellphone":"+98"+num2}
count = 0
while True:
    
    send = requests.post(url,data=mydata)
    if send.status_code == 200:
        print(send)
    count = count + 1
    ss(5)
    if count == 4:
        break

print("end")
