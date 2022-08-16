FROM python:3.9.7-slim

WORKDIR /programs_py

COPY . .
RUN pip install --upgrade pip; \
    pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["main.py"]
