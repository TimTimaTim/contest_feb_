alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
decoded_message = ""

file = open("secret.txt")

for line in file:
    vowel_count = 0

    for character in line:
        if character in vowels:
            vowel_count = vowel_count + 1

    decoded_message = decoded_message + alphabet[vowel_count]

file.close()

print(decoded_message)