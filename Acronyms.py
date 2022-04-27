input = str(input("Enter a phrase: "))
text = input.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)