def fibonacci_seq(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verify(number):
    fibonacci = fibonacci_seq(number)
    if number in fibonacci:
        return (f"{number} pertence à sequência de Fibonacci.")
    else:
        return (f"{number} não pertence à sequência de Fibonacci.")

number = int(input("Digite um valor para verificarmos se pertence à sequência de Fibonacci: "))
print(verify(number))
