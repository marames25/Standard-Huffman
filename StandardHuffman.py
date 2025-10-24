import heapq
import json
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
        
        constructed_bytes = bytearray() 
        i = 0; pad = 0

        while (i < len(encoded_data)):
            new_byte = encoded_data[i : i+8]
            if (len(new_byte) < 8):
                pad = 8 - len(new_byte)
                new_byte += pad * '0'
            constructed_bytes.append(int(new_byte, 2))
            i += 8

        json_header = json.dumps({"codes": self.codes, "pad": pad})
        header_bytes = json_header.encode()

        with open(self.output_file, "wb") as output:
            output.write(header_bytes)
            output.write(b"\n------\n")
            output.write(constructed_bytes)



    # Decompression part
   

    def load_compressed_file(self):
        with open(self.input_file, "rb") as file:
            content = file.read()
    
        header_bytes, data_bytes = content.split(b"\n------\n", 1)
        # returns the header as a dict 
        header = json.loads(header_bytes.decode())
        pad = header["pad"]

        self.codes = header["codes"]
        for char in self.codes:
            self.reverse_mapping[self.codes[char]] = char
        
        compressed_data = ""
        for b in data_bytes:
            compressed_data += format(b, "08b")

        return compressed_data[:len(compressed_data)-pad]

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
        compressed_data = self.load_compressed_file()
        decompressed_text = self.decode_data(compressed_data)

        with open(self.output_file, "w") as output:
            output.write(decompressed_text)

def main():
    print("Welcome to Huffman Compression Program")
    print("==============================")

    while True:
        print("\nChoose an option:")
        print("1. Compress a file")
        print("2. Decompress a file")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            input_file = input("Enter the path of the file to compress: ").strip()
            output_file = input("Enter the output file name (e.g., compressed.bin): ").strip()

            try:
                huffman = HuffmanCoding(input_file, output_file)
                huffman.compress()
                print(f"File compressed successfully: {output_file}")
            except FileNotFoundError:
                print(f"Error: File \"{input_file}\" not found")
            except Exception as e:
                print(f"Compression failed: {e}")

        elif choice == "2":
            input_file = input("Enter the path of the compressed (.bin) file: ").strip()
            output_file = input("Enter the output file name (e.g., decompressed.txt): ").strip()

            try:
                huffman = HuffmanCoding(input_file, output_file)
                huffman.decompress()
                print(f"File decompressed successfully: {output_file}")
            except FileNotFoundError:
                print(f"Error: File \"{input_file}\" not found")
            except Exception as e:
                print(f"Decompression failed: {e}")

        elif choice == "3":
            print("Thanks for using the program")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
