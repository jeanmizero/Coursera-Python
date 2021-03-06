# 1. Use for, .split(), and if to create a statement that will print out words that start with "s"
st = 'Sam Print only the words that start with s in the sentence'
for word in st.split():
    if word[0].lower() == "s":
        print(word)

# 2. Use range()to print all the even numbers from 0 to 10

for num in range(0, 11, 2):
    print(num)

# 3.
st = 'Print every word in the sentences that has an even number of letter'
for word in st.split():
    if len(word) %= =0:
        print(word)
