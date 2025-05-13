FROM python:3.10.17-alpine3.21

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r req.txt

EXPOSE 5002

CMD ["flask", "run", "-h", "0.0.0.0"]
