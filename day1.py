# Exercise 1
n = int(input("Enter value of n: "))

print(f"1. This is multiplication table of {n}:")
for i in range (1, 11):
    print(f"{n} x {i} = {n*i}")

# Exercise 2 --> Need to practice more
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"2.1 Is {n} a prime: {is_prime(n)}")

print("2.2 Prime numbers between 2 and 50:", end=" ")
for i in range(2, 51):
    if is_prime(i):
        print(f"{i}", end=" ")

# Exercise 3
def sum_to1(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

print(f"\n3.1 Sum (way 1 - manual) from 1 to {n} is: {sum_to1(n)}")

def sum_to2(n):
    sum = n*(n+1)/2
    return int(sum)

print(f"3.2 Sum (way 2 - formular) from 1 to {n} is: {sum_to2(n)}")
# Way 2 is more optimized because its time complexity is O(1) meanwhile the time complexity of Way 1 is O(n)

# Exercise 4 --> Need to practice more
print("4.FizzBuzz exercise ---", end=" ")
def fizzbuzz(n):
    for i in range (1, n+1):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(f"{i}", end=" ")

fizzbuzz(n)

# Exercise 5 --> Need to practice more
def manual_count(string, char):
    count = 0

    for c in string:
        if c == char:
            count +=1

    return count

text = input("\nEnter text: ")
letter = input("Enter letter which is needed to count: ")
print(f"5. Counting frequency of letter {letter} in text: {manual_count(text, letter)}")
