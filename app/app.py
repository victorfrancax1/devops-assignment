import os
import psycopg2
from psycopg2 import Error
from flask import Flask, request, jsonify

app = Flask(__name__)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        execute_query("insert into random (uuid) select md5(random()::text) from generate_Series(1,1) s;")
    else:
        execute_query("select * from random order by random() limit 10;")
    return jsonify({"status": "ok"}) 

def execute_query(query):
    try:
        connection = psycopg2.connect(user=POSTGRES_USER,
                                      password=POSTGRES_PASSWORD,
                                      host=POSTGRES_HOST,
                                      port="5432",
                                      database=POSTGRES_DB)

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
