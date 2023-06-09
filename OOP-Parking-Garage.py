"""
Consider the following methods/ideas when constructing your garage: (these are suggestions to get you started, if you have other ideas that is totally cool and we love to see it!)

take_ticket
This should decrease the amount of tickets available by 1
This should decrease the amount of parkingSpaces available by 1
pay_for_parking
Display an input that waits for an amount from the user and store it in a variable
If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
This should update the "current_ticket" dictionary key "paid" to True -leave_garage
If the ticket has been paid, display a message of "Thank You, have a nice day"
If the ticket has not been paid, display an input prompt for payment
Once paid, display message "Thank you, have a nice day!"
Update parking_spaces list to increase by 1 (meaning add to the parking_spaces list)
Update tickets list to increase by 1 (meaning add to the tickets list)
"""

class Garage(object):
    def __init__(self):
        