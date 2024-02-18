import matplotlib.pyplot as plt

# Read the terms from the file
with open('terms.txt', 'r') as file:
    terms = [int(line.strip()) for line in file]

# Create stem plot
plt.stem(range(1, len(terms) + 1), terms, use_line_collection=True)

# Set y-axis limits to decrease the scale
plt.ylim(min(terms) - 5, max(terms) + 5)  # Adjust the values as needed

plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.savefig('graph.png')
