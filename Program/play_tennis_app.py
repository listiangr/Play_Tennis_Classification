from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Open and load the saved model
model_file = open('play_tennis_model.pkl', 'rb')
model = pickle.load(model_file)

# Route for the main page
@app.route('/')
def index():
    # Return the HTML page with default values for the result
    return render_template('index.html', hasil=None, outlook=None, temp=None, humidity=None, wind=None)

# Route for making predictions based on user input
@app.route('/predict', methods=['POST'])
def predict():
    '''
    Function to predict if you can play tennis based on user input
    and show the result on the HTML page
    '''
    # Get user input data from the form on the HTML page
    outlook = int(request.form['outlook'])  
    temp = int(request.form['temp'])       
    humidity = int(request.form['humidity'])
    wind = int(request.form['wind'])      
    
    # Create a 2D array with user input to use for prediction
    x = np.array([[outlook, temp, humidity, wind]])
    
    # Predict the result using the loaded machine learning model
    prediction = model.predict(x)
    
    # Define categories for outlook, temperature, humidity, and wind to display in the result
    outlooks = ['Overcast', 'Rain', 'Sunny']
    temps = ['Cool', 'Hot', 'Mild']
    humiditys = ['High', 'Normal']
    winds = ['Strong', 'Weak']
    
    # Determine the result based on the prediction (0 means cannot play, 1 means can play)
    if(prediction == 0):
        play = "You cannot play tennis."
    elif(prediction == 1):
        play = "You can play tennis."
    
    # Return the prediction result to the HTML page, along with the user's selected inputs
    return render_template('index.html', hasil=play, outlook=outlooks[outlook], temp=temps[temp],
                           humidity=humiditys[humidity], wind=winds[wind])

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
