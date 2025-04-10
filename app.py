# -------------------------------------------
# Author: Kanishka Peramunugama
# Email: kanishka96se@gmail.com
# Description: This project is a simple Flask-based Website URL Checker that allows users to input a URL and check if it uses HTTP or HTTPS.
#              It provides feedback on whether the website is secure or not.
# -------------------------------------------

from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables
    url = None
    protocol = None
    result = None

    # Check if the form is submitted (POST method)
    if request.method == 'POST':
        url = request.form['url']
        protocol = url.split(':')[0].upper() if ':' in url else 'UNKNOWN'

        # Determine if it's secure or not
        if protocol == "HTTPS":
            result = "secure"
        elif protocol == "HTTP":
            result = "not secure"
        else:
            result = "unknown"
        
        # Save the result to the session so that it persists on page load
        session['url'] = url
        session['protocol'] = protocol
        session['result'] = result

    # If reset button is pressed, clear the session data
    elif request.args.get('reset'):
        session.pop('url', None)
        session.pop('protocol', None)
        session.pop('result', None)

    return render_template('index.html', url=session.get('url'), protocol=session.get('protocol'), result=session.get('result'))


if __name__ == '__main__':
    app.run(debug=True)
