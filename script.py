import smtplib
from email.mime.text import MIMEText # Class that represent the text of the email
from email.mime.multipart import MIMEMultipart # Class taht represents the email message
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    #Email Details
    sender_email = os.getenv("SENDER_EMAIL")
    sender_pass = os.getenv("SENDER_PASS")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    #Email Message
    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body= f"Hi, the workflow {workflow_name} failed for the repository {repo_name}. Please check the logs for more details. \nMore Details: \nRun_ID: {workflow_run_id}"
    
    #Making the MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_pass)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        print('Email sent successfully!')
        
    except Exception as e:
        print(f"Error: {e}")
        
send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))
