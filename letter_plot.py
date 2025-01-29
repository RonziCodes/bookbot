import matplotlib.pyplot as plt

def plot_letter_counts(letter_counts):
    letters, counts = zip(*sorted(letter_counts.items(), key=lambda x: x[1], reverse=True))
    
    plt.bar(letters, counts, color='blue')
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequency in Frankenstein")
    plt.show()

plot_letter_counts(letter_counts)
