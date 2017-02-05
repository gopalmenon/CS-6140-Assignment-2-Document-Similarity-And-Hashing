import FileIo
import NGrams
import sys

SALT_FILE_NAME = "Data/MobyDickChapter1.txt"
N_GRAMS_SIZE = 3


class NGramHash(object):

    """Get character n-grams from salt file"""
    def __get_salt_file_character_n_grams(self):
        char_n_grams = NGrams.get_character_n_grams(FileIo.get_text_file_contents(SALT_FILE_NAME), N_GRAMS_SIZE)
        char_n_gram_set = set()
        for n_gram in char_n_grams:
            char_n_gram_set.add(n_gram)
        return list(char_n_gram_set)

    def __init__(self):
        self.salt_n_grams = self.__get_salt_file_character_n_grams()

    """Get the hash value for an n-gram. Salt for the hash
    function is the hash_function_number n-gram in char_n_gram_set"""
    def get_n_gram_hash(self, string_to_hash, hash_function_number):

        try:
            salt_for_hash_function = self.salt_n_grams[hash_function_number]
            return hash(str(salt_for_hash_function) + string_to_hash) + sys.maxsize + 1

        except IndexError:
            print("Index " + str(hash_function_number) + " is outside the range")
            sys.exit()