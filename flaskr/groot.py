from flask import Flask, render_template, session, request, redirect, flash, url_for
app = Flask(__name__)
import sqlite3 as sql
import db

@app.route("/")
def groot():
    # get info from challange table in database
    challenge_overview = db.get_db("""
    SELECT challenges.Title, levels.Name, challenges.Description, challenges.ID
    FROM challenges
    INNER JOIN levels ON challenges.Level=levels.Level;
    """)

    return render_template("index.html", challenge_overview = challenge_overview)

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template("login.html")        
    else:
        username_entered = request.form["username"]
        password_entered = request.form["password"]

        if not username_entered or not password_entered:
            return "Please input your data."
        
        user_info = db.get_db("SELECT username, password FROM user WHERE username = '{}' ".format(username_entered))

        # check if user_info is there
        if user_info:
            # compare username_entered to username in database
            if username_entered == user_info[0][0]:
                # compare password_entered to password in database
                if password_entered == user_info[0][-1]:
                    # return homepage
                    return redirect("/")           
                # if password is inaccurate return login page
                else: 
                    return("The password is incorrect. Please try again.")
            # if username is inaccurate return login page
        else:
            return("Wrong login information.")      

if __name__ == "__main__":
    app.run()