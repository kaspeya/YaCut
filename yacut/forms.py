from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

import settings


class YacutForm(FlaskForm):
    """Форма модели URLMap"""
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message=settings.FORM_REQUIRED_FIELD),
                    Length(1, 256)]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                1, settings.MAX_LEN_CUSTOM_ID,
                message=settings.FORM_LEN_MSG),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
