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

### Deploying Mileage Predictor using AWS EBS
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

![using-aws-ebs](https://user-images.githubusercontent.com/13174586/214431889-9c4933ce-2060-452a-b86c-06841a884100.png)

### Deploying Mileage Predictor using AWS Lambda
Create `lambda_function` and for inference, create a function within it with name `lambda_handler`. 

Create `Dockerfile`
Build the image using 
```docker build -t mileage-predictor-lambda:v001 .
```
Run the docker using 
```
docker run --rm -p 8080:8080 mileage-predictor-lambda:v001
```
Run the `test.py` to check if response is fetched back 

publish the image to AWS ECR
```
aws ecr create-repository --repository-name mileage-predictor-lambda-repo

aws ecr get-login-password --region ap-south-01 | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```
Check in AWS ECR webconsole if the repo is created

Create the Lambda Function:
-   Go to Lambda Page and create a new function
-   Click on `Container Image`
-   Enter `Function Name` and create fiunction
-   Go to `Configuration`
-   Increase *memory* to `1024 MB` and *Timout* to `30 sec`
-   Save the settings
-   Go to *Test* tab and try out if the function is working or not
Create API gateway
-   Go to *API Gateway*
-   Select `REST API` and click on **Build**
-   Select **REST**
-   Select **New API**
-   Api Name: `mileage-predictor-api`
-   Description: `expose lambda functio as web service`
-   Endpoint Type: `Regional`
-   Click on **Create API**
-   Next click on **Actions** and select **resources**
-   From **Actions** dropdown select `Create a Resource`
-   Resource Name: `predict-endpoint`
-   Resource Path: `predict`
-   Select the `predict` resource and click **Actions**, and from dropdown select `POST` method, and click on the **Tick** button
-   Integration Type: `Lambda Function`
-   Use Lambda Proxy Integration: `Unchecked`
-   Lambda Function: `mileage-predictor`
-   Click on `Test` and enter the *input* in **Response Body** to test
-   If working fine, select `Deploy API` from **Actions**
-   Deployment Stage:: `[New Stage]`
-   Stage Name: `prod`
-   Stage Description: `Production API`
-   Get a link `Invoke URL`

Test using `test_lambda.py`