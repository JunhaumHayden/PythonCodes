print("="*30)
print("      PRIMO É PARENTE")
print("="*30)
  
numero = int(input("Informe um número inteiro: "))

if numero < 2:
    print("O número não é primo.")
else:
    eh_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")
        for i in range(2, numero):
            if numero % i == 0:
                print(i)