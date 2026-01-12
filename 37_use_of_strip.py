# wap function to remove a give word from a list ad stript it at the same time 
def rem(l,word):
    n=[]
    for item in l:
        if item!=word:
            n.append(item.strip(word))
    return n
l=["yash","kumar"]
print(rem(l,"a"))