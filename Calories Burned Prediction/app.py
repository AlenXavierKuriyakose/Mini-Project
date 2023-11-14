from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained XGBoost model
model = joblib.load('./model (1).pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        gender = request.form['gender']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        duration = request.form['duration']
        heart_rate = request.form['heart_rate']
        body_temp = request.form['body_temp']

        # Create a DataFrame with the user input
       
        input_data = pd.DataFrame([[int(gender), int(age),float(height), float(weight), float(duration), float(heart_rate), float(body_temp)]])
        input_data = pd.DataFrame(data=input_data.values, columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate',
       'Body_Temp'])

        # Make predictions using the model
        prediction = model.predict(input_data)
        print(input_data)
        list1=[gender,age,height,weight,duration,heart_rate,body_temp,prediction,"Male","Female"]

        # You can format the prediction as needed
        return render_template('index.html', data=list1)
        #return f'Predicted Value: {prediction[0]}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
