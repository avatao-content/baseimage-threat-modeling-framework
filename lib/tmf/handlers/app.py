# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from flask import Flask

from tmf.handlers.static_handlers import system_blueprint, component_blueprint, boundary_blueprint, data_flow_blueprint
from tmf.handlers.error_handlers import not_found, bad_request


if __name__ == "__main__":
    print("starting server")

    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    app.register_blueprint(system_blueprint)
    app.register_blueprint(component_blueprint)
    app.register_blueprint(boundary_blueprint)
    app.register_blueprint(data_flow_blueprint)

    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)

    app.run(debug=True)
