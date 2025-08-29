# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<meta charset="utf-8">
<title>POST Echo</title>
<h1>Send a POST and I’ll echo its text</h1>

<form method="post" action="/echo">
  <textarea name="text" rows="6" cols="60" placeholder="Type here..."></textarea><br>
  <button type="submit">Send</button>
</form>

{% if result is not none %}
<hr>
<h2>Received:</h2>
<pre>{{ result | e }}</pre>
{% endif %}
"""

@app.get("/")
def index():
    return render_template_string(PAGE, result=None)

@app.post("/echo")
def echo():
    # Prefer form field named "text", else fall back to raw body text
    text = request.form.get("text")
    if not text:
        text = request.get_data(as_text=True) or ""
    return render_template_string(PAGE, result=text)

if __name__ == "__main__":
    app.run(debug=True)
