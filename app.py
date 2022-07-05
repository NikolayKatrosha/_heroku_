from flask import Flask, render_template, request

def convert(weight, unit):
    if unit == "pounds":
        weight = round( float(weight) / 2.205, 2)
        unit = "kilograms"
    elif unit == "kilograms":
        weight = round( float(weight) * 2.205, 2)
        unit = "pound"

    return weight, unit


app = Flask(__name__)



@app.route('/')
def main():
    return render_template("main.html")



@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        weight = request.form['weight']
        unit = request.form['unit']
        print(f"{weight} {unit}")
        weight, unit = convert(weight, unit)
        return render_template('index.html', weight=weight, unit=unit)
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)