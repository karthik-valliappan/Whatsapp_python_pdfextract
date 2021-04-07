import requests
import json
import base64
import re
import pdfplumber
import pywhatkit
import datetime
import glob

####### filter latest downloaded file from the directory ##########

list_of_files = glob.glob('/Users/karthik/Downloads/*.pdf')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

### filter can be done in other ways by sorting method #####


# folder = "/Users/karthik/Downloads/"
# files_path = os.path.join(folder, '*.pdf')
# files = sorted(
#     glob.iglob(files_path), key=os.path.getctime, reverse=True)
# print(files[0])


####### Using the latest pdf file extracting the customer number #######

with pdfplumber.open(latest_file) as pdf:
    first_page = pdf.pages[0]
    content=first_page.extract_text()

PATTERN= r'\d\d\d\d\d\d\d\d\d\d'
all_no=re.findall(PATTERN, content)
customer_no= all_no[1]
print(customer_no)

##### Uploading file to wordpress media ######

user = 'pythonapp' #Application app name from wordpress site
pythonapp = '**** **** **** **** **** ****' #Application password from wordpress site.
url = 'https://URLofyourdomain/wp-json/wp/v2'
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}
media = {'file': open('test.pdf','rb')}
pdf = requests.post(url + '/media', headers=headers, files=media)
link = json.loads(pdf.content.decode('utf-8'))
postid =json.loads(pdf.content.decode('utf-8'))
mediaUrl = link.get('guid').get('rendered')
print(link.get('guid').get('rendered'))


######### time and pywhatkit module ############
### pywhatkit uses whatsapp web app to send . It require sometime to open whatsapp web. Get the current time and print 2 mins later time. ######
### two minutes later time used as a import for pywhatkit sendmessage function #######

def currentTime():
  print("Current date and time : ")
  today = datetime.datetime.strftime(datetime.datetime.today() , '%Hh/%Mm')
  print(today)

minutesLater = datetime.datetime.today() + datetime.timedelta(minutes = 2)
print("")
currentTime()
print("Time after 2 minutes : ")
print(datetime.datetime.strftime(minutesLater , '%Hh/%Mm'))

hour = int(datetime.datetime.strftime(minutesLater,'%H'))
mins = int(datetime.datetime.strftime(minutesLater,'%M'))

## Print command to verify hour and mins 
print(hour)
print(mins)


message = 'Dear Parents, Please download the fees receipt by clicking the link.'
url = mediaUrl
end_message = 'Thanks, Academy Name'

full_message = message + '\n' + url + '\n' + end_message

## Print full message to test
print(full_message)

pywhatkit.sendwhatmsg(customer_no,full_message,hour,mins)





