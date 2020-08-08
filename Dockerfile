FROM python:alpine

RUN mkdir /root/app
COPY . /root/app/

RUN cd /root/app/ && pip install -r requirements.txt
RUN cd /root/app/ && python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

WORKDIR /root/app/
CMD ["python", "manage.py", "runserver"]
