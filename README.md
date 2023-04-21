# NavLab Flask server

Work in progress!

## Prerequisites

- Python 3.6 or higher installed:

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3
```

- Node 14 or higher with npm 6.14 or higher:

```
sudo apt install nodejs npm
```

## Install dependencies

Change directory to project base path and run:

```
python3 -m pip install -r requirements.txt
npm install
```

## Set up database

Again, from the same project directory.

```
python3 db_init.py
```

## Run

Open two terminals to run the two processes:

```
python3 app.py
npm run create-css
```
