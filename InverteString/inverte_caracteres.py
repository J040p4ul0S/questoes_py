def inverte(string):
    n = len(string)
    aux = ''
    for i in range(n-1, -1, -1):
        aux+=string[i]
    
    return aux
def main():
    s = input("Informe a string: ")
    print(inverte(s))

main()