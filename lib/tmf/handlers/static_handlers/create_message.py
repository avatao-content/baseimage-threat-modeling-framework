# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from flask import jsonify


def create_message(message : str, data):
    return jsonify({
        "message" : message,
        "data" : data
    })
