from flask import Blueprint, render_template

# See https://github.com/staugur/Flask-PluginKit

__plugin_name__ = "firstplugin"
__version__ = "0.1.0"
__author__ = "Your Name"

bp = Blueprint(__plugin_name__, __plugin_name__)

@bp.route("/some-example")
def some_example():
    return render_template("elicitation_index.html", plugin_name=__plugin_name__, plugin_author=__author__)

def register():
    return {
        "bep": dict(blueprint=bp, prefix=None),
    }
