# Enter your code here
camel=input('Insert text in the style of camel case: ')
snake=''
for char in camel:
    if char.isupper():
        snake+='_'+char.lower()
    else:
        snake+=char
print('snake_case:', snake)