from flask import Flask, render_template

app = Flask(__name__) 


@app.route("/") 
def home(): 
	return render_template(
        "index.jinja", 
        title="hello world",
        header="hello world"
    ) 

if __name__ == "__main__": 
	app.run(debug=True) 
