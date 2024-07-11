def caesar_shift(letter, shift, encrypting=True):
    if letter.isalpha():
        ascii_start = ord('A') if letter.isupper() else ord('a')
        shift_direction = shift if encrypting else -shift
        return chr((ord(letter) - ascii_start + shift_direction) % 26 + ascii_start)
    return letter

def encrypt(text, shift):
    return ''.join(caesar_shift(letter, shift, True) for letter in text)

def decrypt(text, shift):
    return ''.join(caesar_shift(letter, shift, False) for letter in text)

def main():
    while True:
        action = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
        if action in ['E', 'D']:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            result = encrypt(text, shift) if action == 'E' else decrypt(text, shift)
            print(f"{'Encrypted' if action == 'E' else 'Decrypted'} text: {result}")
        else:
            print("Invalid input. Please enter 'E' for encryption or 'D' for decryption.")
        
        if input("Do you want to continue? (Y/N): ").strip().upper() != 'Y':
            break

if __name__ == "__main__":
    main()
