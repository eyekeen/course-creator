import os

from flask import Flask, render_template, request, redirect, url_for, session, g, flash, render_template_string

from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from sqlalchemy import text

from .models import db_session
from .models.users import User


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    login_manager = LoginManager()
    login_manager.init_app(app)

    db_session.global_init("db/testing.db")
    sess = db_session.create_session()
    

    @app.route('/')
    def index():
        return render_template('index.html')
   
    @app.route('/rating')
    def rating():
        return render_template('test/rating.html')

    @login_manager.user_loader
    def load_user(user_id):
        return sess.query(User).filter_by(id=user_id).first()

    @app.route('/auth/login', methods=('GET', 'POST'))
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = sess.query(User).filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                return render_template_string(
                    "Invalid username or password"
                 )
        return render_template('auth/login.html')

    @app.route('/auth/register', methods=["GET", "POST"])
    def register():
        if request.method == 'POST':
            new_user = User(
                        surname=request.form['surname'],
                        name=request.form['name'],
                        email=request.form['email'],
                        age=request.form['age'],
                        )
            new_user.set_password(request.form['password'])
            sess.add(new_user)
            sess.commit()
            return redirect(url_for('login'))
        return render_template('auth/register.html')


    @app.route('/auth/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/profile', methods=["GET", "POST"])
    @login_required
    def profile():
        if request.method == 'POST':
            user = sess.query(User).filter_by(id = current_user.id).first()
            if request.form['surname']:
                user.surname = request.form['surname']
            if request.form['name']:
                user.name = request.form['name']
            if request.form['email']:
                user.email = request.form['email']
            if request.form['age']:
                user.age = request.form['age']
            
            sess.commit()

            return 'ok'
        return render_template('user/profile.html')
    

    @app.route('/profile/updatepassword', methods=["POST"])
    @login_required
    def updatepassword():
        user = sess.query(User).filter_by(id = current_user.id).first()

        user.set_password(request.form['new_password'])
            
        sess.commit()

        return 'ok'


    @app.route('/test/testmaker')
    @login_required
    def testmaker():
        return render_template('test/testmaker.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    return app