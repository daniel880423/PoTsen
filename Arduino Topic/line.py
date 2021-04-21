import sys
import requests

msg = str(sys.argv[1])

headers = {
    "Authorization": "Bearer " + "9gPzZGb6M9WHhrTvO8sKMI438rqPtLH8fc8eJkYDIwZ",
    "Content-Type": "application/x-www-form-urlencoded"
}
 
params = {"message": msg}

r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
                      
print(r.status_code)  #200