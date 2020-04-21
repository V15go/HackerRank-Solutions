from collections import Counter
a=input()
ASS=a.lower()
if len(Counter(ASS))==27:
    print("pangram")
else:
    print("not pangram")





