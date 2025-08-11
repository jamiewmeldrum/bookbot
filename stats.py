def get_word_count(text):
    words = str.split(text)
    return len(words)

def get_characters(text):

    character_count_dict = {}

    for character in text:
        character = character.lower()

        if character in character_count_dict:
            character_count_dict[character] += 1
        else:
            character_count_dict[character] = 1

    characters = []
    for character in character_count_dict:
        characters.append(
            {
                "char": character,
                "num": character_count_dict[character]
            }
        )

    return characters


def characters_sort_on(items):
    return items["num"]


def sort_characters(characters):
    characters.sort(reverse=True, key=characters_sort_on)


def filter_non_alphabet(characters):
    filtered_characters = []
    for character in characters:
        if character["char"].isalpha():
            filtered_characters.append(character)

    return filtered_characters