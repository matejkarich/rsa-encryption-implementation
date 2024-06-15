#finished April 4th, 2022
#approximately 10 hours of work
#basic form of RSA encryption which only works with letters. The decrypted product omits capitalization and spaces included in the encryption process

import textwrap

p = 939391
q = 6301
e = 23
n = p*q
phi = (p-1)*(q-1)
group = 0

def encrypt(ciphers):
    encrypted_message = ""
    for cipher in ciphers:
        encrypted_message += str(fast_modular_exponentiation(int(cipher), n, e)) + " "
    return encrypted_message

def decrypt(ciphers):
    decrypted_message = ""
    written_message = ""
    b, d = alt_extended_euclidean(phi, e)
    #while d < 0:
       #d += phi
    print(d)
    for cipher in ciphers:
        decrypted_message += str(fast_modular_exponentiation(int(cipher), n, d)) + " "
    ciphers = decrypted_message.split()
    for i, cipher in enumerate(ciphers):
        if len(cipher) % 2 != 0:
            cipher = "0" + cipher
            ciphers[i] = cipher
        messages = textwrap.wrap(cipher, 2)
        for message in messages:
            if message[0] == "0":
                written_message += chr(int(message[1]) + 96)
            else:
                written_message += chr(int(message) + 96)
    print(ciphers)
    return written_message

def fast_modular_exponentiation(cipher, n, e):
    x = 1
    power = cipher % n
    a = str(bin(e).replace("0b", ""))
    for i in range(len(a)-1,-1,-1):
        if a[i] == "1":
            x = (x*power) % n
        power = (power*power) % n
    return x

#geeksforgeeks algorithm
def extended_euclidean(phi, e):
    if phi == 0:
        return 0, 1
    
    x_1, y_1 = extended_euclidean(e % phi, phi)

    x = y_1 - (e // phi) * x_1
    y = x_1

    return x, y

#dcode.fr algorithm
def alt_extended_euclidean(phi , e):
    r = phi
    r_1 = e
    b = 1
    d = 0
    b_1 = 0
    d_1 = 1

    while r_1 != 0:
        q = r // r_1
        r_2 = r
        b_2 = b
        d_2 = d
        r = r_1
        b = b_1
        d = d_1
        r_1 = r_2 - q *r_1
        b_1 = b_2 - q * b_1
        d_1 = d_2 - q * d_1

    if d < 0:
        d += phi

    return b, d

#def test_bezout():
    n = 64
    m = 35
    r = n % m
    equations = []
    equations.append(str(r) + " = " + str(n)  + " - 1*" + str(m))

    while (r != 1):
        n = m
        m = r
        r = n % m
        equations.append(str(r) + " = " + str(n)  + " - 1*" + str(m))

    print(equations)

def rsa():
    print("Would you like to encrypt or decrypt a message? (e/d):")
    action = str(input())
    if (action.lower() == "e"):
        print("Enter the message you would like to encrypt (lowercase letters only):")
        message = str(input())
        num_char_list = []
        num_message = ""
        ciphers = []
        strip_message = message.lower().replace(" ", "")
        char_list = [i for i in strip_message]
        for char in char_list:
            if ord(char) - 96 < 10:
                temp = "0" + str(ord(char)-96)
                num_char_list.append(temp)
            else:
                num_char_list.append(ord(char)-96)
        for num in num_char_list:
            num_message += str(num)
        #if len(num_message) % 4 != 0:
            #num_message += "X"*(len(num_message)%4)

        digits_of_phi = len(str(phi))
        print(phi)
        print(digits_of_phi)
        if digits_of_phi % 2 != 0:
            group = digits_of_phi - 1
            print(group)
        else:
            number = "26" * (digits_of_phi // 2)
            print(number)
            if int(number) > phi:
                number = number[:len(number)-2]
                print(number)
            group = len(number)
            print(group)

        ciphers = textwrap.wrap(num_message, group)
        print(ciphers)
        print("The encrypted message is " + encrypt(ciphers))
        
    elif (action.lower() == "d"):
        print("Enter the encrypted version of the message:")
        e_message = str(input())
        e_message_list = e_message.split()
        print("The decrypted message is " + decrypt(e_message_list))
    else:
        print("Enter a valid option")
        rsa()
rsa()