# TwilioWhatsapp
Exploring whatsapp message automation using Twilio API with Python

Set up your account on Twilio.

All products and services -> Programmable SMS -> Programmable Whatsapp (Beta)

Save the number displayed on the page, and send the unique text (in bold) on that number via Whatsapp to get your number verified.

Next, 

pip install twilio

Now, go to your console page on twilio.com and copy ACCOUNT SID and AUTH TOKEN into environment variables as 'TWILIO_ACCOUNT_SID' and 'TWILIO_AUTH_TOKEN'.

Similarly, save your whatsapp number under 'MY_WHATSAPP' in the environment variables. This promotes privacy of your phone number.

Now, you're good to go. Run the python file: 

python whatsapp.py 

Edit the code to get custom messages. 

This was the first experiment, I'll try to make a broadcast via Whatsapp as well.
