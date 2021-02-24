# Installation

This project is was built using Python 3.8.5 on Windows 10 update 2004, so this project might run without issues on OS/X or Linux based operating systems. The main purpose of this project is to learn Flask and a bit of it's fundaments.

## Environment

First, let's create a virtual environment for this application. This ensures that your application runs inside a standalone "container" with no need to install it's dependencies globally inside your OS.

```
python -m venv flaskenv
```

After createing virtual env, do not forget to upgrade pip and get latest version:
```
python -m pip install --upgrade pip
```

Now install pipenv to install project's dependencies instead regular pip. This installer generates Pipfile and Pipfile.lock.

```
python -m pip install pipenv
```

Now install dependencies with pipenv installer:
```
python -m pipenv install -r requirements.txt
```

If you don't want to generate these files, just install with pip:
```
python -m pip install -r requirements.txt
```

## Running application

To run this app, just execute one of both files: `serve.bat` or `serve.sh`. They'll provide some environment configuration before start application.