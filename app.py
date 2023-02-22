from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=load_jobs_from_db(),
                         company_name="Jovian Careers Inc.")


@app.route("/api/jobs")
def jobs_json():
  return jsonify(load_jobs_from_db())


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
