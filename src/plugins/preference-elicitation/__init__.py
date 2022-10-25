from flask import Blueprint, render_template, jsonify

# See https://github.com/staugur/Flask-PluginKit

__plugin_name__ = "firstplugin"
__version__ = "0.1.0"
__author__ = "Your Name"

bp = Blueprint(__plugin_name__, __plugin_name__)

# Accessible as http://localhost:5000/some-example
@bp.route("/some-example")
def some_example():
    return render_template("elicitation_index.html", plugin_name=__plugin_name__, plugin_author=__author__)

@bp.route("/preference-elicitation", methods=["GET", "POST"])
def preference_elicitation():
    result = dict()

    result["preferences"] = []
    # TODO Fill the list

    return jsonify(result)


def register():
    return {
        "bep": dict(blueprint=bp, prefix=None),
    }
