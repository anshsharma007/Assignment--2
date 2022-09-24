from datetime import datetime
date = datetime.today()
print(date)
d1 = date.strftime("%d- %m- %Y %I: %m %p") #capital y print the whole year like 2022 insted of 22
print(d1)
d1 = date.strftime("%d-%m-%y") #small y print the short form of the year like 22 instead of 2022
print(d1)

#Capital i use for the hours in 12 hours format and capital h prints in 24 hours format
# p is used for am and pm
d1 = date.strftime("%B-%d-%y") #capital b used for print month and in full form
print(d1)
d1 = date.strftime("%d/%b/%Y") #small p is used for printing month in short form
print(d1)