"""Component 2 (How much) v2
use try/accept and pull error message out of the loop
"""


error = "Please enter a whole number between 1 and 10\n"
valid = False

# Keep asking untill a valid amount )1-10) is entered
while not valid:
    try:
        # ask for amount

