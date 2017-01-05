from bottle.bottle import route, run, template
import psycopg2

@route('/index')
def index():
    conn = psycopg2.connect(database="postgres_db", user="postgres", password="1", host="127.0.0.1", port="5432")
    if conn.closed != 0:
        return "Can't connect to database"
    else:
        curs = conn.cursor()
        curs.execute("select * from student order by id asc;")
        rows = curs.fetchall()
    conn.close()
    return template('index', result=rows)

run(host='localhost', port=8080, debug=True)
