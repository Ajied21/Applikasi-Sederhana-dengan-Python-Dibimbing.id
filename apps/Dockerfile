FROM python:3.10

WORKDIR /app

COPY App.py App.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "App.py"]
