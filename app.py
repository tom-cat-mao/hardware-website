from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

class AppointmentForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    phone = StringField('电话', validators=[DataRequired()])
    service = StringField('服务类型', validators=[DataRequired()])
    message = TextAreaField('留言')
    submit = SubmitField('提交预约')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        # 这里可以添加处理预约表单的逻辑
        return redirect(url_for('index'))
    return render_template('appointment.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
