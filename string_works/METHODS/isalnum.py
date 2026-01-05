#check only num and character are include

text = "python123"
text_1 = "python 123"
text_2 = "python&123"

print(text.isalnum())
print(text_1.isalnum())
print(text_2.isalnum())