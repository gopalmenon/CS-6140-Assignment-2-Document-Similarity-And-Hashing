import FileIo
import NGrams


FILE_D1 ="Data/D1.txt"
FILE_D2 ="Data/D2.txt"
FILE_D3 ="Data/D3.txt"
FILE_D4 ="Data/D4.txt"

TWO_GRAM = 2
THREE_GRAM = 3

"""Construct character 2-grams for all documents"""
d1_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D1), TWO_GRAM)
d2_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D2), TWO_GRAM)
d3_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D3), TWO_GRAM)
d4_2_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D4), TWO_GRAM)

"""Construct character 3-grams for all documents"""
d1_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D1), THREE_GRAM)
d2_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D2), THREE_GRAM)
d3_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D3), THREE_GRAM)
d4_3_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(FILE_D4), THREE_GRAM)


