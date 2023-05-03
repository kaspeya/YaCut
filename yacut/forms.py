from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import (FORM_LEN_MSG, FORM_REGEX_MSG, FORM_REQUIRED_FIELD,
                      MAX_LEN_CUSTOM_ID, REGEX_PATTERN)


class YacutForm(FlaskForm):
    """Форма модели URLMap"""
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=FORM_REQUIRED_FIELD),
            Length(1, 256)
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                1,
                max=MAX_LEN_CUSTOM_ID,
                message=FORM_LEN_MSG
            ),
            Regexp(
                REGEX_PATTERN,
                message=FORM_REGEX_MSG
            ),
            Optional()
        ])
    submit = SubmitField('Создать')
