import editdistance


def find_correction(word, dictionary):
    if word in dictionary:
        return (word, 0)

    for entry in dictionary:
        if editdistance.eval(word, entry) == 1:
            return (entry, 1)

    for entry in dictionary:
        for i in range(len(word) - 1):
            new_word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
            if editdistance.eval(new_word, entry) == 1:
                return (entry, 2)

    return (None, 3)


# Load dictionary
with open("dictionary.txt", "r", encoding="utf-8") as f:
    dictionary = [line.strip() for line in f]

# Process queries
with open("queries.txt", "r", encoding="utf-8") as f:
    queries = [line.strip() for line in f]

results = []
for query in queries:
    correction, num_errors = find_correction(query, dictionary)
    if num_errors >= 3:
        results.append(f"{query} 3+")
    elif correction:
        if num_errors == 0:
            results.append(f"{query} 0")
        elif num_errors == 1:
            results.append(f"{query} 1 {correction}")
        else:
            results.append(f"{query} 2 {correction}")
    else:
        results.append(f"{query} 3+")

# Write results to file
with open("answer.txt", "w", encoding="utf-8") as f:
    for line in results:
        f.write(f"{line}\n")
