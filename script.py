import os
from collections import Counter
import socket
import re

# Function to count words in a text file
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read().lower()
    # Keep contractions intact, and remove special characters
    text = re.sub(r"[^a-zA-Z0-9'\s]", "", text)
    words = text.split()
    word_count = len(words)
    return words, word_count

# Function to get the top 3 most frequent words
def get_top_frequent_words(words, top_n=3):
    word_freq = Counter(words)
    return word_freq.most_common(top_n)

# Function to get the IP address of the machine running the container
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Paths for text files
file1_path = '/home/data/IF.txt'
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'

# Count words in both files
words_file1, count_file1 = count_words(file1_path)
words_file2, count_file2 = count_words(file2_path)

# Grand total word count
grand_total = count_file1 + count_file2

# Get top 3 frequent words in each file
top_words_file1 = get_top_frequent_words(words_file1)
top_words_file2 = get_top_frequent_words(words_file2)

# Get IP address of the machine
ip_address = get_ip_address()

# Write results to result.txt
output_dir = '/home/data/output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'result.txt'), 'w') as result_file:
    result_file.write(f"Word count for IF.txt: {count_file1}\n")
    result_file.write(f"Word count for AlwaysRememberUsThisWay.txt: {count_file2}\n")
    result_file.write(f"Grand total word count: {grand_total}\n\n")
    
    result_file.write("Top 3 frequent words in IF.txt:\n")
    for word, freq in top_words_file1:
        result_file.write(f"{word}: {freq}\n")
    
    result_file.write("\nTop 3 frequent words in AlwaysRememberUsThisWay.txt:\n")
    for word, freq in top_words_file2:
        result_file.write(f"{word}: {freq}\n")
    
    result_file.write(f"\nIP Address of the machine: {ip_address}\n")

# Print the result file content to the console
with open(os.path.join(output_dir, 'result.txt'), 'r') as result_file:
    print(result_file.read())