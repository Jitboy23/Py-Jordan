Ceaser_Art = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
print(Ceaser_Art)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 0, 1, 
2, 3, 4, 5, 6, 7, 8, 9]




#-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(direct, plain_text, shift_amount, decrypted_text, decrypted_shift_amount):
    
    if direct == 'encode':
        string = ''
        for letter in plain_text:
            letter_index = alphabet.index(letter)
            index_position = letter_index + shift_amount
            if shift_amount >= 26:
                shift_amount = shift_amount % 26
            if index_position >= 26:
                index_position = index_position - 26
            final_position = alphabet[index_position]
            string += final_position
        print(f"Your encrypted message is: {string}")
    
    elif direct == 'decode':
        string2 = ''
        for decode_letter in decrypted_text:
            decode_index = alphabet.index(decode_letter)
            new_decoded_index = decode_index - decrypted_shift_amount
            final_decoded_message = alphabet[new_decoded_index]
            string2 += final_decoded_message
        print(f"Your decrypted message is: {string2}")


#loop flag
cypher_loop = True
while cypher_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        cypher_loop = False
    else:
        print('Invalid Entry')
        cypher_loop = False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(direction, plain_text=text, shift_amount=shift, decrypted_text=text, decrypted_shift_amount=shift)



#-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##Bug alert: What happens if you try to encode the word 'civilization'?

#-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 