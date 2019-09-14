from flask import Flask, render_template
import os

BASE_DIR = os.getcwd()

app = Flask(__name__,
            template_folder=os.path.join('/templates'),
            static_folder=os.path.join('/templates/static')
            )


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
