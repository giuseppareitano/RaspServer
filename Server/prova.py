from flask import render_template
import connexion

import RPi.GPIO as GPIO
import time

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    app.run(host='/*your ip*/', port=5000, debug=False)
    while True:
        a = GPIO.input(4)
        if a == 1:
            print("a = 1")
        if a == 0:
            print("a = 1")
        time.sleep(10)