# Given a divisor and a bound, find the largest integer N such that:
# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.
def solution(divisor, bound):
    
    for i in range(bound, -1, -1):
        if i % divisor == 0:
            return i

# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column 
# you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, 
# assuming all seats are occupied.
def solution(nCols, nRows, col, row):
    # need rows behind me exclusive * columns to my left (inclusive)
    columns = nCols - (col - 1)
    rows = nRows - row
    return columns * rows


# n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly 
# the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. 
# Individual pieces of candy cannot be split.
def solution(n, m):
    pieces = m // n
    return n * pieces


# Given an integer n, return the largest number that contains exactly n digits.
def solution(n):
    string = ""
    
    for i in range(n):
        string += '9'
    
    result = int(string)
    
    return result


# You are given a two-digit integer n. Return the sum of its digits.
def solution(n):
    
    n = str(n)
    total = 0
    
    for digit in n:
        digit = int(digit)
        total += digit
    
    return total


# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two 
# neighboring numbers is equal (note that 0 and n - 1 are neighboring, too). Given n and firstNumber, 
# find the number which is written in the radially opposite position to firstNumber.
def solution(n, firstNumber):
    if firstNumber < (0.5 * n):
        return (n/2 + firstNumber)
    else:
        return (firstNumber - (n/2))


