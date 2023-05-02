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

- Sqlite3
```
sudo apt install sqlite3
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

## Compile translations

Run each time you change some literals. Server needs to be restarted.

```
./parse_translations.sh
```

## Run

Open two terminals to run the two processes:

```
python3 app.py
npm run create-css
```

## Misc

How to activate a user, or make it admin from the sqlite console.
Look that we first find the id of the user to activate and then update it.

```
$ sqlite3 app/navlab.db
sqlite> select id from user where email="isaac@isaaciglesias.net";
2
sqlite> update user set active=1 where id=2;
sqlite> update user set admin=1 where id=2;
```
