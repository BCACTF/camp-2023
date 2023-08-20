from flask import Flask, render_template, send_file

app = Flask(__name__)
app.static_folder = '.'
app.template_folder = '.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run('0.0.0.0','9999')