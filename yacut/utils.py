import random
from string import ascii_letters, digits

from .models import URLMap

SYMBOLS_CHOICE = list(ascii_letters + digits)


def get_unique_short_url():
    """Алгоритм формирования коротких идентификаторов переменной длины"""
    short = ''.join(random.choices(SYMBOLS_CHOICE, k=6))
    while URLMap.query.filter_by(short=short).first():
        return get_unique_short_url()
    return short
