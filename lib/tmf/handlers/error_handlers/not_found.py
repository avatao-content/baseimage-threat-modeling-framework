# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from flask import make_response, jsonify


def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
