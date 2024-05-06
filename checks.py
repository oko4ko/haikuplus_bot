import datetime

def is_haiku(text):
    vowels = 'аоуыэяёюие'
    syllable_structure = [5, 7, 5]
    words = text.strip().split()
    vowel_count = [0] * len(words)
    sum_of_vowels = 0
    for i in range(len(words)):
        word = words[i]
        for vowel in vowels:
            vowel_count[i] += word.count(vowel)
            sum_of_vowels += word.count(vowel)
        if sum_of_vowels > 17:
            return None

    if sum_of_vowels == 17:
        haiku = ''
        start_word_index = 0
        end_word_index = 0
        for needed_syllable_count in syllable_structure:
            haiku_string = ''
            current_vowel_count = 0
            while current_vowel_count < needed_syllable_count: #fix prepositions
                current_vowel_count += vowel_count[end_word_index]
                end_word_index += 1
            if current_vowel_count == needed_syllable_count:
                for word in words[start_word_index:end_word_index]:
                    haiku_string += word
                    haiku_string += ' '

                haiku_string = haiku_string[:-1]
                haiku_string += '\n\n'
                print(haiku_string)
                haiku += haiku_string
                start_word_index = end_word_index
            else:
                return None
        haiku = haiku[:-2]
        return haiku

def add_info(text, username):
    text_date = datetime.datetime.today().strftime('%d.%m.%Y')
    text += '\n\n'
    if str(username) == '':
        text += f'Аноним, {text_date}'
    else:
        text += f'@{username}, {text_date}'
    return text


