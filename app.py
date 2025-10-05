from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q", "")
    # intentionally vulnerable naive SQL (for demo only)
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM users WHERE id = %s" % q)  # unsafe
        rows = cur.fetchall()
    except Exception as e:
        rows = []
    return render_template_string("<h1>Results</h1><pre>{{rows}}</pre>", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
