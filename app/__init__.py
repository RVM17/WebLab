from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

from app.asm2205.st16 import bp as bp0516


bps = [
    ["[2205-16] Матвеев 2205", bp0516]

]


for i, (title, bp) in enumerate(sorted(bps), start=1):
    app.register_blueprint(bp, url_prefix=f"/st{i}")


@app.route("/")
def index():
    return render_template("index.tpl", bps=sorted(bps))


@app.route("/api/", methods=['GET'])
def api():
	sts = []
	for i, (title, bp) in enumerate(sorted(bps), start=1):
		sts.append([i, title])
	return jsonify({'sts': sts})
