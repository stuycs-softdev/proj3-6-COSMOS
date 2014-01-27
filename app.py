from flask import Flask, url_for, render_template, redirect, request, session
import auth

app = Flask(__name__)
app.secret_key = 'key'

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if (auth.authenticate(username, password)):
            session["username"] = username
            return render_template("portfolio.html", username = session["username"])
        else:
            return render_template("login.html", error=True)
                
@app.route("/register", methods = ["GET", "POST"])
def register():
    error = None
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        if (request.form["username"]=="" or request.form["password"]==""):
            return render_template("register.html",error="empty")
        elif (request.form["cpassword"]==""):
            return render_template("register.html",error="badc")
        elif (request.form["username"]==request.form["password"]):
            return render_template("register.html",error="lazy")
        elif request.form["password"]!=request.form["cpassword"]:
            return render_template("register.html",error="wrongc")
        if (request.form["username"]==request.form["cpassword"] and auth.register(username, password)):
            session['username'] = username
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))
    
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
