import requests


data = {"url":
            {
            "cylinders": 10,
            "displacement": 247,
            "horsepower": 160,
            "weight": 3904,
            "acceleration": 18,
            "model_year": 75,
            "origin": 1
            }
}

invoke_URL = "https://fakexyz.execute-api.ap-south-1.amazonaws.com/prod"
url = f"{invoke_URL}/predict" 

#print(requests.post(url, json=data).json())
result  = requests.post(url, json=data).json()

print(result)