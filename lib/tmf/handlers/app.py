# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from flask import Flask

from tmf.handlers.static_handlers import system_blueprint, component_blueprint, boundary_blueprint
from tmf.handlers.error_handlers import not_found


if __name__ == "__main__":
    print("starting server")

    app = Flask(__name__)

    app.register_blueprint(system_blueprint)
    app.register_blueprint(component_blueprint)
    app.register_blueprint(boundary_blueprint)
    app.register_error_handler(404, not_found)

    app.run(debug=True)
