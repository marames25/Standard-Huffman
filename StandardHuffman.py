class HuffmanCoding:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.probabilities = {}
        self.codes = {}
        self.reverse_mapping = {}


    # Compression part
   

    def calculate_probabilities(self):
        """
        Reads the input file and calculates the probability of each symbol.
        Returns a dictionary {symbol: probability}.
        """
        pass

    def sort_probabilities_descending(self, probabilities):
        """
        Sorts the symbols based on probability in descending order.
        Returns a list of tuples [(symbol, probability), ...].
        """
        pass

    def build_huffman_tree(self, sorted_probabilities):
        """
        Builds the Huffman tree by repeatedly summing the two smallest probabilities.
        Returns the root of the tree.
        """
        pass

    def generate_codes(self, tree_root):
        """
        Traverses the Huffman tree to generate binary codes for each symbol.
        """
        pass

    def encode_data(self, data):
        """
        Encodes the input data using the generated Huffman codes.
        Returns the bitstring.
        """
        pass

    def save_compressed_file(self, bitstring):
        """
        Saves the compressed data as binary (actual bits) to the output file.
        Overhead (e.g., codes or metadata) may be stored in a readable format.
        """
        pass

    def compress(self):
        """
        Main function to perform compression:
        1. Calculate probabilities
        2. Sort descending
        3. Build Huffman tree
        4. Generate codes
        5. Encode and save to binary file
        """
        pass


    # Decompression part
   

    def load_compressed_file(self):
        """
        Loads the compressed binary file and retrieves the bitstream and any stored metadata.
        """
        pass

    def decode_data(self, bitstring):
        """
        Decodes the bitstring using the stored Huffman codes.
        Returns the original text.
        """
        pass

    def save_decompressed_file(self, data):
        """
        Writes the decompressed text to the output file.
        """
        pass

    def decompress(self):
        """
        Main function to perform decompression:
        1. Load compressed file
        2. Decode bitstream
        3. Save decompressed text
        """
        pass
