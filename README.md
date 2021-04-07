# Text Extract from PDF and Automate WhatsApp Message
Extracting PDF text and uploading it to wordpress and sending whatsapp message to the user using python

# Use Case

User Download the fees receipt from the application and the application doesn't have the capabilities to send WhatsApp messages. Tried to automate the message sending process through Python. Steps involved

1. Download fees receipt from website.
2. Using the windows automation tool triggers the python code when the new file downloaded into the windows directory.
3. Python Code read the pdf and get the customer number.
4. Same code uploads the pdf file to WordPress media using WordPress API and gets the link to download the pdf file.
5. Same code uses the customer number and pdf downloadable link as input for the WhatsApp python library send messages function.

## Cons

WhatsApp python library uses WhatsApp web to send messages and it consumes time.

## Required Libraries


```bash
pywhatkit
datetime
requests
pdfplumber
```

## Reason to use this Method

When small businesses can't afford WhatsApp business API can use this method to automate the message sending process.


## License
[MIT](https://choosealicense.com/licenses/mit/)
