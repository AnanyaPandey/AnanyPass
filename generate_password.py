import random
import string
from pathlib import Path
ROOTDIR = Path('G:/py/passowordgen/Ananypass')

# List of Hindi words transliterated to English (you can extend this list)
hindi_words_transliterated = [
    # ... (same as in your original code)
    "Sundar", "Sukha", "Pyaara", "Chhota", "Mota", "Bura", "Khoobsurat",
    "Swasth", "Garib", "Ameer", "Nanga", "Jhulta", "Majedar", "Garam",
    "Thanda", "Naya", "Purana", "Lal", "Hara", "Neela", "Safed", "Kala",
    "Sukha", "Dhaniya", "Lamba", "Samridh", "Sachcha", "Jhoota", "Sharif",
    "Tez", "Teekha", "Udta", "Langda", "Jhagdalu", "Budbak", "Gaddar", "Bhutiya",
    "Chulbul","Bhukkad","Peela","Lambu","Namkeen","Shaana"
]

hindi_words_transliterated2 = [
    # ... (same as in your original code)
     "Kanya", "Talwar", "Teer", "Tyagi", "Chhatri", "Pappu","Hira",
    "Maal", "Rasta", "Mazdur", "kitab", "kaagaz", "Tubelight","Moza",
    "kursi", "botal", "raja", "don", "bhai", "Sipahi","Bijli","Jhola",
    "Shakeel", "gunda", "Aurat", "Panchi", "Chaman","Mogambo","Pustak"
    "Khidki", "Darwaza", "Mahal", "Gulaab","Kachra","Paanwala","Ghoda"
]

def replace_characters(word):
    # ... (same as in your original code)
    # Replace 's' with '$', 'o' with '0'
    word = word.replace('s', '$')
    word = word.replace('o', '0')
    return word

def generate_strong_password(password_length):
    # ... (same as in your original code)
    if password_length < 7:
        return "Password length is too short (minimum length is 7 characters)."

    while True:
        word1 = random.choice(hindi_words_transliterated)
        word2 = random.choice(hindi_words_transliterated2)
        if word1 != word2:
            break

    readable = f"{word1} {word2}"
    word1 = replace_characters(word1).capitalize()
    word2 = replace_characters(word2).capitalize()


    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    password = [word1, word2, digit, special_char]

    indicestoshuffle = [0, 2, 3]
    shuffled_elements = random.sample([password[i] for i in indicestoshuffle], len(indicestoshuffle))
    random.shuffle(shuffled_elements)
    for i, index in enumerate(indicestoshuffle):
        password[index] = shuffled_elements[i]

    password = ''.join(map(str, password))
    # readable = f"{word1} {word2}"

    return password, readable

def generate_passwords(num_passwords=5):
    # ... (same as in your original code)
    password_length = 11
    passwords = []
    readables = []

    for _ in range(num_passwords):
        password, readable = generate_strong_password(password_length)
        passwords.append(password)
        readables.append(readable)

    # print_Password(passwords,readables)
    return passwords,readables

def pull_hindi_words(filename):
    # filepaths = ROOTDIR.glob("Some*.txt")
    # for each in filepaths:
    fname=Path(filename)
    with open(fname,'r') as file :
        passw = file.readlines()
    return passw

def generate_user_pass(user_pass_words,password_length=10):
    # ... (same as in your original code)
    if password_length < 7:
        return "Password length is too short (minimum length is 7 characters)."

    while True:
        word1 = random.choice(user_pass_words)
        word2 = random.choice(user_pass_words)
        if word1 != word2:
            break

    readable = f"{word1} {word2}"
    word1 = replace_characters(word1).capitalize()
    word2 = replace_characters(word2).capitalize()


    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)
    password = [word1, word2, digit, special_char]

    indicestoshuffle = [0, 2, 3]
    shuffled_elements = random.sample([password[i] for i in indicestoshuffle], len(indicestoshuffle))
    random.shuffle(shuffled_elements)
    for i, index in enumerate(indicestoshuffle):
        password[index] = shuffled_elements[i]

    password = ''.join(map(str, password))
    # readable = f"{word1} {word2}"

    return password, readable
def generate_userpass(user_pass_words,num_passwords=5):
    # ... (same as in your original code)
    password_length = 11
    passwords = []
    readables = []

    for _ in range(num_passwords):
        password, readable = generate_user_pass(user_pass_words)
        passwords.append(password)
        readables.append(readable)

    # print_Password(passwords,readables)
    return passwords,readables

if __name__ == '__main__':
    test = ['Hello', 'World', 'This', 'Is', 'a', 'Wondeful', 'World']
    pasw,reads = generate_userpass(test)
    print(pasw)
    print(reads)