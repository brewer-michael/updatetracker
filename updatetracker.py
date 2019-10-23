import bs4, requests, smtplib

#Dowload page
getPage = requests.get('')
getPage = raise_for_status() #if error it will stop the script

#Parse text
ticketInfo = bs4.BeautifulSoup(getPage.text, 'html.parser')
tickets = ticketInfo.select('.somediv') #div from html website