from flask import Flask, render_template, jsonify, request
app = Flask(__name__) 		


@app.route("/")
def homepage():
        return render_template('mainpage/index.html')
    
@app.route("/sub")
def subpage():
        return render_template('sub/sub.html')

if __name__ == "__main__":
    app.run()