# One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins 
# counting the length of your ride, in minutes. Off you go to explore the neighborhood. When you finally decide to head back, 
# you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your 
# watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
# Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
def solution(n):
    hours = str(n // 60)
    minutes = str(n % 60)

    total_1 = 0
    for i in range(len(hours)):
        total_1 += int(hours[i])
    
    total_2 = 0
    for j in range(len(minutes)):
        total_2 += int(minutes[j])
    
    return total_1 + total_2


# Some phone usage rate may be described as follows:
# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down 
# to the nearest integer) you can have?
def solution(min1, min2_10, min11, s):
    minutes = 0
    
    if s < min1:
        return 0
    else:
        minutes += 1
        s = s - min1
    
    for i in range(9):
        if s > min2_10:
            minutes += 1
            s = s - min2_10
        else:
            return minutes
    
    while s >= min11:
        minutes += 1
        s = s - min11
    
    return minutes


# You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your 
# XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.
# Given values experience, threshold and reward, check if you reach the next level after killing the monster.
def solution(experience, threshold, reward):
    return experience + reward >= threshold


# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. 
# What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for 
# the items later? Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or
# two second items.
def solution(value1, weight1, value2, weight2, maxW):
    if (weight1 + weight2) <= maxW:
        return (value1 + value2)
    elif weight1 <= maxW and value1 >= value2:
        return value1
    elif weight2 <= maxW and value2 > value1:
        return value2
    elif weight1 <= maxW:
        return value1
    else:
        return 0


# You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. 
# What is the value of the third integer?
def solution(a, b, c):
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a


# Given integers a and b, determine whether the following pseudocode results in an infinite loop
# while a is not equal to b do
#   increase a by 1
#   decrease b by 1
# Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
def solution(a, b):
    if a == b:
        return False
    if a < (b - 1) and (b - a - 1) % 2 == 1:
        return False
    else:
        return True


# Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the
# four signs: +, -, * or / to obtain a correct expression.
def solution(a, b, c):
    if a+b==c or a-b==c or a*b==c or a/b==c:
        return True
    else:
        return False

    
# In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared 
# the winner unless their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.
# Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final 
# score of score1 : score2.
def solution(score1, score2):
    if (score1 != 6 and score1 != 7) and (score2 != 6 and score2 != 7):
        return False
    
    elif score1 == 6 and score2 < 5:
        return True
    
    elif score1 == 7 and score2 == 5:
        return True
    
    elif score1 == 7 and score2 == 6:
        return True
    
    elif score2 == 6 and score1 < 5:
        return True
    
    elif score2 == 7 and score1 == 5:
        return True
    
    elif score2 == 7 and score1 == 6:
        return True
    
    else:
        return False

    
# Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". 
# Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to 
# put her belief to the test. Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.
# A person contradicts Mary's belief if one of the following statements is true:
# they are young and beautiful but not loved;
# they are loved but not young or not beautiful.
def solution(young, beautiful, loved):
    
    if young and beautiful and loved:
        return False
    
    if not loved and not young:
        return False
    
    if not loved and not beautiful:
        return False
    
    if loved and not young:
        return True
    
    if loved and not beautiful:
        return True
    
    else:
        return True
    
    
# You just bought a public transit card that allows you to ride the Metro for a certain number of days. Here is how it works: upon first 
# receiving the card, the system allocates you a 31-day pass, which equals the number of days in January. The second time you pay for the 
# card, your pass is extended by 28 days, i.e. the number of days in February (note that leap years are not considered), and so on. 
# The 13th time you extend the pass, you get 31 days again. You just ran out of days on the card, and unfortunately you've forgotten 
# how many times your pass has been extended so far. However, you do remember the number of days you were able to ride the Metro during 
# this most recent month. Figure out the number of days by which your pass will now be extended, and return all the options as an array 
# sorted in increasing order.
def solution(lastNumberOfDays):
    if lastNumberOfDays == 31:
        return [28, 30, 31]
    if lastNumberOfDays == 30:
        return [31]
    if lastNumberOfDays == 28:
        return [31]


# Given an integer n, find the minimal k such that: 
# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.
def solution(n):
    if n <= 1:
        return 1
    else:
        if n <= 120 and n > 24:
            return 120
        if n <= 24 and n > 6:
            return 24
        if n <= 6 and n > 2:
            return 6
        if n == 2:
            return 2
        
        
# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.


# You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, 
# it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make?
def solution(a, b, n):
    dollars = 0
    
    while n > 0:
        dollars += (a*b)
        a += 1
        b += 1
        n -= 1
    
    return dollars


# To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them 
# up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. Alternatively, 
# when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around. Unfortunately some 
# students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when 
# they hear 'R'. The coach wants to know how many times the students end up facing the same direction. Given the list of commands the coach 
# has given, count the number of such commands after which the students will be facing the same direction. 
def solution(commands):

    count = 0
    tally = 0

    for move in commands:
        if move == "L" or move == "R":
            count += 1
        elif move == "A":
            count += 2
            
        if count % 2 == 0:
            tally += 1
    
    return tally


# A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. 
# But the child always forgets about the important part - carrying. Given two integers, your task is to find the result that the child will get.
# Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.
Need answer


# You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:
# The smallest box is size 1, the next one is size 2,..., all the way up to size k. Boxes that have an odd size contain only yellow apples. 
# Boxes that have an even size contain only red apples. Your task is to calculate the difference between the number of red apples and the 
# number of yellow apples.
def solution(k):
    
    red = 0
    yellow = 0
    
    for i in range(1, k+1):
        
        if i % 2 == 0:
            red += (i**2)
        else:
            yellow += (i**2)
    
    return red - yellow


# Define an integer's roundness as the number of trailing zeroes in it. Given an integer n, check if it's possible to increase n's 
# roundness by swapping some pair of its digits.
def solution(n):
    
    n = str(n)
    
    for i in range(len(n)-1, -1, -1):
        if n[i] != "0":
            break
    
    for j in range(i, -1, -1):
        if n[j] == "0":
            return True
    
    return False


# When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, 
# will in turn leave another leftover. You have solutionNumber solution in your possession. What's the total number of solution you can burn, 
# assuming that you create new solution as soon as you have enough leftovers?
def solution(candlesNumber, makeNew):
    
    total = 0
    leftovers = 0
    
    while candlesNumber > 0:
        total += candlesNumber
        leftovers += candlesNumber
        
        candlesNumber = leftovers // makeNew
        leftovers = leftovers % makeNew
    
    return total


# 
