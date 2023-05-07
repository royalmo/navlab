# NavLab Flask server

Work in progress!

## Easy start using Docker

Start the server on local port 5000:

```
docker run -p 5000:5000 -d royalmo/navlab
```

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

Again, from the same project directory. It will create 3 test users:

- Super User: super@user.com
- Aleix Llusà: aleix.llusa@upc.edu
- Deactivated User: foo@bar.com

All 3 users have the same password: `1234ABc$` .

```
python3 db_init.py
```

## Compile CSS

Run each time you change something tailwind-related:

```
npm run create-css
```

If you want it to automatically recompile all CSS every time a file changes, run `npm run create-css-forever` instead.

# Compile translations

Every time you translate something, you need to run these two commands:

```
$ pybabel extract -F app/babel.cfg -o app/translations/messages.pot --input-dirs=app
$ pybabel update --input-file=app/translations/messages.pot --output-dir=app/translations
```

And then, in each language file, fill the missing translations. Once
done, compile them and restart the server:

```
$ pybabel compile -f -d app/translations
```

## Run

Simple! Just go to the project folder and type:

```
python3 app.py
```

Run `python3 app.py --production` if you wish to accept TCP
connections from other IP addresses than localhost.
