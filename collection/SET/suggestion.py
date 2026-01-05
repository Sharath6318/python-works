all_user = {"sachin", "dravid", "laxman","ganguly" "sreenath", "zaheer", "dhoni", "yuvi", "kaif"}

sachin_friends = {"dravid","laxman", "ganguly" }


suggestion = all_user.difference(sachin_friends)

suggestion.remove("sachin")

print(suggestion)