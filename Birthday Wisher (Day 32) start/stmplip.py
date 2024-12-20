# import smtplib
# import random
# import datetime as dt

# MY_EMAIL = "chasmhearts@gmail.com"
# PASSWORD = "ovxmjfwquurglake"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 3:
#     with open ("D:\\Project\\Angela yu\\Email SMTP\\Birthday Wisher (Day 32) start\\quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)

    # with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL,PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg=f"Subject: Monday quotes \n\n{quote}"
    #     )






# my_email = "chasmhearts@gmail.com"
# password = "ovxmjfwquurglake"


# with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection: # Increased timeout
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="walterwhite8979@gmail.com", msg="Subject:Hello\n\n Vanakam da mapla")


# import datetime as dt

# now = dt.datetime.now()

# months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# current_month = now.month 
# output = months[current_month]  

# print(f"current month: {output}")

