

import random
from collections import defaultdict

sample_text = input("Enter a sample text for Markov chain training: ")

def build_markov_chain(text):
    words = text.split()
    markov_chain = defaultdict(list)
    for i in range(len(words) - 1):
        markov_chain[words[i]].append(words[i + 1])
    return markov_chain

def generate_text(chain, start_word="I", length=20):
    current = start_word
    output = [current]
    for _ in range(length - 1):
        next_words = chain.get(current)
        if not next_words:
            break
        current = random.choice(next_words)
        output.append(current)
    return ' '.join(output)


chain = build_markov_chain(sample_text)
print("📢 Markov Test Output:\n")
word=input()
print(generate_text(chain, start_word=word, length=25))
