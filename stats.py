def get_word_count(text):
    words = str.split(text)
    return len(words)

def get_character_count_dict(text):

    character_dict = {}

    characters = list(text)
    for character in characters:
        character = str.lower(character)

        count = character_dict.get(character)
        if count is None:
            count = 0
        character_dict.update({character: count + 1})

    return character_dict