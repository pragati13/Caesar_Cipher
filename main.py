import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
  
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)


flag = True 
while flag:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

  if direction != "encode" and direction != "decode":
    print("Please enter correct input...")
    continue
    
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift%26, cipher_direction=direction)
  answer = input("Type 'yes' if you want to go again. Otheriwse type 'no'\n").lower()
  if answer == "yes":
    continue
  elif answer == "no":
    print("Goodbye")
    flag = False
  else:
    print("Please enter valid input...")
    while(True):
       answer = input("Type 'yes' if you want to go again. Otheriwse type 'no'\n").lower()
       if answer == "yes":
          break
       elif answer == "no":
          print("Goodbye")
          flag = False
          break