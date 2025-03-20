from flask import Flask, render_template, request
import helper
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        processed_input = helper.getPrediction(user_input)
    else:
        processed_input = ""
    return render_template('index.html', processed_input=processed_input)

if __name__ == '__main__':
    app.run(debug=True)
