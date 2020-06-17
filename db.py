import sqlite3
import sched
import time
import datetime
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'bataysk55@gmail.com'
PASSWORD = 'Snoopdoggjimcarrey1999'


while True:                                                                         # sql.execute("""CREATE TABLE reports (
    s = sched.scheduler(time.time, time.sleep)                                      #     date BIGINT,
    db = sqlite3.connect('db.sqlite3')                                              #     number BIGINT
    sql = db.cursor()                                                               # )""")
    data = []                                                                       # db.commit()


    def report():
        # sql.execute("DELETE FROM reports WHERE number = 1")
        # db.commit()
        today = datetime.datetime.now()
        number = 1                                                                  # sql.execute("SELECT date FROM reports")
        sql.execute("INSERT INTO reports VALUES (?, ?)", (today, number))           # if sql.fetchone():
        db.commit()                                                                 # sql.execute("DELETE FROM reports WHERE number = 1")
        for value in sql.execute("SELECT * FROM reports"):                         # db.commit()
            data.append(value)
        with open("report_db.txt", mode="a+", encoding="utf-8") as text:
            text.write(f"{str(data[-1])}\n")


    def get_contacts(filename):
        """
        Return two lists names, emails containing names and email addresses
        read from a file specified by filename.
        """

        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])
        return names, emails


    def read_template(filename):
        """
        Returns a Template object comprising the contents of the
        file specified by filename.
        """

        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)


    def main():
        names, emails = get_contacts('mycontacts.txt')  # read contacts
        message_template = read_template('report_db.txt')

        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()  # create a message

            # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name.title())

            # Prints out the message body for our sake
            print(message)

            # setup the parameters of the message
            msg['From'] = MY_ADDRESS
            msg['To'] = email
            msg['Subject'] = "This is TEST"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            s.send_message(msg)
            del msg

        # Terminate the SMTP session and close the connection
        s.quit()


    # if __name__ == '__main__':
    s.enter(10, 1, report)
    s.enter(20, 1, main)
    s.run()

    if time.time() == 1:
        break




