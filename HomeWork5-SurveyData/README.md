Example 39: This project shows how to integrate a database in your web app.

## Quick Start
### Local Test Setup
There is no setup required for the database if you have the requirements installed then, the python file will create the database locally.

The required libraries are:
```
Flask==1.0.2
Jinja2==2.10
flask-sqlalchemy
sklearn
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

To fulfill all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

The results are split up into 4 tables:

Table 1: Males with Age less than or equal to 35
```
Grouped By Country and Clustered using Kmeans for groups with more than 10 records.
First 15 records are displayed here. Please click on the pagination to access next set of records in each table
```
Table 2: Males with Age Greater than or equal to 36
```
Grouped By Country and Clustered using Kmeans for groups with more than 10 records.
First 15 records are displayed here. Please click on the pagination to access next set of records in each table
```
Table 3: Females with Age less than or equal to 35
```
Grouped By Country and Clustered using Kmeans for groups with more than 10 records.
First 15 records are displayed here. Please click on the pagination to access next set of records in each table
```
Table 4: Females with Age greater than or equal to 36
```
Grouped By Country and Clustered using Kmeans for groups with more than 10 records.
First 15 records are displayed here. Please click on the pagination to access next set of records in each table
```

This project was developed and tested on Ubuntu
