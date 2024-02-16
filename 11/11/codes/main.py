import matplotlib.pyplot as plt

# Read the terms from the file
with open('terms.txt', 'r') as file:
    terms = [int(line.strip()) for line in file]

# Create stem plot
plt.stem(range(1, len(terms) + 1), terms, use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.show()
