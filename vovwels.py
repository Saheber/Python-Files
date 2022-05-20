f = open("SampleFile.txt","r")
ch=""
vowels = ['a','A','e','E','i','I','o','O','u','U']
vcount = 0
consonants = 0
for ch in f.read():
    
    if ch in vowels:
        vcount+=1
    else:
        consonants+=1
print("Count of Vowels in the text",vcount)
print("Count of Consonants in the text is",consonants)
f.close()
    
