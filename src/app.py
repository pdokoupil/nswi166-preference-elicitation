from flask import Flask, render_template
from flask_pluginkit import PluginManager

# See https://github.com/sh4nks/flask-plugins/blob/master/example/app.py

# Default Settings
SECRET_KEY = "this-key-is-not-secure"

# Initialize flask
app = Flask(__name__)

# Initialize the plugin manager
plugin_manager = PluginManager()
plugin_manager.init_app(app)

@app.route("/")
def index():
    return render_template("index.html", some_var = "Some text")

if __name__ == "__main__":
    app.run(debug=True)
