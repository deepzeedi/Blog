from wtforms import Form, StringField, TextAreaField

# Форма ввода и редактирования постов
class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Post')