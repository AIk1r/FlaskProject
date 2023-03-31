from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange, DataRequired


class QuestForm(FlaskForm):
    way = SelectField('Выберите направление',
                      coerce=int,
                      choices=[
                          (0, 'Север'),
                          (1, 'Восток'),
                          (2, 'Юг'),
                          (3, 'Запад')
                      ],
                      render_kw={
                          'class': 'form-control'
                      },
                      validators=[InputRequired()],
    )
    steps = IntegerField('Как далеко хотите пойти?', validators=[NumberRange(min=1), DataRequired()],
                         default=1,
                         render_kw={
                             'class': 'form-control'
                         },
    )
    submit = SubmitField('Выполнить')