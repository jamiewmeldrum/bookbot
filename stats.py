def get_word_count(text):
    words = str.split(text)
    return len(words)

def get_character_count_dict(text):

    character_dict = {}

    for character in text:
        character = character.lower()

        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict