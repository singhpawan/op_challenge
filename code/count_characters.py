# Count the character frequency of the letters in Resume

import pandas as pd
from ggplot import *
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Plot the histogram and the character count for the resume
def get_character_frequency(file):
    text = open(file).read().lower()
    count = Counter()
    for i in range(len(text)):
        c = text[i]
        if c in "abcdefghijklmnopqrstuvwxyz":
            count[c] += 1
    count = dict(count)
    labels = []
    values = []
    for k,v in count.items():
        labels.append(k)
        values.append(v)
    pos = np.arange(len(labels))
    width = 1.0
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(labels)
    ax.set_title('Histogram of frequency of characters in Resume')
    ax.set_xlabel('characters')
    ax.set_ylabel('Frequency of Characters')
    plt.bar(pos, values, width, color='r')
    plt.show()
    print count

    return count

# Take the input file and call the get_character_frequency function 
def main():
    file = sys.argv[1]
    get_character_frequency(file)

# Boiler Plate code to call the main function
if __name__ == '__main__':
    main()
