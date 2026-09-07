def factorial(n):
    if n< 0:
        raise ValueError("Factorial not defined for the negative values.")
    result = 1
  for i in range(2, n + 1):
       result *= i
  return result 

 if __name__ == "__main__":
     num = 5
   print(f"Factorial of {num} is {factorial(num)}")
