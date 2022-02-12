import collections

# Input the guests 
input_guest = input("Enter the guests you'd like to invite to dinner separated by a comma: ")
DinnerGuests = (input_guest.split(","))

for guest in DinnerGuests:
    if (len(guest) > 10):
        print(guest," goes on a BIG ID tag")
    else:
        print(guest," goes on a SMALL ID tag")

# Input the date the guests were invited
input_date = input("In the same order you inputted the guests, please input the date they were invited separated by a comma: ")
DinnerDates = input_date.split(",")

#Print names and dates and size of ID card
for i in range(len(DinnerGuests)):
    print(DinnerGuests[i] + '\t ' + DinnerDates[i])
