def n_words(text):
    return len(text.split())

def get_count_letters(text):
    character_frequency = {}
    for character in text:
        character = character.lower()
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1
    
    return character_frequency

def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key= lambda item: item[1], reverse= True))