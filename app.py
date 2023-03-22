from flask import Flask, render_template, request, redirect
import datetime

app=Flask(__name__)

messages=[]

@app.route('/')
def index():
    return render_template("index.html.jinja2", messages=messages)

@app.route('/post/add/', methods=['POST'])
def add_message():
    text = request.form.get('message')
    timestamp = datetime.datetime.now()
    messages.append({'text': text, 'timestamp': timestamp})
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)