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


# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(row._asdict())
#   print(result_dicts)
#   print(len(result_dicts))

# print("type(result):", type(result))
  # result_all = result.all()
  # print("type(result_all):", type(result_all))
  # # print("result_all:", result_all)
  # print("type(result_all[0]):", type(
  #   result_all[0]))
  # print("result_all[0]:", result_all[0])

  # first_result_dict = result_all[0]._asdict()
  # print("type(first_result_dict):", type(first_result_dict))
  # print("first_result_dict:", first_result_dict)
