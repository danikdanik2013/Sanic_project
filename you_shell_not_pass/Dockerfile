FROM nginx:alpine
FROM mongo:4.0.5-xenial
RUN mongod --fork --syslog
ENV MONGO_URL mongodb://localhost:27017/
EXPOSE 27017
FROM python:3.6-stretch

WORKDIR /you_shell_not_pass
COPY . /you_shell_not_pass

EXPOSE 80
ENV http_proxy host:port

WORKDIR /you_shell_not_pass/
RUN pip install --trusted-host pypi.python.org -r requirements/requirements.txt

CMD ["python", "manage.py"]

#docker build -t app .
#docker run -p 4000:80 app