# 
## Quick start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/argon-dashboard-django.git
$ cd argon-dashboard-django
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

## How to Install MYSQL
(Ubuntu 20.0.4 instructions)
>1. Once on command line, type in "sudo apt-get install mysql-server"
>2. After installation has occured, type in "sudo mysql_secure_installation utility"
>3. Upon entering the above command, you will be asked to create a user which will allow you to control MYSQL.
>4. After the installation of the user, type the following 2 commands:
>     "sudo ufw enable"
>     "sudo ufw allow mysql"
>(This will allow remote access to your database)
>5. To start the server type in "sudo systemctl start mysql"
>5a. To start the server starts on reboot of your system, type in "sudo systemctl enable mysql"
>6. Enter your server by typing in "/usr/bin/mysql -u root -p" and enter your password and you should see a shell which has the line "mysql>"



## How to install Database connector
> 1. Enter into command line and enter "pip install mysql-connector-python"
> 2. Once download has completed, you now have the database connector.



## Getting Started
> 1. After running above steps, go to http://127.0.0.1:8000/
> 2. Log into the site (or create an account)
> 3. On the left side select "Databases"
> 4. On the new screen, select "MYSQL" and enter in the host, username, and password and press select
> 5. The next page will show you the list of the databases within the given information.
