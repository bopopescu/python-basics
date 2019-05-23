from flask import Flask
app = Flask(__name__)


from src.controllers import (
	home_controller,
)

app.register_blueprint(home_controller.blueprint)