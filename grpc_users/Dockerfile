FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /grpc_users
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /grpc_users
EXPOSE 50051