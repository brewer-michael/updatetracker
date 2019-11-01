#updatetracker.py
import bs4, requests, smtplib, difflib

#Dowload page - add URL of the desired page
getPage = requests.get('')
#getPage = raise_for_status() #if error it will stop the script

#Parse text
ticketInfo = bs4.BeautifulSoup(getPage.text, 'html.parser')
tickets = ticketInfo.select('.somediv') #div from html website

# first time run
# create folder called data in your project directory
# uncomment the lines below
# run docker container with - "docker run -v ~dropbox/docker-python/data:/data {image}"
#with open("/data/currenttext.txt","w+") as text_file:
 #   text_file.write(str(tickets).replace('\n',''))

# check for differences on the page

#Assuming you will use Gmail SMTP server, directions on obtaining appKey are here: https://support.google.com/mail/answer/185833?hl=en
appKey = ''
fromAddress = ''
#can be set to multiple recipient addresses ["","",""]
toAddress = ['']

# Read stored file and compare it to the current text
with open('currenttext.txt','r') as file:
    original = str(file.read().replace('\n', ''))
    newText = str(tickets).replace('\n','')
    if original != newText:
        conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
        conn.ehlo() # call this to start the connection
        conn.starttls() # starts tls encryption. When we send our password it will encrypt
        conn.login(fromAddress, appKey)
        conn.sendmail(fromAddress, toAddress, '')
        conn.quit()
        print('Sent notification')
        for i in range(len(toAddress)):
            print(toAddress[i])
        print('')
        print (str(newText))
    else: 
        print ('no changes')

    

