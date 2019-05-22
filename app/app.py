# -------------------------------------
# Тело приложения
# -------------------------------------

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user
from flask_admin.contrib import sqla
from flask import redirect, url_for, request
# импорт встроенных модулей
from config import Configuration
from flask import jsonify

# создаем приложение
app = Flask(__name__)
app.config.from_object(Configuration)

# подключаем БД и миграцию
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# импортируем все таблицы
from models import *

# проверка уровня доступа пользователя
class AdminMixin:
    def is_accessible(self):
        if current_user.has_role('superuser') or current_user.has_role('user') or current_user.has_role('admin'):
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect( url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form , model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


# запеты на доступ к редактированию и админке гостям
class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class PostAdminView(AdminMixin, BaseModelView):
    @expose('/')
    def index(self):
        post = Post()
        massive = jsonify(id=post.id,
                        created=post.created,
                        title=post.title,
                        slug=post.slug,
                        body=post.body)
        return self.render('admin/qindex.html', post=post, massive=massive)
    
class UserAdminView(AdminMixin, BaseModelView):
    @expose('/')
    def index(self):
        user = User()
        massive = jsonify(id=user.id,
                        email=user.email,
                        roles=user.roles)
        return self.render('admin/users.html', user=user, massive=massive)
    







# подключаем админку
admin = Admin(app, name='Admin', base_template='/base.html', template_mode='bootstrap3')




# подключаем вьюхи, ссылки на каждую таблицу в шапке
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(UserAdminView(User, db.session))

# права досупа
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)








