FROM public.ecr.aws/lambda/python:3.8

RUN pip install update -U pip
RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY lambda_function.py lambda_function.py

COPY dv.bin dv.bin
COPY ridge_auto_mse-3.293.bin ridge_auto_mse-3.293.bin

CMD ["lambda_function.lambda_handler"]