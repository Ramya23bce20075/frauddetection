from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('payments.pkl', 'rb'))

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/pred', methods=['POST'])
def pred():
    try:
        form = request.form
        x = np.array([[float(form['step']), float(form['type']), float(form['amount']),
                       float(form['oldbalanceorg']), float(form['newbalanceorig']),
                       float(form['oldbalancedest']), float(form['newbalancedest']), 0.0]])
        prediction = model.predict(x)
        return render_template('result.html', pred=str(prediction[0]))
    except Exception as e:
        return f"Error: {e}"

if _name_ == '_main_':
    app.run(debug=True)
