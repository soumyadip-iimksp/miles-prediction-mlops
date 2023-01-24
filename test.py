import requests


data = {
    "cylinders": 8,
    "displacement": 307,
    "horsepower": 130,
    "weight": 3504,
    "acceleration": 12,
    "model_year": 70,
    "origin": 1
}

host = "mileage-predictor-env.eba-ymtcygug.ap-south-1.elasticbeanstalk.com"
url = f"http://{host}/predict" #"http://localhost:9696/predict"

#print(requests.post(url, json=data).json())
result  = requests.post(url, json=data).json()

print(result)