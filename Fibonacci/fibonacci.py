def fibonacci(x):
    n, m = 0, 1
    s = n+m

    if x == n or x == m or s == x:
        return True
        
    while s<x:
        #print(n, end=" ")
        n,s = s, n+s
        if s == x:
            return True
    
    return False

def main():
    x = int(input("Informe o número: "))
    print("Pertence a sequência " if fibonacci(x) else "Não petence a sequência")

main()