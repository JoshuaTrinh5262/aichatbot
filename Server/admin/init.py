from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from routes import app

# app.config['SECRET_KEY'd3e] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

admin = Admin(app)

#View
from models import db, Users, Conversations

admin.add_view(ModelView(Users, db.session))

admin.add_view(ModelView(Conversations, db.session))


if __name__ == '__main__':
    app.run()