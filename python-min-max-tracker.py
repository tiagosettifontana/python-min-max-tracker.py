largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try:
        # Tenta converter a entrada para inteiro
        n = int(num)
    except:
        # Se não for um número, imprime exatamente esta frase
        print("Invalid input")
        continue

    # Lógica para o maior número
    if largest is None:
        largest = n
    elif n > largest:
        largest = n
        
    # Lógica para o menor número
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n

# As frases de saída precisam ser exatamente estas
print("Maximum is", largest)
print("Minimum is", smallest)