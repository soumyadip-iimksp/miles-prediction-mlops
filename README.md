# miles-prediction-mlops

### 1. Data Processing

### 2. Build the model
```
Ridge Regression
```
### 3. Local Model Deployment
```
Deploy REST API using Flask
```
### 3. Create a virtual env for deploying using Docker - use **Pipenv**
```
pip install pipenv
pipenv install scikit-learn flask
```
To install the libraries used in theis project, simply use
```
pip install
```
To run the code from pipenv shell
```
pipenv run python app.py
```
### 4. Create a Dockerfile
```
FROM 3.9-slim # Set base image

ENV PYTHONUNBUFFERED=TRUE # python settings to see logs

RUN pip --no-cache-dir install pipenv # Install pipenv

WORKDIR /app #Set working path to /app

COPY ["Pipfile", "Pipfile.lock", "./"] # Copy pipenv files

RUN pipenv install --deploy --system && rm -rf /root/.cache # Install dependencies

COPY ["app.py", "ridge_auto_mse-3.293.bin", "dv.bin", "./"] # Copy the codes and models

EXPOSE 9696

ENTRYPOINT [ "gunicorn" , "--bind", "0.0.0.0:9696", "app:app"] # Specify the code to start the service
```
Build the docker 
```
docker build -t mileage-predictor .
```
Run the docker
```
docker run -it -p 9696:9696 mileage-predictor:latest
```
Install EBS CLI for AWS EBS using pipenv
```
pipenv install awsebcli --dev
```

Check EB version
```
pipenv shell
eb --version
```

Run initialization command
```
eb init -p docker mileage-predictor
```

Change the DEFAULT REGION on configure.yml

Test the abblication locally
```
eb local run --port 9696

python test.py
{'predicted_mpg': 15.256814714536844}
```
Deploy to AWS
```
eb create mileage-predictor-env
```
## Deploying Mileage Predictor using AWS EBS
![using-aws-ebs](https://user-images.githubusercontent.com/13174586/214431889-9c4933ce-2060-452a-b86c-06841a884100.png)