FROM python:3.9.16-slim 
# Set base image

ENV PYTHONUNBUFFERED=TRUE 
# python settings to see logs

RUN pip --no-cache-dir install pipenv 
# Install pipenv

WORKDIR /app 
#Set working path to /app

COPY ["Pipfile", "Pipfile.lock", "./"] 
# Copy pipenv files

RUN pipenv install --deploy --system && rm -rf /root/.cache 
# Install dependencies

COPY ["app.py", "ridge_auto_mse-3.293.bin", "dv.bin", "./"] 
# Copy the codes and models

EXPOSE 9696

ENTRYPOINT [ "gunicorn" , "--bind", "0.0.0.0:9696", "app:app"] 
# Specify the code to start the service