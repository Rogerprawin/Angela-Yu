import pandas, datetime, random
import smtplib

MY_EMAIL = "chasmhearts@gmail.com"
PASSWORD = "ovxmjfwquurglake"

today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("D:\\Project\\Angela yu\\Email SMTP\\Birthday Wisher (Day 32) start\\birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
print(data)
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"D:\\Project\\Angela yu\\Email SMTP\\Birthday Wisher (Day 32) start\\letter\\letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        contents = contents.replace("Angela", "Roger")
    
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],  
            msg=f"Subject: Birthday Reminder  \n\n{contents}"
        )

 # upload in cloud(python anywhere) to schedule the mail repeating process every year