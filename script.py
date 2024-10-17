import os
from collections import Counter
import re
import socket

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    # Use regex to split words and handle contractions
    words = re.findall(r"\b\w+(?:'\w+)?\b", text.lower())
    return Counter(words)

def process_text_files():
    # File paths
    file1 = '/home/data/IF.txt'
    file2 = '/home/data/AlwaysRememberUsThisWay.txt'

    # Read files
    text1 = read_file(file1)
    text2 = read_file(file2)

    # Count words
    word_count_1 = count_words(text1)
    word_count_2 = count_words(text2)

    # Total words
    total_words_1 = sum(word_count_1.values())
    total_words_2 = sum(word_count_2.values())
    grand_total_words = total_words_1 + total_words_2

    # Top 3 words in IF.txt
    top_3_if = word_count_1.most_common(3)

    # Top 3 words in AlwaysRememberUsThisWay.txt
    top_3_arutw = word_count_2.most_common(3)

    # Get container's IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Write results to result.txt
    output_path = '/home/data/output/result.txt'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as result_file:
        result_file.write(f'Total words in IF.txt: {total_words_1}\n')
        result_file.write(f'Total words in AlwaysRememberUsThisWay.txt: {total_words_2}\n')
        result_file.write(f'Grand total of words: {grand_total_words}\n')
        result_file.write(f'Top 3 words in IF.txt: {top_3_if}\n')
        result_file.write(f'Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_arutw}\n')
        result_file.write(f'Container IP Address: {ip_address}\n')

    # Print the results to the console
    with open(output_path, 'r') as result_file:
        print(result_file.read())

if __name__ == "__main__":
    process_text_files()