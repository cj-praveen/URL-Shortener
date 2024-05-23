from flask import Flask, render_template, request, redirect
from database import DataBase

app = Flask(__name__, static_folder="/")
db: DataBase = DataBase()


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/short", methods=["POST"])
def main() -> str:
    url: str= request.form.get("url")
    exists, uid = db.check_database(url)
    if not exists:
        uid = db.new_record(url)
    return render_template("index.html", uid=uid)


@app.route('/<uid>')
def redirect_url(uid):
    result = db.db.execute("SELECT URL FROM URLS WHERE UID=?", (uid,)).fetchone()
    if result:
        return redirect(result[0])
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
