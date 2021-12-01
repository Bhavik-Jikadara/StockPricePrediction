from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict/', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Open = request.form.get('Open')
        High = request.form.get('High')
        Low = request.form.get('Low')
        Volume = request.form.get('Volume')
    
    prediction = utils.preprocess(Open, High, Low, Volume)

    return render_template('prediction.html', prediction = prediction)



# @app.errorhandler(404)
# def error(e): 
#     return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
