# Text Extract from PDF and Automate WhatsApp Message
Extracting contact number from PDF and sending WhatsApp message to the extracted number using python. 

# Use Case

User Download the fees receipt from the application and the application doesn't have the capabilities to send WhatsApp messages. Tried to automate the message sending process through Python. Steps involved

1. Download fees receipt from website.
2. Using the windows automation tool triggers the python code when the new file downloaded into the windows directory.
3. Python Code read the pdf and get the customer number.
4. Same code uploads the pdf file to WordPress media using WordPress API and gets the link to download the pdf file.
5. Same code uses the customer number and pdf downloadable link as input for the WhatsApp python library send messages function.

## Wordpress API:

Refer Generating Manually section from the below link to generate application password for the user.

https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/ 

## Monitor your file system

Python Watchdog library help to monitor the file system to detect on new file created or modified. If new files is created it will trigger the whatsapp.py file.


## Libraries


```bash
pywhatkit
datetime
requests
pdfplumber
watchdog
```

## Reason to use this Method

When small businesses can't afford WhatsApp business API can use this method to automate the message sending process.

## Cons

WhatsApp python library uses WhatsApp web to send messages and it consumes time.
Cant be used as a WhatsApp chatbot


## License
[MIT](https://choosealicense.com/licenses/mit/)
