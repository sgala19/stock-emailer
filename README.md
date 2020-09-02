# Stock Emailer
Simple class that can be used to email current share prices of a list of stocks utilizing two packages (yagmail and stockquotes).

## Contact Class
Defines a Contact object which will store information about the recipient such as their name, stocks, and email.  
Contains functions to update their information and send email.

## Important Notes
A user must create a dummy gmail from which to send the prices.  The user can also set up a keyring in order to not have this dummy account password remain visible within the code.  
When creating a dummy email, one must allow access for less secure apps in order to utilize the yagmail package.
