from flask import jsonify, request

from utils.endpoint import Endpoint, setup
from utils.db import get_db
from random import choice
import rethinkdb as r

@setup
class UsageStats(Endpoint):
    """
    This endpoint returns the usage statistics of the key requesting it. No parameters are required.
    """
    params = []

    def generate(self, avatars, text, usernames, kwargs):
        table = r.table('keys').get(request.headers.get('authorization', '')).run(get_db())
        return jsonify(table["usages"])
