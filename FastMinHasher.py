import HashFunctions
import sys


class FastMinHasher(object):

    def __init__(self, document_n_grams, number_of_hash_functions):
        self.document_n_grams = document_n_grams
        self.number_of_hash_functions = number_of_hash_functions
        self.document_vector_representation = self.to_vector()

    """Convert document n-grams to vector representation"""
    def to_vector(self):

        """Create initial vector filled with max values"""
        document_vector_representation = [sys.maxsize for index in range(self.number_of_hash_functions)]

        n_gram_hash = HashFunctions.NGramHash()

        """Loop through every n-gram"""
        for n_gram in self.document_n_grams:

            n_gram_string = ""
            for character in n_gram:
                n_gram_string += character

            """Hash the n-gram using each of the hash functions and put in the vector"""
            for hash_function in range(self.number_of_hash_functions):
                n_gram_hash_value = n_gram_hash.get_n_gram_hash(n_gram_string, hash_function)
                if n_gram_hash_value < document_vector_representation[hash_function]:
                    document_vector_representation[hash_function] = n_gram_hash_value

        return document_vector_representation

    """Return Jaccard Similarity between this and another document vector"""
    def  get_jaccard_similarity(self, other_document_vector_representation):

        """The other document vector must have the same number of elements as the number of hash functions"""
        if len(other_document_vector_representation) != self.number_of_hash_functions:
            raise ValueError("Document vector should have a length of " + str(self.number_of_hash_functions))

        jaccard_similarity = 0
        for index in range(len(self.document_vector_representation)):
            if self.document_vector_representation[index] == other_document_vector_representation[index]:
                jaccard_similarity += 1

        return jaccard_similarity / len(self.document_vector_representation)