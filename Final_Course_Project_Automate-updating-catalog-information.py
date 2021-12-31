"""
Introduction

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 
What you’ll do

    Write a script that summarizes and processes sales data into different categories 

    Generate a PDF using Python

    Automatically send a PDF by email 

    Write a script to check the health status of the system 
"""
"""
#Fetching supplier data
You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).
Here, you'll find two script files download_drive_file.sh and the example_upload.py files. You can view it by using the following command.
=> ls ~/
To download the file from the supplier onto our linux-instance virtual machine we will first grant executable permission to the download_drive_file.sh script.

=> sudo chmod +x ~/download_drive_file.sh
Run the download_drive_file.sh shell script with the following arguments:
=> ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
You have now downloaded a file named supplier-data.tar.gz containing the supplier's data. Let's extract the contents from this file using the following command:
=> tar xf ~/supplier-data.tar.gz
This creates a directory named supplier-data, that contains subdirectories named images and descriptions.
List contents of the supplier-data directory using the following command:
=> ls ~/supplier-data
The subdirectory images contain images of various fruits, while the descriptions subdirectory has text files containing the description of each fruit. You can have a look at any of these text files using cat command.
=> cat ~/supplier-data/descriptions/007.txt
#Working with supplier images
In this section, you will write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
    Size: Change image resolution from 3000x2000 to 600x400 pixel
    Format: Change image format from .TIFF to .JPEG
Create and open the file using nano editor.
=> nano ~/changeImage.py

"""
"""Codes:-"""
#changeImage.py

#!/usr/bin/env python3
import os, sys
from PIL import Image

user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/{}/supplier-data/images/'.format(user)
for image_name in os.listdir(image_directory):
    if not image_name.startswith('.') and 'tiff' in image_name:
        image_path = image_directory + image_name
        path = os.path.splitext(image_path)[0]
        im = Image.open(image_path)
        new_path = '{}.jpeg'.format(path)
        im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")
        
"""
Once you have completed editing the changeImage.py script, save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Grant executable permissions to the changeImage.py script.
=> sudo chmod +x ~/changeImage.py
Now run the changeImage.py script:
=> ./changeImage.py
Now, let's check the specifications of the images you just updated. Open any image using the following command:
=> file ~/supplier-data/images/003.jpeg

#Uploading images to web server
You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [linux-instance-IP-Address]/upload URL.
Copy the external IP address of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".
In the home directory, you'll have a script named example_upload.py to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.
=> cat ~/example_upload.py
In this script, we are going to upload a sample image named icon.sheet.png.
Grant executable permission to the example_upload.py script.
=>sudo chmod +x ~/example_upload.py
Execute the example_upload.py script, which will upload the images.
=> ./example_upload.py
Now check out that the file icon.sheet.png was uploaded to the web server by visiting the URL [linux-instance-IP-Address]/media/images/, followed by clicking on the file name.
#In a similar way, you are going to write a script named supplier_image_upload.py that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog.
Use the nano editor to create a file named supplier_image_upload.py:
=> nano ~/supplier_image_upload.py

"""
        
#supplier_image_upload.py

#!/usr/bin/env python3
import requests, os
# The URL to upload the images
url = "http://localhost/upload/"
# To get the username from environment variable
USER = os.getenv('USER')
# The directory which contains all the images.
image_directory = '/home/{}/supplier-data/images/'.format(USER)
# Listing all the files in images directory
files = os.listdir(image_directory)
# Parsing through all the images
for image_name in files:
    # Accepting files that has jpeg extension and ignoring hidden files
    if not image_name.startswith('.') and 'jpeg' in image_name:
        # creating absolute path for each image
        image_path = image_directory + image_name
        # uploading jpeg files
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

"""
Once you have completed editing the supplier_image_upload.py script, save the file by typing Ctrl-o, Enter key, and Ctrl-x.
Grant executable permission to the supplier_image_upload.py script.
=> sudo chmod +x ~/supplier_image_upload.py
Run the supplier_image_upload.py script.
=> ./supplier_image_upload.py
Refresh the URL opened earlier, and now you should find all the images uploaded successfully.

#Uploading the descriptions
The Django server is already set up to show the fruit catalog for your company. You can visit the main website by entering linux-instance-IP-Address in the URL bar or by removing /media/images from the existing URL opened earlier. The interface looks like this:
Check out the Django REST framework, by navigating to linux-instance-IP-Address/fruits in your browser.
Currently, there are no products in the fruit catalog web-server. You can create a test fruit entry by entering the following into the content field:
{"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}
After entering the above data into the content field click on the POST button. Now visit the main page of your website (by going to http://[linux-instance-external-IP]/), and the new test fruit you uploaded appears.
To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the fruit images and their respective description in JSON format.
Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.
Create run.py using the nano editor:
=> nano ~/run.py

"""
#run.py

#!/usr/bin/env python3

import os, requests, json

def catalog_data(url,description_dir):
    """This function will return a list of dictionaries with all the details like name, weight, description, image_name.
    It will change the weight to integer format.
    """
    fruit={}
    for item in os.listdir(description_dir):
      fruit.clear()
      filename=os.path.join(description_dir,item)
      with open(filename) as f:
        line=f.readlines()
        description=""
        for i in range(2,len(line)):
          description=description+line[i].strip('\n').replace(u'\xa0',u'')
        fruit["description"]=description
        fruit["weight"]=int(line[1].strip('\n').strip('lbs'))
        fruit["name"]=line[0].strip('\n')
        fruit["image_name"]=(item.strip('.txt'))+'.jpeg'
        print(fruit)
        if url!="":
          response=requests.post(url, json=fruit)
          print(response.request.url)
          print(response.status_code)
    return 0

