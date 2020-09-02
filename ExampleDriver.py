from Contact import Contact

# example driver class to show how to use various functions

# initialize Contact object with name, email, and list of stocks
test_contact = Contact("insert_name", ["TSLA", "AAPL", "AMZN", "FB", "GOOG", "MSFT"], "INSERT_EMAIL")
test_contact.send_email()

# update Contact with new name and new list of stocks
test_contact.change_name("new_name")
test_contact.reset_stocks()
test_contact.add_stocks("^GSPC", "^IXIC", "^DJI")
test_contact.send_email()
