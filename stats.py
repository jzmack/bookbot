def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1

    return letter_count

def sort_on(items):
    return items["num"]

def sort_letters(letter_dict):
    sorted_list = []
    
    for letter in letter_dict:
        l_dict = {}
        count = letter_dict[letter]
        l_dict["char"] = letter
        l_dict["num"] = count
        sorted_list.append(l_dict)
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
