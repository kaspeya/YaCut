from flask import flash, redirect, render_template, request

from . import app, db
from .forms import YacutForm
from .models import URLMap
from .utils import get_unique_short_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Вью функция главной страницы"""
    form = YacutForm()
    custom_id = form.custom_id.data
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if not custom_id:
        custom_id = get_unique_short_url()
    if URLMap.query.filter_by(short=custom_id).first():
        form.custom_id.errors = [f'Имя {custom_id} уже занято!']
        return render_template('index.html', form=form)
    url_map = URLMap(
        original=form.original_link.data,
        short=custom_id,
    )
    db.session.add(url_map)
    db.session.commit()
    flash('Ваша новая ссылка: '
          f'<a href="{request.base_url}{custom_id}">'
          f'{request.base_url}{custom_id}</a>')
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def yacut_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
