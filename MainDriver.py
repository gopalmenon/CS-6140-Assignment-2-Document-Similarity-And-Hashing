import FileIo
import NGrams


FILE_D1 ="Data/D1.txt"
FILE_D2 ="Data/D2.txt"
FILE_D3 ="Data/D3.txt"
FILE_D4 ="Data/D4.txt"

TWO_GRAM = 2
THREE_GRAM = 3

"""Construct character 2-grams for all documents"""
d1_char_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D1), TWO_GRAM)
d1_char_2_gram_set = set()
for n_gram in d1_char_2_grams:
    d1_char_2_gram_set.add(n_gram)
print("D1.txt has " + str(len(d1_char_2_gram_set)) + " character 2-grams")

d2_char_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D2), TWO_GRAM)
d2_char_2_gram_set = set()
for n_gram in d2_char_2_grams:
    d2_char_2_gram_set.add(n_gram)
print("D2.txt has " + str(len(d2_char_2_gram_set)) + " character 2-grams")

d3_char_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D3), TWO_GRAM)
d3_char_2_gram_set = set()
for n_gram in d3_char_2_grams:
    d3_char_2_gram_set.add(n_gram)
print("D3.txt has " + str(len(d3_char_2_gram_set)) + " character 2-grams")

d4_char_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D4), TWO_GRAM)
d4_char_2_gram_set = set()
for n_gram in d4_char_2_grams:
    d4_char_2_gram_set.add(n_gram)
print("D4.txt has " + str(len(d4_char_2_gram_set)) + " character 2-grams")


"""Construct character 3-grams for all documents"""
d1_char_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D1), THREE_GRAM)
d1_char_3_gram_set = set()
for n_gram in d1_char_3_grams:
    d1_char_3_gram_set.add(n_gram)
print("D1.txt has " + str(len(d1_char_3_gram_set)) + " character 3-grams")

d2_char_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D2), THREE_GRAM)
d2_char_3_gram_set = set()
for n_gram in d2_char_3_grams:
    d2_char_3_gram_set.add(n_gram)
print("D2.txt has " + str(len(d2_char_3_gram_set)) + " character 3-grams")

d3_char_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D3), THREE_GRAM)
d3_char_3_gram_set = set()
for n_gram in d3_char_3_grams:
    d3_char_3_gram_set.add(n_gram)
print("D3.txt has " + str(len(d3_char_3_gram_set)) + " character 3-grams")

d4_char_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D4), THREE_GRAM)
d4_char_3_gram_set = set()
for n_gram in d4_char_3_grams:
    d4_char_3_gram_set.add(n_gram)
print("D4.txt has " + str(len(d4_char_3_gram_set)) + " character 3-grams")

"""Construct word 2-grams for all documents"""
d1_word_2_grams = NGrams.get_word_n_grams(FileIo.get_text_file_contents(FILE_D1), TWO_GRAM)
d1_word_2_gram_set = set()
for n_gram in d1_word_2_grams:
    d1_word_2_gram_set.add(n_gram)
print("D1.txt has " + str(len(d1_word_2_gram_set)) + " word 2-grams")

d2_word_2_grams = NGrams.get_word_n_grams(FileIo.get_text_file_contents(FILE_D2), TWO_GRAM)
d2_word_2_gram_set = set()
for n_gram in d2_word_2_grams:
    d2_word_2_gram_set.add(n_gram)
print("D2.txt has " + str(len(d2_word_2_gram_set)) + " word 2-grams")

d3_word_2_grams = NGrams.get_word_n_grams(FileIo.get_text_file_contents(FILE_D3), TWO_GRAM)
d3_word_2_gram_set = set()
for n_gram in d3_word_2_grams:
    d3_word_2_gram_set.add(n_gram)
print("D3.txt has " + str(len(d3_word_2_gram_set)) + " word 2-grams")

d4_word_2_grams = NGrams.get_word_n_grams(FileIo.get_text_file_contents(FILE_D4), TWO_GRAM)
d4_word_2_gram_set = set()
for n_gram in d4_word_2_grams:
    d4_word_2_gram_set.add(n_gram)
print("D4.txt has " + str(len(d4_word_2_gram_set)) + " word 2-grams")
