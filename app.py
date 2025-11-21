from flask import Flask, render_template_string
from utils import load_json
from detector import compute_score, classify

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Fake App Detector</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .item { background:#f2f2f2; padding:15px; border-radius:8px; margin-bottom:15px; width:420px; }
    </style>
</head>
<body>

<h2>Fake App Detector (Multiple Apps)</h2>

{% for entry in results %}
<div class="item">
    <p><b>Official App:</b> {{ entry.official }}</p>
    <p><b>Test App:</b> {{ entry.name }}</p>
    <p><b>Score:</b> {{ entry.score }}/100</p>
    <p><b>Result:</b> {{ entry.label }}</p>
</div>
{% endfor %}

</body>
</html>
"""

@app.route("/")
def home():
    official = load_json("official_app.json")
    fake_apps = load_json("fake_app.json")

    results = []
    for sample in fake_apps:
        score = compute_score(sample, official)
        label = classify(score)

        results.append({
            "official": official["app_name"],
            "name": sample["app_name"],
            "score": score,
            "label": label
        })

    return render_template_string(HTML_PAGE, results=results)


if __name__ == "__main__":
    app.run(debug=True)
