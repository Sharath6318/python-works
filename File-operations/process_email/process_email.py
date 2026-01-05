file_path = "PYTHON-WORKS\\File-operations\\process_email\\email.txt"

gamil_path = "PYTHON-WORKS\\File-operations\\process_email\\gmail.txt"

yohoo_path = "PYTHON-WORKS\\File-operations\\process_email\\yohoo.txt"

outlook_path = "PYTHON-WORKS\\File-operations\\process_email\\outlook.txt"




fr = open(file_path, "r")

fw_gamil = open(gamil_path, "w")

fw_yohoo = open(yohoo_path, "w")

fw_outlook = open(outlook_path, "w")



for email in fr:

    email = email.rstrip("\n")

    if email.endswith("gmail.com"):

        fw_gamil.write(email + "\n")

    elif email.endswith("yahoo.com"):

        fw_yohoo.write(email + "\n")

    elif email.endswith("outlook.com"):

        fw_outlook.write(email + "\n")






