import pyffx

#Copyright Rajath Shetty 
  
#enter the 'e = pyffx.String(b'secret-key', alphabet='abc', length=6)' here

##################################
"""Encryption Function"""
##################################

def encrypt(test):
    to_list = list(test) #Sends each character of the string to a list(array)
    list2 = []
    for i in to_list:
        if i.isalnum():

            encrypted = e.encrypt(i)
            list2.append(encrypted)
            
        else:
            list2.append(i)

    encrypted_string = ''.join(list2)
    print(encrypted_string)

##################################
"""Decryption Function"""
##################################


def decrypt(test):
    to_list = list(test) #Sends each character of the string to a list(array)
    list2 = []
    for i in to_list:
        if i.isalnum():
            decrypted = e.decrypt(i)
            list2.append(decrypted)
            # Send each alphanumeric character to encryption from here
        else:
            list2.append(i)

    encrypted_string = ''.join(list2) #
    print(encrypted_string)


encrypt('PASS INPUT VALUE HERE')
decrypt('PASS ENCRYPTED INPUT VALUE HERE')
