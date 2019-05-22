# -------------------------------------
# Вьюхи, рендеринг страниц
# -------------------------------------

from main import app
from flask import render_template, flash, redirect
from forms import LoginForm
from flask_security import login_required
from models import Post

# запускаем декоратор для URL
# инициализируем главную страницу шаблон
@app.route('/')
def index():
    # можно задать переменную для функции
    # и связать с аргументом, передать на HTML страницу
    return render_template('index.html')

# инициализируем страницу "домой"
@app.route('/home')
def home():
    return render_template('home.html')

# инициализируем страницу "контакты"
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# инициализируем страницу "контакты"
@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


# инициализируем страницу "login"
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign IN', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

