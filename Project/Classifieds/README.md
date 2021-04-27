Example 39: This project shows how to integrate a database in your web app.

## Quick Start
### Local Test Setup
There is no setup required for the database if you have the requirements installed then, the python file will create the database locally.

he required libraries are:
```
Flask==1.0.2
Jinja2==2.10
flask-sqlalchemy
```
They are in requirements.txt which will help with easy of install.


First, we need to install a Python 3 virtual environment with:
```
sudo apt update
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

To get to the website you need to route to this site:
```
http://127.0.0.1:5287/classifieds
```

Since the database it set up locally, there will be no recent ads and there will not be any accounts made. So you will have to make an account to see all of the tabs offered which are Search Ads, Post As, My Profile, My Ads, Recent Ads. When you log in it will create a session until you log out, then the session will end.

After you post an ad you will see it in the my ads tab, where you can view your ad, edit your ad, or delete the add.

The Recents Ads tab will show you the recent ads created from all users, and the search ads will search through all of the ads including the ones from other users.
