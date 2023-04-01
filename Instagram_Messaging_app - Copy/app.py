#This is for all the library used in this app.
import os

from flask import Flask, render_template, request, Response, current_app
from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

app = Flask(__name__,template_folder='template')


# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
#UPLOAD_FOLDER = 'C://Users//Ayan//Python_Flask//Instagram_Messaging_app - Copy-2//Instagram_Messaging_app - Copy//static//file'
#UPLOAD_FOLDER = current_app.root_path
#app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/')
def hello1():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def home():
    data = []
    if request.method == "POST":
        message = request.form["details"]
        email = request.form["email"]
        password = request.form["password"]
        print(message,email, password)
        # get the uploaded file
        uploaded_file = request.files['fileupload']
        UPLOAD_FOLDER = current_app.root_path + "/static/file"
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
        # save the file
        return parseCSV(file_path,email,password)


def parseCSV(filePath,email,password):
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath, sep =',', header = 0, names = ['user_name', 'password'])
    print(csvData)
    # Loop through the Rows
    for index, row in csvData.iterrows():
        print(row['user_name'])
        print(row['password'])
    # Return the response object
    return instagram(csvData,email,password)

def instagram(csvData,email,password):
   # service = Service("C:\\Scraping\\chromedriver_win32\\chromedriver_win32\\chromedriver.exe")
    print('ffff')
    for index, row in csvData.iterrows():
      print(row['user_name'])
      print(row['password'])
    service = Service("C:\\Scraping\\1\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://instagram.com")
    time.sleep(getRandomTime())
    driver.find_element(By.XPATH, "//input[@name=\"username\"]") \
        .send_keys(email)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]") \
        .send_keys(password)
    time.sleep(getRandomTime())
    driver.find_element(By.XPATH, '//button[@type="submit"]') \
        .click()
    time.sleep(getRandomTime())
    # Create a response object
    resp = Response("Hello World!")
    return resp

def getRandomTime():
    randTime = randint(8, 10)
    return randTime

if __name__ == "__main__":
    app.run()

