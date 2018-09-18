# example to loop around a dictionary and count the occurances of every word ad alphabet in the dictionary

string = "This is an awesome occasion. This has never happened before."
a = string.count('a')
print(a)

occurances = {}
for char in string:
    occurances[char] = occurances.get(char, 0) + 1

print(occurances)

occurances_ = {}

for word in string.split():
    occurances_[word] = occurances_.get(word, 0) +1

print(occurances_)