if __name__=='__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    catalog_data(url,description_directory)

    """
    Once you complete editing run.py script, save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Grant executable permission to the run.py script.
=> sudo chmod +x ~/run.py
Run the run.py script:
=> ./run.py
Now go to the main page of your website (by going to http://[linux-instance-IP-Address]/) and check out how the new fruits appear.
#Generate a PDF report and send it through email
Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library.
Script to generate a PDF report
Create a script reports.py to generate PDF report to supplier using the nano editor:
=> nano ~/reports.py

    """
#reports.py

#!/usr/bin/env python3

from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])
    
"""
Using the reportlab Python library, define the method generate_report to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf.
Once you have finished editing the script reports.py, save the file by typing Ctrl-o, Enter key, and Ctrl-x.
#Create another script named report_email.py to process supplier fruit description data from supplier-data/descriptions directory. Use the following command to create report_email.py.
=> nano ~/report_email.py

"""
#report_email.py

#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email


def pdf_body(input_for,desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    res = []
    wt = []
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as f:
        line=f.readlines()
        weight=line[1].strip('\n')
        name=line[0].strip('\n')
        print(name,weight)
        res.append('name: ' +name)
        wt.append('weight: ' +weight)
        print(res)
        print(wt)
    new_obj = ""  # initializing the object
    # Calling values from two lists one by one.
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)  # The directory which contains all the files with data in it.
    current_date = datetime.date.today().strftime("%B %d, %Y")  # Creating data in format "May 5, 2020"
    title = 'Processed Update on ' + str(current_date)  # Title for the PDF file with the created date
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))  # calling the report function from custom module
    email_subject = 'Upload Completed - Online Fruit Store'  # subject line give in assignment for email
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
    msg = generate_email("automation@example.com", "<username>@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")  # structuring email and attaching the file. Then sending the email, using the cus$
    send_email(msg)

    """
    Once you have completed the report_email.py script. Save the file by typing Ctrl-o, Enter key, and Ctrl-x.
    
    Send report through email
Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.
Create emails.py using the nano editor using the following command:
=> nano ~/emails.py

   """
#emails.py

#!/usr/bin/env python3

import email
import mimetypes
import smtplib
import os


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Making attachment_path optional, if the attachment variable is empty string, no email will be sent.
    if not attachment_path == "":
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                                   filename=attachment_filename)

    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
"""
Once you have finished editing the report_email.py script, save the file by typing Ctrl-o, Enter key, and Ctrl-x.
Grant executable permissions to the script report_email.py.
=> sudo chmod +x ~/report_email.py
Run the report_email.py script.
=> ./report_email.py
Now, check the webmail by visiting [linux-instance-external-IP]/webmail. Here, you'll need a login to roundcube using the username and password mentioned in the Connection Details Panel on the left hand side, followed by clicking Login.
Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.

"""    
"""
#Health check
This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:
    Report an error if CPU usage is over 80%
    Report an error if available disk space is lower than 20%
    Report an error if available memory is less than 500MB
    Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
Create a python script named health_check.py using the nano editor:
=> nano ~/health_check.py

"""
#health_check.py

#! /usr/bin/env python3

import socket
import shutil
import psutil
import emails


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_memory_usage():
    """Verifies that there's enough free space on disk"""
    available_memory = psutil.virtual_memory().available
    total = available_memory/(1024*1024)
    return total > 500

def check_localhost():
    """check localhost is correctly configured on 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def send_email(subject):
    email = emails.generate_email("automation@example.com", "student-00-ac02b5a$
                                  subject,
                                  "please check your system and resolve the issue as soon as possible." "")
    emails.send_email(email)

# If there's not enough disk, or not enough CPU, print an error
if not check_cpu_usage():
    subject = "ERROR - CPU usage is over 80%"
    print(subject)
    send_email(subject)

if not check_disk_usage('/'):
    subject = "ERROR - Available disk space is less than 20%"
    print(subject)
    send_email(subject)

if not check_memory_usage():
    subject = "ERROR - Available memory is less than 500MB"
    print(subject)
if not check_localhost():
    subject = "ERROR - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    send_email(subject)

"""
Once you have completed the health_check.py script. Save the file by typing Ctrl-o, Enter key, and Ctrl-x.
Grant executable permissions to the script health_check.py.
=> sudo chmod +x ~/health_check.py
Run the file.
=> ./health_check.py
Next, go to the webmail inbox and refresh it. There should only be an email something goes wrong, so hopefully you don't see a new email.
To test out your script, you can install the stress tool.
=> sudo apt install stress
Next, call the tool using a good number of CPUs to fully load our CPU resources:
=> stress --cpu 8
Allow the stress test to run, as it will maximize our CPU utilization. Now run health_check.py by opening another SSH connection to the linux-instance. Navigate to Accessing the virtual machine on the navigation pane on the right-hand side to open another connection to the instance.
Now run the script:
=> ./health_check.py
Close the stress --cpu command by clicking Ctrl-c.
Now, you will be setting a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user.
To set a user cron job use the following command:
=> crontab -e
Enter 1 to open in the nano editor. Now, set the complete path for health_check.py script, and save by clicking Ctrl-o, Enter key, and Ctrl-x.
Congratulations!
Congrats! You've successfully created a python script that processes images and descriptions and then updates your company's online website to add the new products. You have also generated a PDF report and sent it by email. Finally, you have also set up monitoring of the system's health.
"""
