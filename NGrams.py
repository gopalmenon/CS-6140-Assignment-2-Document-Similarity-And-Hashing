from nltk.util import ngrams
import nltk

"""Return character n-grams"""
def get_character_n_grams(file_contents, n):

    for file_snippet in file_contents:
        file_n_grams = ngrams(file_snippet, n)
        for n_gram in file_n_grams:
            yield(n_gram)