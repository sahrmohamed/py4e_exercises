word =str(input("Enter a word: " ))
letter =str(input("Enter a letter to parse: "))

def count(wrd, letr):
    cnt = 0
    for char in wrd:
        if char ==letr :
            cnt = cnt + 1
    print(cnt)
count(word, letter)
