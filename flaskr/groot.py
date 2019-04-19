from flask import Flask, render_template, session, request, redirect, flash, url_for
app = Flask(__name__)
import sqlite3 as sql

@app.route("/")
def groot():
    return render_template("index.html", name="groot")
    # con = sql.connect("groot_tasks.db")

if __name__ == "__main__":
    app.run()