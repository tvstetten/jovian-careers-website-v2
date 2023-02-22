import os
from sqlalchemy import create_engine, text

db_conn_str = os.environ["DB_CONNECTION_STRING"]
engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  
    result_jobs = []
    for row in result.all():
      result_jobs.append(row._asdict())
  return result_jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})

    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    # use the complete application-dict and simply add the job_id
    params = application.copy()
    params["job_id"] = job_id
    result = conn.execute(query, params)
