
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


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
        )

# запеты на доступ к редактированию и админке гостям
class HomeAdminView(AdminMixin, AdminIndexView):
    pass

# Админка для админа
class AdminView(AdminMixin, BaseModelView):
    @expose('/')
    def home(self):
        return self.render('admin/index.html')


    @expose('/post')
    def post(self):
        post = Post()
        massive = jsonify(id=post.id,
                        created=post.created,
                        title=post.title,
                        slug=post.slug,
                        body=post.body)
        return self.render('admin/posts.html', post=post, massive=massive)
    
    @expose('/user')
    def home(self):
        return self.render('admin/users.html')


# подключаем админку
admin = Admin(app, name='Admin', template_mode='bootstrap3')


#admin.add_view(MyView(name='Custom Views', endpoint='customviews'))
admin.add_view(AdminView(Post, db.session))
#admin.add_view(MyModelView(Role, db.session))
#admin.add_view(MyModelView(User, db.session))

# подключаем вьюхи, ссылки на каждую таблицу в шапке
#admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Post, db.session))



# права досупа
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)








