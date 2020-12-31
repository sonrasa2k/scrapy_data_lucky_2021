import cv2 as cv
import numpy as np
import os
from app import app
from collections import Counter
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import  base64
import pandas as pd
day_in_data = []
moth_in_data = []
rank_in_data = []

def get_data(path_csv):
    global day_in_data
    global moth_in_data
    global rank_in_data
    data = pd.read_csv(path_csv)
    day_in_data = data[['day']].values
    moth_in_data = data[['month']].values
    rank_in_data = data[['rank']].values
    print(rank_in_data[0])

@app.route('/')
def upload_form():
    return render_template('index.html')
@app.route('/lucky',methods=['POST'])
def get_date():
    day = request.form.get('date')
    month = request.form.get('month')
    get_data("lucky.csv")
    rank_final = ""
    for i in range(len(day_in_data)):
        if int(day) == int(day_in_data[i]) and int(month) == int(moth_in_data[i]):
            rank_final = int(rank_in_data[i])
    return render_template('index.html',rank = rank_final)


if __name__ == "__main__":
    app.run()