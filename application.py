from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application", methods=["POST"])
def submission():
    """Message that we've received input"""

    firstname = request.form.get("first-name")
    lastname = request.form.get("last-name")
    salary = request.form.get("salary")
    position = request.form.get("position")

    return render_template("submitted.html", first=firstname, last=lastname,
                                            position=position, salary=salary)



@app.route("/application-form")
def gather_info():
    """Take applicant input from form"""


    return render_template("application-form.html")
    # return "<html><body>This /app-form.</body></html>"



if __name__ == "__main__":
    app.run(debug=True)
