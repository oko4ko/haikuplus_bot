import datetime
from tsnorm import Normalizer

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

def is_ring(text):
    vowels = 'аоуыэяёюие'
    sum_of_vowels = 0
    for i in text: #count vowels in order to discard messages without exactly 7 vowels
        if i in vowels:
            sum_of_vowels += 1
            if sum_of_vowels > 7:
                return None

    if sum_of_vowels == 7: #need seven vowels for обручальное кольцо
        stress_mark = '+'
        normalizer = Normalizer(stress_mark=stress_mark, stress_mark_pos="before", stress_yo=True, stress_monosyllabic=True)
        stressed_text = normalizer(text)

        for i in vowels: #list of syllables
            stressed_text = stressed_text.replace(i, i + 'SpLiT')
        stressed_text = stressed_text.replace(' ', ' ' + 'SpLiT')
        splitted_text = stressed_text.split('SpLiT')

#TODO: add vowels between syllabic sonorants and abbreviations' consonants

        final_split = [] #merging ending consonants with open syllables to get closed syllables
        current_syll = splitted_text[0]
        for i in splitted_text[1:]:
            if all([k not in i for k in vowels]): #if no vowel in syllable
                current_syll += i
            else:
                final_split.append(current_syll)
                current_syll = i
        final_split.append(current_syll) #this is now list of syllables in phrase (with stress marks)

        print(final_split)

        #checking for the needed stress pattern here
        #need stress in the final syllable and no stress in even-numbered syllables
        #TODO: pattern is imperfect, needs rewriting
        pattern = int(''.join(list(map(lambda x: '1' if '+' in x else '0', final_split))), 2)
        if pattern & 0b101011 == 1: #bit mask things
            return text
        else:
            return None


    else:
        return None



def add_info(text, username):
    text_date = datetime.datetime.today().strftime('%d.%m.%Y')
    text += '\n\n'
    if str(username) == '':
        text += f'Аноним, {text_date}'
    else:
        text += f'@{username}, {text_date}'
    return text


