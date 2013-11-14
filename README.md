N-Grams Zipf's law 
==================

- Generate 5 grams from corpus
- Generate long-log plot of frequency vs rank order
- Show whether 5-grams follow Zipf's law and approximate value of alpha

- Working of parse.py
    - Uses parallel processing to digest the corpus and generate the 5-gram files
    - Creates a master\_dict file that contains an inverted frequency tuple list
    - plots the freq vs rank order in log scale using the matplotlib library

- To Do
    - effectively use the multiprocessing functionality to build the
      master\_dict file the reduce part
    - try using cluster of computers, probably a cloud to digest data
