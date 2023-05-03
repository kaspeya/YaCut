from http import HTTPStatus
from re import match

from flask import jsonify, request

from settings import (INVALID_URL_NAME, NO_REQUEST_BODY, NO_REQUIRED_FIELD,
                      NOT_FOUND, REGEX_PATTERN)

from . import app, db
from .error_handlers import InvalidAPIUsage, check_inique_short_url
from .models import URLMap
from .utils import get_unique_short_url


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage(NO_REQUEST_BODY)

    if 'url' not in data:
        raise InvalidAPIUsage(NO_REQUIRED_FIELD, HTTPStatus.BAD_REQUEST)

    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_url()

    custom_id = data['custom_id']
    if len(custom_id) > 16 or not match(REGEX_PATTERN, custom_id):
        raise InvalidAPIUsage(INVALID_URL_NAME, HTTPStatus.BAD_REQUEST)

    if check_inique_short_url(custom_id):
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.', HTTPStatus.BAD_REQUEST)

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage(NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
