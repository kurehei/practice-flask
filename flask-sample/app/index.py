from flask import Flask, render_template
from markupsafe import escape
import model
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/user/<id>")
def user(id):
    user_info = model.get_user_info(id)
    return f"{user_info}"

@app.route("/thanks")
def thanks():
    return render_template('thanks.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)