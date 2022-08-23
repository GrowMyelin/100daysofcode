alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  shifted_text = ''
  for ltr in text:
    new_idx = (alphabet.index(ltr) + shift) % len(alphabet)
    shifted_text += alphabet[new_idx]
  print(shifted_text)

def decrypt(text,shift):
  shifted_text = ''
  for ltr in text:
    new_idx = (alphabet.index(ltr) - shift) % len(alphabet)
    shifted_text += alphabet[new_idx]
  print(shifted_text)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction.lower() == 'encode':
        encrypt(text,shift)
    elif direction.lower() == 'decode':
        decrypt(text,shift)
    else:
        print('Enter encode or decode.')

if __name__ == "__main__":
    main()