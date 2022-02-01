from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("form.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect('/')

@app.route('/greetings')
def pozdro():
    return render_template("greetings.html")