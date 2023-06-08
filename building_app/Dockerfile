FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /buiding_app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /buiding_app
EXPOSE 7000