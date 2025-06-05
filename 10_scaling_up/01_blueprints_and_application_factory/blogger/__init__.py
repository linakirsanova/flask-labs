from flask import Flask

def create_app():
  app = Flask(__name__)

  app.secret_key = 'hello_world'
  app.config.from_object(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  from .models import db
  db.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .blog import blog as blog_blueprint
  app.register_blueprint(blog_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  with app.app_context():
    db.create_all()

  return app

