import FileIo
import HashFunctions
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

"""Print n-gram set size"""
def print_set_size(file_name, set_name, n_gram_type, n_gram_size):

    print(file_name + " has " + str(len(set_name)) + " distinct " + n_gram_type + str(n_gram_size) + "-grams")

"""Return the Jaccard Similarity between the two sets"""
def get_jaccard_similarity(set_1, set_2):

    return len(set_1.intersection(set_2))/len(set_1.union(set_2))

def print_n_gram_stats():

    """Character 2-grams"""
    file_name = ALL_FILES[0]
    d1_char_2_grams = get_character_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d1_char_2_grams, "character", TWO_GRAM)

    file_name = ALL_FILES[1]
    d2_char_2_grams = get_character_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d2_char_2_grams, "character", TWO_GRAM)

    file_name = ALL_FILES[2]
    d3_char_2_grams = get_character_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d3_char_2_grams, "character", TWO_GRAM)

    file_name = ALL_FILES[3]
    d4_char_2_grams = get_character_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d4_char_2_grams, "character", TWO_GRAM)

    """Character 3-grams"""
    file_name = ALL_FILES[0]
    d1_char_3_grams = get_character_n_gram_set(file_name, THREE_GRAM)
    print_set_size(file_name, d1_char_3_grams, "character", THREE_GRAM)

    file_name = ALL_FILES[1]
    d2_char_3_grams = get_character_n_gram_set(file_name, THREE_GRAM)
    print_set_size(file_name, d2_char_3_grams, "character", THREE_GRAM)

    file_name = ALL_FILES[2]
    d3_char_3_grams = get_character_n_gram_set(file_name, THREE_GRAM)
    print_set_size(file_name, d3_char_3_grams, "character", THREE_GRAM)

    file_name = ALL_FILES[3]
    d4_char_3_grams = get_character_n_gram_set(file_name, THREE_GRAM)
    print_set_size(file_name, d3_char_3_grams, "character", THREE_GRAM)

    """Word 2-grams"""
    file_name = ALL_FILES[0]
    d1_word_2_grams = get_word_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d1_word_2_grams, "word", TWO_GRAM)

    file_name = ALL_FILES[1]
    d2_word_2_grams = get_word_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d2_word_2_grams, "word", TWO_GRAM)

    file_name = ALL_FILES[2]
    d3_word_2_grams = get_word_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d3_word_2_grams, "word", TWO_GRAM)

    file_name = ALL_FILES[3]
    d4_word_2_grams = get_word_n_gram_set(file_name, TWO_GRAM)
    print_set_size(file_name, d4_word_2_grams, "word", TWO_GRAM)

    """Print Jaccard Similarities between character 2-grams"""
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[1] + " is " + format(get_jaccard_similarity(d1_char_2_grams, d2_char_2_grams), '.4f'))
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d1_char_2_grams, d3_char_2_grams), '.4f'))
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d1_char_2_grams, d4_char_2_grams), '.4f'))
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[1] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d2_char_2_grams, d3_char_2_grams), '.4f'))
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[1] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d2_char_2_grams, d4_char_2_grams), '.4f'))
    print("Jaccard Similarity between character 2-grams of " + ALL_FILES[2] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d3_char_2_grams, d4_char_2_grams), '.4f'))

    """Print Jaccard Similarities between character 3-grams"""
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[0] + " and " + ALL_FILES[1] + " is " + format(get_jaccard_similarity(d1_char_3_grams, d2_char_3_grams), '.4f'))
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[0] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d1_char_3_grams, d3_char_3_grams), '.4f'))
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[0] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d1_char_3_grams, d4_char_3_grams), '.4f'))
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[1] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d2_char_3_grams, d3_char_3_grams), '.4f'))
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[1] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d2_char_3_grams, d4_char_3_grams), '.4f'))
    print("Jaccard Similarity between character 3-grams of " + ALL_FILES[2] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d3_char_3_grams, d4_char_3_grams), '.4f'))

    """Print Jaccard Similarities between word 2-grams"""
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[1] + " is " + format(get_jaccard_similarity(d1_word_2_grams, d2_word_2_grams), '.4f'))
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d1_word_2_grams, d3_word_2_grams), '.4f'))
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[0] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d1_word_2_grams, d4_word_2_grams), '.4f'))
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[1] + " and " + ALL_FILES[2] + " is " + format(get_jaccard_similarity(d2_word_2_grams, d3_word_2_grams), '.4f'))
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[1] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d2_word_2_grams, d4_word_2_grams), '.4f'))
    print("Jaccard Similarity between word 2-grams of " + ALL_FILES[2] + " and " + ALL_FILES[3] + " is " + format(get_jaccard_similarity(d3_word_2_grams, d4_word_2_grams), '.4f'))

print_n_gram_stats()
n_gram_hash = HashFunctions.NGramHash()

print(str( n_gram_hash.get_n_gram_hash("Gopal", 0)))
print(str( n_gram_hash.get_n_gram_hash("Gopal", 1)))
print(str( n_gram_hash.get_n_gram_hash("Gopal", 2)))
print(str( n_gram_hash.get_n_gram_hash("Gopal", 0)))
