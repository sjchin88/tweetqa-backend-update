import connexion
from decouple import config

from flask_sqlalchemy import SQLAlchemy 


app = connexion.App(__name__, specification_dir='./')
SECRET_KEY = config('SECRET_KEY')

# App Config
app.app.config['SECRET_KEY'] = SECRET_KEY


app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + SECRET_KEY + '@ljdub.com:3306/mysql_database'  
db = SQLAlchemy(app.app)

#app.add_api('../swagger.yml')