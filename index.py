from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess key'


class LoginForm(FlaskForm):
    adminName = StringField(validators=[DataRequired()])
    adminPsd = PasswordField(validators=[DataRequired()])
    login = SubmitField()


@app.route('/admin')
def admin_login():
    form = LoginForm()
    return render_template('admin.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
