
    
name = str(input('Enter the string:'))  #yahya parayil
print('The entered string is : ',name)
reversed_text = ""

for char in name:
    reversed_text = char + reversed_text

print(f"Reversed string: {reversed_text}")

if reversed_text == name :
    print('they are palindrome')
else:
    print('they are not palindrome')