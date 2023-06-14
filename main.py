'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import string                        # 'import string' cauz we used string.ascii_letters 
import random                        # 'import random' cauz we used random.randint()
symbols = []                         #  empty list named symbols
symbols = list(string.ascii_letters) #  since this is from string library, so 'import string'
card1 = [0]*5                        #  empty list named card1 initialized to 5 zero's
card2 = [0]*5
pos1 = random.randint(0,4)           #  pos1 and pos2 are same symbol positions in card1 and card2
pos2 = random.randint(0,4)           #  pos2 = same symbol positions in card2
# here pos1 and pos2 will be random positions from 0 to 4 

print('random position for card1 is ',pos1)                          
print('random position for card2 is ',pos2)

#        import string 
#        print(string.ascii_letters)
# -----> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

samesymbol = random.choice(symbols)  #  character named 'samesymbol', randomly choosing from list named 'symbols'
symbols.remove(samesymbol)           # even if we choosing from the same list, card1 and card2 may have same symbols so so we used this     
                                     # becauz we dont want same symbols to repeat in card1 and card2  

if(pos1 == pos2):
    card2[pos1] = samesymbol         # card2 pos1 and card1 pos1 will have samesymbol
    card1[pos1] = samesymbol
 #  card2[pos2] = samesymbol
 #  card1[pos2] = samesymbol
else:
 #  https://in.images.search.yahoo.com/search/images;_ylt=Awrx.3e8qiBkNPsO8jm7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=dobble+game&fr2=piv-web&type=E210IN885G0&fr=mcafee#id=12&iurl=http%3A%2F%2Fwww.mumstheboss.co.uk%2Fwp-content%2Fuploads%2FDobble-puzzle.jpg&action=click
 #  visit this image for better understanding
    card1[pos1] = samesymbol        
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])      # to prevent repitations in same card
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])      # to prevent repitations in same card

 # now for the other positions in card1 and card2 other than pos1 and pos2 (offcourse not same)
i = 0
while(i<5):
    if(i != pos1 and i != pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)    # to prevent repitations in same card
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)    # to prevent repitations in same card
        card1[i] = alphabet1         # appending alphabet1 in card1 ith position
        card2[i] = alphabet2         # appending alphabet2 in card2 ith position
    i = i + 1

print('\n',card1)                    # \n just to print in another line
print(card2)

ch = input("\nspot the similar symbol : ")
if(ch == samesymbol):
    print("you guessed it right !!!")
else:
    print("heyy! sorry you are wrong here")
    

