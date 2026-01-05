
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com", "b@yahoo.com"]

new_sec = set()
duplicate_id = set()

unique_email = []

for mail_id in emails:

    if(mail_id in new_sec):

        duplicate_id.add(mail_id)

        unique_email.append(new_sec.difference(duplicate_id))

    else:

        new_sec.add(mail_id)

print(f"unique mail id :  {unique_email}")

print(f"duplicate mail id  : {duplicate_id}")