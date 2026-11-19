from datetime import date
event = input("what is the event title?:")
event_year = int(input("what year does the event take place?:"))
event_month = int(input("what month number (1-12) does the event take place?"))
event_day = int(input("What day (1-31) does the event take place on?:"))
#formats the data
event = event .strip() .title()
event_date = date(event_year, event_month, event_day)
#prints the results
print("Name of the Event:", event)
print("The Date of the Event:", event_date.strftime("%B %d, %Y"))
print("On the year of:", event_year)
print("the day of:", event_day)
print("the month of:", event_date.strftime("%B"))
print("what day will it be on?", event_date.strftime("%A"))