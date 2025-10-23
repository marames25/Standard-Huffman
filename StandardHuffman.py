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
        probabilities = self.calculate_probabilities()
        sorted_probabilities = self.sort_probabilities_descending(probabilities)
        huffman_tree_root = self.build_huffman_tree(sorted_probabilities)
        self.generate_codes(huffman_tree_root)
        
        # Encoding the data
        with open(self.input_file, "r", encoding="utf-8") as file:
            txt = file.read()
        
        encoded_data = ""
        for char in txt:
            encoded_data += self.codes[char]
        
        with open(self.output_file, "w", encoding="utf-8") as output:
            output.write(encoded_data)

        print("File compressed and saved to", self.output_file)
        print("Original size:", len(txt), "characters")
        print("Compressed size:", len(encoded_data), "bits")
        print("Compression Ratio:", len(encoded_data)/ (len(txt)*8))
        print("Huffman Codes:", self.codes)
        print("Encoded data:", encoded_data)


    # Decompression part
   

    def load_compressed_file(self):

        with open(self.input_file, "r") as file:
            compressed_data = file.read()
        return compressed_data

    def decode_data(self, bitstring):
        current_code = ""
        decoded_text = ""

        for bit in bitstring:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def save_decompressed_file(self, data):
        try :
            with open(self.output_file, "w", encoding="utf-8") as file:
                file.write(data)
        except Exception as e:
            print("Error saving decompressed file:", e)

    def decompress(self):
        """
        Main function to perform decompression:
        1. Load compressed file
        2. Decode bitstream
        3. Save decompressed text
        """
        pass
