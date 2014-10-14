#print "How many times should the loop run?"

#total = 0

#var1 = int(raw_input())

#for x in range(var1):
    #print "What are the item prices?"
    #UserInput = int(raw_input())
    #total = total + UserInput
    
#print "The sum of the numbers is " + str(total)

#Part 2 ----------------------------------------------------

#print "How many times should the loop run?"

#totalCost = []

#var1 = int(raw_input())

#for x in range(var1):
    #print "What are the item prices?"
    #UserInput = int(raw_input())
    #totalCost.append(UserInput)
    
#print "The sum of the numbers is " + str(sum(totalCost))


#Part 3-----------------------------------------------------

#print 'What number would you like the factorial of?'

#number = int(raw_input())
#factorial = 1
#for z in range(1, number + 1, 1):
    #factorial = factorial * z
#print factorial



#Part 4-----------------------------------------------------

factors = []
print 'What number would you like to find the factorial of?'
number = int(raw_input())
count = 1

while (count < number):
    if number%count == 0:
        factors.append(count)
    count = count + 1
    print factors