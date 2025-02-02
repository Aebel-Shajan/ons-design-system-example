from flask import Flask, render_template
from jinja2 import ChainableUndefined

app = Flask(__name__) 
app.jinja_env.undefined = ChainableUndefined

@app.route("/") 
def home(): 
	return render_template(
        "index.jinja", 
        title="hello world",
        header="hello world"
    ) 

if __name__ == "__main__": 
	app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    ) 
