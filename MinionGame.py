PROBLEM:
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string S.
For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

MY SOLVE:
def minion_game(string):
    # your code goes here
    Kevin=0 
    Stuart=0
    vow=[]
    
    substrings = [string[i: j] for i in range(len(string)) 
          for j in range(i + 1, len(string) + 1)] 
    #print("All substrings of string are : " + str(substrings)) 
    n = len(string)
    total=int(n * (n + 1) / 2)
    #print(total)
    for x in substrings:
      if x[0]=='A' or x[0]=='E' or x[0]=='I' or x[0]=='O' or x[0]=='U':
        #print(x)
        vow.append(x)
    
    #print(vow)
    Kevin=len(vow)
    #print(Kevin)
    Stuart=total-Kevin
    #print(Stuart)
  
    if Stuart>Kevin:
      print('Stuart', Stuart)
    elif Kevin>Stuart:
      print('Kevin', Kevin)
    else:
      print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)


