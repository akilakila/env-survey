from http.server import *
import os
import sys
import subprocess
from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    calc_cat = False
    if request.method == 'POST':
        form = request.form
        calc_cat = calc_cat(form)
    return render_template('index.html', calc_cat=calc_cat)

def calc_cat(self):
    input = self.get_body()
    dict = json.loads(input)

    #converts the strings from the dict into ints
    sum = 0
    for key in dict:
        num = int(dict[key])
        sum += num

    sum = sum//5
    category = "None"
    if sum < 2:
        category = "category 1"
        return category
    elif sum == 3:
        category = "category 2"
    elif sum == 4:
        category = "category 3"
    elif sum == 5:
        category = "category 4"
    else:
        print("error")
    
    return category