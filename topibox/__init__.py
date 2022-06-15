import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)
    # register the database commands
    #from topibox import db
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    #@app.route("/hello")
    #def hello():
    #    return "Hello, World!"

    

    # apply the blueprints to the app
    from topibox.main import bp as main_bp
    app.register_blueprint(main_bp)




    return app
