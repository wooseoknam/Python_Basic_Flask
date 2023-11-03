from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired

class UserForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    age = IntegerField('나이', validators=[DataRequired()])
    image_name = FileField('사진', validators=[
        # FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')    # By default, flask-wtf does not show any error message if validation fails, message - error message = None
    ])


# 이미지 파일은 아니지만 확장자가 jpg나 png인 경우,,,,