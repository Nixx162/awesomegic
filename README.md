# AwesomeGIC

A simple banking app that records deposit and withdrawal. Can be accessed online [here](https://awesomegic.up.railway.app/).

To deploy locally, **ensure that you have Python installed**, then do the following steps:

## Windows

1. Go to the project's root directory on your shell
2. Run `env\Scripts\Activate.ps1` if you're using PowerShell, or `env\Scripts\activate.bat` if you're using Command Prompt.
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`
6. Go to your browser and access the web app through http://127.0.0.1:8000/ or however you choose to configure.

## MacOS

1. Go to the project's root directory on your shell
2. Run `source env/Scripts/activate`
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`
6. Go to your browser and access the web app through http://127.0.0.1:8000/ or however you choose to configure.
