import requests


data = {"url":
            {
            "cylinders": 8,
            "displacement": 307,
            "horsepower": 130,
            "weight": 3504,
            "acceleration": 12,
            "model_year": 70,
            "origin": 1
            }
}


url = "http://localhost:8080/2015-03-31/functions/function/invocations" 

#print(requests.post(url, json=data).json())
result  = requests.post(url, json=data).json()

print(result)