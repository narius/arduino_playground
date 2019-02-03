# This is a small flask page to turn on and off leds
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.orm import relationship, backref
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import UserMixin, RoleMixin, current_user
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
import click
import code
import io
import time
from pyfirmata import ArduinoNano, util
import datetime
import time

board = ArduinoNano('/dev/cu.usbserial-1410')
led_blue = board.get_pin('d:4:o')
led_blue.write(0)
moisture = board.get_pin('a:7:i')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = "hadf38746"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECURITY_PASSWORD_SALT'] = '93iu4hkejfndm,'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
admin = Admin(app, name='flask-arduino', template_mode='bootstrap3')


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id =db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))


class MeasurementTypeValue(db.Model):
    __tablename__ = 'measurement_type_value'
    id = db.Column(db.Integer, primary_key=True)
    value_id = db.Column('value_id', db.Integer, db.ForeignKey('measurement.id'))
    type_id = db.Column('type_id', db.Integer, db.ForeignKey('measurement_type.id'))


class MeasurementType(db.Model):
    __tablename__ = 'measurement_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


class Measurement(db.Model):
    __tablename__ = 'measurement'
    id = db.Column(db.Integer, primary_key=True)
    type = relationship('MeasurementType', secondary='measurement_type_value',
                         backref=backref('measurement', lazy='dynamic'))
    value = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


admin.add_view(ModelView(MeasurementType, db.session))
admin.add_view(ModelView(Measurement, db.session))

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/ledBlue_on')
def ledBlue_on():
    led_blue.write(1)
    return render_template('hello.html')

@app.route('/ledBlue_off')
def ledBlue_off():
    led_blue.write(0)
    print("status ledblue")
    print(led_blue.read())
    moist = {'value': '123',
             'time': '2018-12-30'}
    return render_template('hello.html')


@app.context_processor
def inject_values():
    moist = {'value': moisture.read(),
             'time': datetime.datetime.now()}
    led_blue_status = 'on' if led_blue.read()==1 else 'off'
    return {'blue_status':led_blue_status,
            'moist': moist}


if __name__ == '__main__':
    manager.run()
