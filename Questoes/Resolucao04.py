import re
def capitalize_sentences(input_string):
    sentences = re.split(r'(?<=[.?!:;])\s+', input_string)
    capitalized_sentences = []

    for sentence in sentences:
        words = sentence.split()
        capitalized_words = []

        for i, word in enumerate(words):
            if not any(char.isdigit() for char in word):
                if i == 0:
                    capitalized_words.append(word.capitalize())
                else:
                    capitalized_words.append(word)
        capitalized_sentence = ' '.join(capitalized_words)
        capitalized_sentences.append(capitalized_sentence)
    output_string = ' '.join(capitalized_sentences)
    return output_string
input_string = input("Digite algo: ")
output_string = capitalize_sentences(input_string)
print(output_string)