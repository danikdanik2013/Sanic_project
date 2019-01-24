FROM python:3.6-stretch

WORKDIR /you_shell_not_pass
COPY . /you_shell_not_pass

EXPOSE 80

WORKDIR /you_shell_not_pass/
RUN pip install --trusted-host pypi.python.org -r requirements/requirements.txt

CMD ["python", "manage.py"]

#docker build -t app .
#docker run -p 4000:80 app