FROM python:3.7.2-stretch
WORKDIR /myapp
COPY . /myapp
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini", "uwsgi.ini"]
