passwd={'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}
print(passwd.items())
print(passwd.keys())
print(passwd.values())
k=input("Enter User:")
if k in passwd.keys():
    print("The password is:",passwd[k])
    a=input("Enter New Password:")
    passwd[k]=a
    print("Updated!!")
