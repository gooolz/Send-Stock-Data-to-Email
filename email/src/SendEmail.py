"""Julia Foote
    This program takes the user input file name for the list of stock symbols and opens an smtp
    email process that takes the stock symbols and parses 5 of them per each yahoo finance call
    and puts these symbols into the getQuotes.py function getQuotes.print_stock_info() which returns
     the output of the raw stock data and puts this into the body of the email. It also takes the
     list of stock symbol data and pulls them into the function getQuotes.process_quotes() and
     returns an xml layout of the stock data and puts this in an attachment on the email."""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import my_pass
import sys
import getQuotes
import datetime



def SendEmailMsgWithAttachment(fromuser, tolist, subject, message,
                               attachmentfilename="No Filename.xml",
                               attachmentContent="No Content"):

    msg = MIMEMultipart()
    msg.attach(MIMEText(message))

    msg['From'] = fromuser
    msg['To'] = ', '.join(tolist)
    msg['Subject'] = subject

    attachment = MIMEText(open(attachmentfilename, "r").read())
    attachment.add_header('Content-Disposition', 'attachment', filename=attachmentfilename+".txt")
    msg.attach(attachment)

    smtpObj = smtplib.SMTP('smtp.office365.com', 587)
    smtpObj.starttls()
    smtpObj.login("battsj1@spu.edu", my_pass.smtp_pass())
    smtpObj.sendmail(fromuser, tolist, msg.as_string())
    smtpObj.quit()

    return

def SendEmailMsgWithAttachmentFilename(fromuser, tolist, subject, message, attachmentfilename):
    SendEmailMsgWithAttachment(fromuser, tolist, subject, message,
                               attachmentfilename,
                               open(attachmentfilename, "r").read())
    return


if __name__ == "__main__":
    # grabs the filename input from the user which holds the list of stock symbols
    sym = input("Enter filename of stock symbols: ")
    # writes the raw stock data to a new file called 'rawdata.txt' and then the data is
    # put into the body of the email
    symb_file = open("rawdata.txt", "w")
    with open(sym, "r") as file:
        array = []
        for line in file:
            array.append(line)
            j = 0
            k = 0
            while j < len(line):
                j += 1
                k += 1
                sys.stdout = symb_file
                getQuotes.print_stock_info('&s=' + line)
                while (j < len(line)) & (k < 5):
                    j += 1
                    k += 1
    symb_file.close()
    # gets the datetime and attaches it to the beginning of the
    # xml file name
    dt = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    newname = dt + ' stockquotes.xml'
    # writes the xml style stock data into the new file called 'stock_file' and then
    # the output is put into an attachment on the email
    stock_file = open(newname, "w")
    with open(sym, "r") as file:
        array = []
        for line in file:
            array.append(line)
            j = 0
            k = 0
            while j < len(line):
                j += 1
                k += 1
                sys.stdout = stock_file
                getQuotes.process_quotes('&s=' + line)
                while (j < len(line)) & (k < 5):
                    j += 1
                    k += 1
    stock_file.close()
    # sends the email with attachment from myself to myself with the
    # raw stck data and the xml style data
    file_raw = open("rawdata.txt", "r")
    SendEmailMsgWithAttachmentFilename('battsj1@spu.edu',
                                       ['battsj1@spu.edu'],
                                       'CSC4800 XML Stock Quotes - Julia Foote',
                                       file_raw.read(),
                                       (dt + ' stockquotes.xml'))

    file.close()

