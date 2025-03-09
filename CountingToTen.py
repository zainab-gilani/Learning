# App for Toddlers and Old people with dementia to help them memorize and learn counting 1 to 10
#
# It'll start by saying, okay let's start counting. What's the next number after 1?
#
# The user must enter 2 and hit return. If the number given is not 2, keep asking
# When the correct number is given, we then say "Good! What comes next?" and then our code should check for the next expected number and so on
# till 10

START = 1
COUNT = 9
LIMIT = START + COUNT

def ask(next_num):
    '''
    Asks user for number until it matches next_num
    :param next_num: The expected number
    :return: None
    '''
    i = next_num - 1
    num = -1

    while num != next_num:
        num = int(input(f"enter num pls after {i}: "))
        if num != next_num:
            print("NO")
        else:
            print("YES")
            break
        #endif
    #endwhile
#enddef

print("Welcome!!")
print(f"Today we are going to learn how to count to {LIMIT} !!! yayyyyy !!!")

for i in range(START+1, LIMIT+1):
    ask(i)
#endfor