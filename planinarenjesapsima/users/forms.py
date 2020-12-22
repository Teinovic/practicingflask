from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from planinarenjesapsima.models import User




class LoginForm(FlaskForm):
    email = StringField('Email adresa', validators=[DataRequired(), Email()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    submit = SubmitField('Prijavi se')


class RegistrationForm(FlaskForm):
    email = StringField('Email adresa', validators=[DataRequired(),Email()])
    username = StringField('Nalog', validators=[DataRequired()])
    password = PasswordField('Lozinka', validators=[DataRequired(), EqualTo('pass_confirm', message='Šifre moraju biti iste!')])
    pass_confirm = PasswordField('Potvrdi lozinku', validators=[DataRequired()])
    submit = SubmitField('Registruj se!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Ta email adresa je već registrovana!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nažalost, to korisničko ime je zauzeto.')


class UpdateUserForm(FlaskForm):
    email = StringField('Email adresa', validators=[DataRequired(),Email()])
    username = StringField('Korisničko ime', validators=[DataRequired()])
    picture = FileField('Ažuriraj profilnu sliku', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Ažuriraj')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Ta email adresa je već registrovana!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nažalost, to korisničko ime je zauzeto.')
