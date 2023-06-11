#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    name=request.form["first_name"]
    student_id=request.form["student_id"]
    strawberries=request.form["strawberry"]
    raspberries=request.form["raspberry"]
    apples=request.form["apple"]
    count= int(strawberries)+int(raspberries)+int(apples)
    # now=datetime.datetime.now()
    # timestamp=now.strftime("%B %d %Y %I:%M %p")
    print(request.form)
    return render_template("checkout.html", strawberries=strawberries, raspberries=raspberries, apples=apples, name=name, student_id=student_id)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
