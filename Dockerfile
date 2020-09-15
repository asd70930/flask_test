FROM python:3.6
WORKDIR RESTful_test2
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY RESTful_test2 .
ENV DATABASE_URL="10.5.0.3" \
    DATABASE_PORT="3306" \
    DATABASE_USER="root" \
    DATABASE_PASSWORD="123"
RUN flask db init && flask db migrate && flask db upgrade
WORKDIR /
#CMD ["gunicorn", "-w 4" ,"-b 0.0.0.0" ," RESTful_test2.wsgi:application"]
CMD gunicorn -w 4 -b 0.0.0.0 RESTful_test2.wsgi:application
EXPOSE 8000