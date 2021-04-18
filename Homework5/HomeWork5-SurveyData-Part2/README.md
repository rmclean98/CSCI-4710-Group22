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

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

On the home page there will be two links:
```
1. Map Format of data
2. Ontology Graph of data
```

The map format will display a map of the world and has a legend in the top left corner for which colors the countries are that contain data. You can click on the countries and there 4 tables of data from part 1 will be displayed.

The ontology graph display each country as a subgraph and each country has 4 subgraphs containing the one of each tables from part 1.
When you over over a point it will get larger to indicate you are over a point. To drag the graphs you have to click on the country name and drag it around and to display the data of each group you have to click on the subgraph of each country.
