from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/bq2134', methods=['GET'])
def page():
    return render_template('my_page.html')


if __name__ == '__main__':
    app.run()
