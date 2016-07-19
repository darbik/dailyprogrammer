# Daily Programmer Easy Challenge 270 https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text/

word1= list(raw_input("First word: "))
word2 = list(raw_input("Second word: "))

if len(word1) < len(word2):     # to make sure zip() works properly, lengths needs to be equal 

    while len(word1) < len(word2):

        word1.append(' ')

else:

    while len(word1) > len(word2):

        word2.append(' ')

for x, y in zip(range(len(word1)), range(len(word2))):

    print word1[x], word2[y]

    
