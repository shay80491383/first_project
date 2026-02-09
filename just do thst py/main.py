from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        user_input = request.form.get('password')
        if user_input == 'a1':
            return render_template('done.html')
        else:
            message = "چرند وارد نکن :/" 
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
