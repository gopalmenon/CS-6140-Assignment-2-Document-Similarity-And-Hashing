import FileIo
import NGrams

ALL_FILES = ["Data/D1.txt", "Data/D2.txt", "Data/D3.txt", "Data/D4.txt"]

TWO_GRAM = 2
THREE_GRAM = 3

"""Return character n-gram set"""
def get_character_n_gram_set(file_name, n):
    char_n_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(file_name), n)
    char_n_gram_set = set()
    for n_gram in char_n_grams:
        char_n_gram_set.add(n_gram)
    return char_n_gram_set

"""Return word n-gram set"""
def get_word_n_gram_set(file_name, n):

    word_n_grams = NGrams.get_word_n_grams(FileIo.get_text_file_contents(file_name), n)
    word_n_gram_set = set()
    for n_gram in word_n_grams:
        word_n_gram_set.add(n_gram)
    return word_n_gram_set

"""Print n-gram counts and return n-gram sets"""
def get_n_gram_sets():

    character_2_gram_sets = set()
    character_3_gram_sets = set()
    word_2_gram_sets = set()

    for file_name in ALL_FILES:

        character_2_gram_sets.add(get_character_n_gram_set(file_name, TWO_GRAM))
        character_3_gram_sets.add(get_character_n_gram_set(file_name, THREE_GRAM))
        word_2_gram_sets.add(get_word_n_gram_set(file_name, TWO_GRAM))

        print(file_name + " has " + str(len(character_2_gram_sets[len(character_2_gram_sets) - 1])) + " character " + str(TWO_GRAM) + "-grams")
        print(file_name + " has " + str(len(character_3_gram_sets[len(character_3_gram_sets) - 1])) + " character " + str(THREE_GRAM) + "-grams")
        print(file_name + " has " + str(len(word_2_gram_sets[len(word_2_gram_sets) - 1])) + " word " + str(TWO_GRAM) + "-grams")

        return character_2_gram_sets, character_3_gram_sets, word_2_gram_sets

"""Print Jaccard Similarity for eklements in the set"""
def print_jaccard_similarity(list_of_sets):

    print("Similarity between first two is " + str(   len(     list_of_sets[0].intersection(list_of_sets[1])/len(list_of_sets[0].union(list_of_sets[1]  ) ))))

character_2_gram_sets, character_3_gram_sets, word_2_gram_sets = get_n_gram_sets()
print_jaccard_similarity(character_2_gram_sets)