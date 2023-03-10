from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from flask_hcaptcha import hCaptcha
import os

app = Flask(__name__)

app.config["HCAPTCHA_SITE_KEY"] = site_key=os.environ["HCAPTCHA_SITE_KEY"]
app.config["HCAPTCHA_SECRET_KEY"]=os.environ["HCAPTCHA_SECRET_KEY"]
hcaptcha = hCaptcha(app)

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=load_jobs_from_db(),
                         company_name="Jovian Careers Inc.")


@app.route("/job/<id>")
def job_json(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=["post"])
def apply_to_job(id):
  if not hcaptcha.verify():
    return "Invalid Captcha", 404
  else:
    application = request.form
    job = load_job_from_db(id)
    # store this in the db
    add_application_to_db(id, application)
    
    # return jsonify(data)
    return render_template("application_submitted.html", application=application, job=job)
  
@app.route("/api/job/<id>")
def api_job_json(id):
  return jsonify(load_job_from_db(id))

@app.route("/api/jobs")
def api_jobs_json():
  return jsonify(load_jobs_from_db())


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
