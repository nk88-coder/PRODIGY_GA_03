# PRODIGY_GA_03
# Markov Chain Text Generator (Internship Task)

This Python script builds a simple **first-order Markov chain** from input text and generates new text sequences based on the learned word transitions. It’s a basic NLP project showcasing stochastic text generation using historical word patterns.

---

## 🧠 What It Does

- Takes a user-provided text sample (any paragraph or sentence)
- Builds a word-level Markov chain where each word maps to a list of possible next words
- Randomly generates a new sentence using the Markov chain

---

## 📌 How It Works

1. The input text is split into words.
2. A dictionary is created where each word points to a list of possible next words based on the original order.
3. Starting from a seed word (default: `"I"`), new words are randomly selected using the chain to generate a pseudo-random sentence.

---

## 📝 Example

**Input:**
