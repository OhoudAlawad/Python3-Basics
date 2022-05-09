# Project 2 #
# Count words in a sentence without Repetition


# input sentence

sent = input ("\nEnter your sentence")
  
# using split() 
# to extract words from string 

num = sent.split()
c = []
for i in num:
    if (sent.count(i)>=1 and (i not in c)):
        c.append(i)
res = len(c)        
 
print ("\nThe number of words in string is : "   + str(res))
