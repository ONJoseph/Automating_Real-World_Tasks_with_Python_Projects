"""
Introduction

You’re working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company’s website. To do this, you’ll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company’s website (currently using Django).
What you’ll do

    Use the Python OS module to process a directory of text files 

    Manage information stored in Python dictionaries

    Use the Python requests module to upload content to a running Web service

    Understand basic operations for Python requests like GET and POST methods 
    """
"""
Web server corpweb
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. A Web framework is a set of components that provide a standard way to develop websites quickly and easily.
For this lab, a Django web server corpweb is already configured under /projects/corpweb directory. You can check it out by visiting the external IP address of the corpweb VM. The external IP address can be found in the connection details panel. Enter the corpweb external IP address in a new separate browser tab.
corpweb external IP Address: 34.121.197.24
Output: No feedback
You'll see that there's currently no feedback.
Now, append /feedback to the external IP address of corpweb VM opened in the browser tab.
This is a web interface for a REST end-point. Through this end-point, you can enter feedback that can be displayed on the company's website. You can use this end-point in the example below. Start by copying and pasting the following JSON to the Content field on the website, and click POST.
{"title": "Experienced salespeople", "name": "Alex H.", "date": "2020-02-02", "feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}
Now, go back to the main page by removing the /feedback from the URL. You can see that the feedback that you just entered is displayed on the webpage.

Process text files and upload to running web server

In this section, you'll write a Python script that will upload the feedback automatically without having to turn it into a dictionary.

Navigate to /data/feedback directory, where you'll find a few .txt files with customer reviews for the company.
~cd /data/feedback
~ls
Use the cat command to view these files. For example:
~cat 007.txt
They're all written in the same format (i.e. title, name, date, and feedback).

Here comes the challenge section of the lab, where you'll write a Python script that uploads all the feedback stored in this folder to the company's website, without having to turn it into a dictionary one by one.

Now, navigate back to the home directory and create a Python script named run.py using the following command:
*cd ~
~nano run.py

#Python script
"""
#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://34.121.197.24/feedback/",
    json=fb)
print(response.request.body)
print(response.status_code)
"""
Save the run.py script file by pressing Ctrl-o, the Enter key, and Ctrl-x.

Grant executable permission to the run.py script.
~chmod +x ~/run.py
Now, run the run.py script:
~./run.py
Your POST requests should have successfully uploaded the feedback on the company's website. Now, visit the website again using the corpweb external IP address or just refresh the page if already opened, and you should be able to see the feedback.
"""
