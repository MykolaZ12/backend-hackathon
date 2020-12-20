FROM python:3.8

RUN git clone https://github.com/MykolaZ12/backend-hackathon /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

COPY ./local_config.py /app/config

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]