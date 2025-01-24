#1. Implement a hash function that hashes a string based on the sum of its ASCII values (mod 100). Find two real english words that hash to the same thing.
#2. Finish your rubric for the Graham Scan project
#3. Get yourself a notebook you can write stuff down in and actually use it next time
def HashThis(x,mod = 100):
    combinedVal = 0
    for char in x:
        combinedVal += ord(char)
    print(combinedVal)
    return combinedVal % mod


def main():
    x = 'edit'
    print(HashThis(x))
    x = 'tide'
    print(HashThis(x))
if __name__ == "__main__":
    main()
