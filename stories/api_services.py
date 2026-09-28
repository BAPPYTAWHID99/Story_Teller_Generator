import json
from typing import Dict

import requests

QUOTABLE_API_URL = 'https://api.quotable.io/random'


def get_random_quote() -> Dict[str, str]:
    try:
        response = requests.get(QUOTABLE_API_URL, timeout=5)
        response.raise_for_status()
        payload = response.json()
        quote = payload.get('content') or payload.get('quote')
        author = payload.get('author') or payload.get('authorName')
        if quote and author:
            return {'quote': quote.strip(), 'author': author.strip()}
    except (requests.RequestException, ValueError, TypeError, KeyError, json.JSONDecodeError, Exception):
        return {'quote': '', 'author': ''}

    return {'quote': '', 'author': ''}
