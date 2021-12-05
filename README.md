# DealingWithSpammers
I use Outlook daily to check my multiple emails account. The problem with the built in system that should protect you from spam is that is smart until a certain point.
I have a common name in south Italy so I suppose that maybe it's my namesake's fault (I refuse to believe that I was so dum to give my mail away to those people lol).
Basically I receive every two or three day irritating and obviously fake email. Like "take your amazon free gift card" and similar.
The problem here is receiving a mail every time from a sender that is a little different from every other. The problem is that you can block only a specific account, you can't like "block an account that goes like this". Because I could clearly see a recurring pattern in the sender name so thanks to regex you can easily deal with that.
That's said I wrote my own solution to this problem:
a Python script that look for new unwanted mail in your box and send back to the sender a mail every second for a while...

## Setup
To run this project you need your third party app password for your account, you can add it with you account's name in ReadMail.py and SendMail.py.
Download the repo and run the following (you need Python installed)

```
$ py ReadMailv3.py
$ py Regex.py
$ py SendMail.py
```
Yes at the moment are three different script to run. In fact, here the to do list.

## To do:
The project is still in an early phase.
Here's few point:
* Automate the process. Like check every 3 hours. It is more 
* Having a single main script

Actually for me worked after two session of revenge. It's a week now that I don't receive any. So yeah, I'm happy with it.
	
