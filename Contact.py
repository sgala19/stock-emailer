from datetime import date
import yagmail
import stockquotes

# create dummy gmail account and password
# can store password in yagmail keyring for more security
yag = yagmail.SMTP('INSERT_GMAIL', 'INSERT_GMAIL_PASSWORD')


class Contact:
    def __init__(self, name, stocks, email):
        self.name = name
        self.stocks = stocks
        self.email = email

    # add stocks to existing list of stocks
    def add_stocks(self, *ticker_names):
        for ticker_name in ticker_names:
            self.stocks.append(ticker_name)

    def change_name(self, name):
        self.name = name

    def reset_stocks(self):
        self.stocks = []

    # helper function to create and format the string used in email
    def create_string(self):
        contents = ""
        for ticker in self.stocks:
            stock = stockquotes.Stock(ticker)
            contents += ticker + " : " + str(stock.current_price) + "\n"
        return contents

    # function that sends emails using instance object names
    def send_email(self):
        email = self.create_string()
        today = date.today()
        yag.send(self.email, self.name + " " + today.strftime("%b-%d-%Y"), email)
