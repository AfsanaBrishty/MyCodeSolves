'''PROBLEM:
Given an integer,n,print the following values for each integer i from 1 to n:
1.Decimal
2.Octal
3.Hexadecimal (capitalized)
4.Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of n. 

MY SOLVE: '''
def print_formatted(number):
    # your code goes here
    w = len(format(number, 'b'))
    
    for x in range(1,number+1):
        a1=(str(x).rjust(w))
        a2= (oct(x).lstrip("0o").rjust(w))
        a3=(hex(x).lstrip("0x").upper().rjust(w))
        a4=(bin(x).replace("0b", "").rjust(w))
        print(a1,a2,a3,a4)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)