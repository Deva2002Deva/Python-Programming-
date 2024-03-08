def is_prime(num):
    if num < 2:
        return false
    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            return false
        return true
    A=int(input("enter the value of A:"))
    B=int(input("enter the value of B:"))
    non_primes=[num for num in range(A, B+1)if not is_prime(num)]
    print(", ".join(map(str, non_primes)))
    
