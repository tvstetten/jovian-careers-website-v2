from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bangaluru, India",
    "salery": "Rs. 10,00,000",
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "London, Great Britain",
    "salery": "Rs. 15,00,000",
  },
  {
    "id": 3,
    "title": "Full Stack Developer",
    "location": "Remote",
    # "salery": "Rs. 20,00,000",
  },
  {
    "id": 4,
    "title": "Data Analyst",
    "location": "Deli, India",
    "salery": "$120,000",
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                         company_name="Jovian Careers Inc.")


@app.route("/api/jobs")
def jobs_json():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
