# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt update -y

# Installing python
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3 python3-pip -y

# Installing nodejs
RUN apt install nodejs npm -y

# Installing sqlite3
RUN apt install sqlite3 -y

# Changing directory
WORKDIR /navlab

# NPM requirements
COPY package-lock.json .
COPY package.json .
RUN npm install

# Python requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Copying all
COPY . .

# Setting up database
RUN python3 db_init.py

# Compiling CSS
RUN npm run create-css

# Compiling translations
RUN pybabel compile -f -d app/translations

# Run
EXPOSE 5000
CMD python3 app.py --production
