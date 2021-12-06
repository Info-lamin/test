from flask import Flask, render_template, request, redirect, send_from_directory
import os
from email.message import Message
import smtplib

app = Flask(__name__)


def mail(from_address, to_address, password, subject, message, priority):   #it send the mail,  only gmails without two factor authentication are supported
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        m = Message()
        m['From'] = from_address
        m['To'] = to_address
        m['X-Priority'] = str(priority)
        m['Subject'] = subject
        m.set_payload(message)
        smtp.login(from_address, password)
        smtp.sendmail(from_address, to_address, m.as_string())
    return None


@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'),'test.html')


@app.route('/api/api_key')
def api_key():
    mail('mail.orderbywhatsapp@gmail.com', 'laminkutty@gmail.com', 'eqeonnmmthttrhka', 'Mail From Cron', 'the test mail from cron is working fine.', 2)
    return ''


@app.route('/upi', methods=['GET', 'POST'])
def upi():
    return """
    <form onsubmit='myfun()'>
    <input type='text' id='text'>
    <input type='submit'>
    </form>
    <script>
    function myfun(){
        window.location = document.getElementById('text').value
        return false
    }
    </script>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
