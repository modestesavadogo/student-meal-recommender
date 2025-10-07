from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        budget = request.form.get("budget")
        time = request.form.get("time")
        return f"Recommended meal for budget {budget} MAD and time {time} min"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
