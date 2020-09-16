# python-flask demonstrating the flask applicaton development

-PREREQUISITES 
	Python installed , a text editor
- Setting up Flask
create virtual environment to install flask , there will be one virtual environemnt per project
COMMAND : py -m venv yourenvironemntname

- Activate environemnt
yourenvironemntname\Scripts\activate 

- Deactivate environemnt
yourenvironemntname\Scripts\deactivate 

- once activated , install flask
COMMAND : pip install flask

- set main file for flask 	
COMMAND: set FLASK_APP = app.py

- app.py will run when the application is run


- two ways to run flask 
METHOD 1:
Go to directory where main file is located
COMMAND : flask run    

if you want ot runa different file 
export FLASK_APP=app2.py  

METHOD 2:
add followin

if __name__ == "__main__":
    app.run(debug=True)
	
go to directory and run 
COMMAND : python app.py

