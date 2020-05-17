# Python Messaging App with Twilio's REST API
---------------------------------------------
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Project Summary
A barebones app project for sending messages in Python using Twilio API.

## About The Project
The python app lets you send SMS to a regisatered Twilio number (As the account you will test it on is a trial account). Have fun sending weird messages to
yoursef or your spouse through python XD.

## How To Run The App

***With a free Twilio account, you only get to text verified numbers.***
#### 1. Get a Github  profile.
#### 2. Star this project ;)!
#### 3. Create an account on [Twilio](http://twilio.com).
#### 4. Verify a Phone Number on Twilio https://www.twilio.com/console/phone-numbers/verified. That you would like to text.
#### 5. Get Twilio Credentials
- [ ] https://www.twilio.com/console 
- [ ] Get Account SID
- [ ] Get Auth Token
#### 6. Get Phone Numbers
- [ ] [Your Twilio Number is Here](https://www.twilio.com/console/phone-numbers/incoming)
- [ ] [Verified Cell Phone Number You Want To Text](https://www.twilio.com/console/phone-numbers/verified)
#### 7. Get Message Service SID
- [ ] [Create New Messaging Service](https://www.twilio.com/console/sms/services/) 
- [ ] Select 'Mixed'
- [ ] Select 'Numbers' on the left side of dashboard and then 'Add an Existing Number' to add the Twilio number you created.
- [ ] Go to 'Settings' and hit 'Save'.
#### 7. Put your twilio credentials, service message SID and Twilio phone numbers in `credentials.py`
#### 8. Clone this repository on your desktop.
#### 9. Open your terminal and `pip install twilio`.
#### 10. Open `send_sms.py` in **IDLE** and Run it!
#### Or if you want to be cool on your mac...
On Your Mac hit <kbd>CMD</kbd>+<kbd>SPACE</kbd> and type **Terminal**.
Then type in the following command:
```
python Desktop/CP-Twilio-Python-Text-App/send_sms.py
```
### Congratulations!
- [X] Using Twilio's REST API, you sent your first text in your own Pyhon Messaging app.

## Tech Stack
* Python
* Atom Text Editor
* Bash Terminal
* Twilio Free Trial Account

## Contributing
Fee free to add suggestions!

## License
The contents of this repository is licensed under a [MIT License](https://opensource.org/licenses/MIT)