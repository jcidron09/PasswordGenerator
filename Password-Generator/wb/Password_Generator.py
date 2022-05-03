import random
import string
import math
import Word_Reader
# uppercase letters are characters A-Z
# lowercase letters are characters a-z
# digits are characters 0-9
# punctuation characters are :;'"?,.`
# special characters are characters !@#$%^&*(){}[]\~<>+=_-


def create_lower_alpha(character_limit):
    password = ""
    for i in range(0, character_limit):
        password += random.choice(string.ascii_lowercase)
    return password


def create_upper_alpha(character_limit):
    password = ""
    for i in range(0, character_limit):
        password += random.choice(string.ascii_uppercase)
    return password


def create_alpha(character_limit):
    password = ""
    for i in range(0, character_limit):
        upper_or_lower = random.randint(0, 1)
        if upper_or_lower == 0:
            password += random.choice(string.ascii_lowercase)
        else:
            password += random.choice(string.ascii_uppercase)
    return password


def create_digits(character_limit):
    return int((random.randint(int(math.pow(10, character_limit)), (int(math.pow(10, character_limit+1)))))/10)


def create_punctuation(character_limit):
    punctuations = "!\",.:;?\'"
    password = ""
    for i in range(0, character_limit):
        password += random.choice(punctuations)
    return password


def create_special_characters(character_limit):
    special_characters = "#$%&()*+/@[]^_`{|}~"
    password = ""
    for i in range(0, character_limit):
        password += random.choice(special_characters)
    return password


def create_word_password(word_amount):
    words = []
    cancat_word = Word_Reader.get_word_by_index(random.randint(0, len(Word_Reader.read_words())))
    for i in range (0, word_amount):
        word = Word_Reader.get_word_by_index(random.randint(0, len(Word_Reader.read_words())))
        words.append(word)
        cancat_word += "-" + word
    return cancat_word


def create_password(character_limit, all_allowed, lowercase_letters_allowed, uppercase_letters_allowed, alpha_allowed,
                    digits_allowed, alphanumerics_allowed, punctuation_allowed, special_characters_allowed):
    # 0 lowercase
    # 1 uppercase
    # 2 digits
    # 3 punctuation
    # 4 special characters
    if character_limit < 1:
        return None
    if all_allowed:
        pass
    elif lowercase_letters_allowed:
        pass
    elif uppercase_letters_allowed:
        pass
    elif alpha_allowed:
        pass
    elif digits_allowed:
        pass
    elif alphanumerics_allowed:
        pass
    elif punctuation_allowed:
        pass
    elif special_characters_allowed:
        pass
    else:
        return ""

    password = ""
    if all_allowed:
        for i in range(0, character_limit):
            character = random.randint(0, 5)
            if character == 0:
                password += create_lower_alpha(1)
            elif character == 1:
                password += create_upper_alpha(1)
            elif character == 2:
                password += str(create_digits(1))
            elif character == 3:
                password += create_punctuation(1)
            elif character == 4:
                password += create_special_characters(1)
    else:
        allowed_characters = []
        if alphanumerics_allowed:
            allowed_characters.append(0)
            allowed_characters.append(1)
            allowed_characters.append(2)
        elif alpha_allowed:
            allowed_characters.append(0)
            allowed_characters.append(1)
        elif lowercase_letters_allowed:
            allowed_characters.append(0)
        elif uppercase_letters_allowed:
            allowed_characters.append(1)
        elif digits_allowed:
            allowed_characters.append(2)
        if punctuation_allowed:
            allowed_characters.append(3)
        if special_characters_allowed:
            allowed_characters.append(4)

        if len(allowed_characters) == 1:
            if allowed_characters[0] == 0:
                return create_lower_alpha(character_limit)
            elif allowed_characters[0] == 1:
                return create_upper_alpha(character_limit)
            elif allowed_characters[0] == 2:
                return create_digits(character_limit)
            elif allowed_characters[0] == 3:
                return create_punctuation(character_limit)
            elif allowed_characters[0] == 4:
                return create_special_characters(character_limit)

        for i in range(0, character_limit):
            character = random.choice(allowed_characters)
            if character == 0:
                password += create_lower_alpha(1)
            elif character == 1:
                password += create_upper_alpha(1)
            elif character == 2:
                password += str(create_digits(1))
            elif character == 3:
                password += create_punctuation(1)
            elif character == 4:
                password += create_special_characters(1)
    return password


if __name__ == "__main__":
    print(create_word_password(10))
