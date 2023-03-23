FROM python:3.8-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=start.py
CMD ["python", "${FLASK_APP}"]