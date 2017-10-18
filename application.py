from flask import Flask
from flask import render_template

# EB looks for an 'application' callable by default.
app = Flask(__name__)

# index page
@app.route('/')
def index():
    return render_template('index.html')

# run the app.
if __name__ == "__main__":
    app.debug = True
    app.run()
