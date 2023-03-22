FROM python:3.7-alpine
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=start.py
CMD ["flask", "run", "--host", "0.0.0.0"]