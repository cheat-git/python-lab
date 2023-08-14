import re
p1=r'[aeiouAEIOU]'
p2=r'[bcdfghjklmnpqrstuvwxyzBCDFGHJKLMNPQRSTUVWXYZ]'
p3=r'[0-9]'
a=input("Enter the string:")
print(f"Vowels:{len(re.findall(p1,a))}")
print(f"Consonants:{len(re.findall(p2,a))}")
print(f"Digits:{len(re.findall(p3,a))}")

