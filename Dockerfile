FROM public.ecr.aws/lambda/python:3.9
WORKDIR /usr/src/app

COPY app.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . .

CMD ["app.lambda_handler"]