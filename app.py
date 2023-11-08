from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estimate_pi', methods=['GET', 'POST'])
def estimate_pi():
    if request.method == 'POST':
        num_simulations = int(request.form['num_simulations'])
        inside_circle = 0

        for _ in range(num_simulations):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)

            if x ** 2 + y ** 2 <= 1:
                inside_circle += 1

        pi_estimate = 4 * inside_circle / num_simulations

        return render_template('result.html', pi_estimate=pi_estimate)


if __name__ == '__main__':
    app.run(debug=True)
