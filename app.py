from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings', methods=['post'])
def settings():
    print(request.form)
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)

#.\profile\Scripts\activate.ps1#