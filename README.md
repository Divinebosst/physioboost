First of all make sure that the Local Server is running (Xampp, Mampp e.t.c)

# To set up the environment, first install all requirements in the requirements.txt file (Make sure you open your command line in the directory which contains the requirements.txt file). Do this by running the following command:

pip install -r requirements.txt --no-index --find-links file:///tmp/packages

Then reset all your migrations by running the following one after the otherr:

python manage.py makemigrations
python manage.py migrate --fake-initial

Create an adminstrator account by running the following and following the instructions:

python manage.py createsuperuser

Then run your server

python manage.py runserver

Login at 127.0.0.01:8000/admin

And then add Country, League and Club

Enable Foreign Key Checks by removing the following from setting.py

'OPTIONS':{
            "init_command":"SET foreign_key_checks = 0;",
        }
