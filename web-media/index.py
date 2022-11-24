from flask import Flask, render_template

app = Flask(__name__)                                                                                                            

@app.route('/')
def index():
    data = ['kiki']
    return render_template('login.html',data = data);

if __name__ == '__main__':
    app.run(debug=True)
