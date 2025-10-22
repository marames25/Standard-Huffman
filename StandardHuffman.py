import heapq
import os
from collections import Counter
class Node:
    def __init__(self,char,freq):
        self.char =  char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq
    
class HuffmanCoding:
    def __init__(self, inputFile, outputFile):
        self.input_file = inputFile
        self.output_file = outputFile
        self.probabilities = {}
        self.codes = {}
        self.reverse_mapping = {}

        """ Compression part """
   
    def calculate_probabilities(self):
        # reading the file 
        with open(self.input_file,"r",encoding="utf-8") as file:
            txt = file.read()
               
        total = len(txt)
        
        # Calculate the frequency of each character
        for char in txt:
            self.probabilities[char]=self.probabilities.get(char,0)+1
            
        # count the probabilities
        for char in self.probabilities:
            self.probabilities[char] /=total
        
        return self.probabilities  

    def sort_probabilities_descending(self, probabilities):
        return sorted(probabilities.items(),key = lambda item: item[1],reverse=True)
        

    def build_huffman_tree(self, sorted_probabilities):
        heap = [Node(char,freq) for char , freq in sorted_probabilities]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)

        return heap[0] if heap else None


    def generate_codes(self, tree_root):
        """
        Traverses the Huffman tree to generate binary codes for each symbol.
        """
        def generate(node,curr_code):
            if node is None:
                return
            if node.char is not None:
                self.codes[node.char] = curr_code
                self.reverse_mapping[curr_code] = node.char
                return
            generate(node.left, curr_code + "0")
            generate(node.right, curr_code + "1")

        generate(tree_root, "")
        return self.codes
            

   

    def compress(self):
        """
        Main function to perform compression:
        1. Calculate probabilities
        2. Sort descending and Build Huffman tree
        3. Generate codes
        4. Encode and save to binary file
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
