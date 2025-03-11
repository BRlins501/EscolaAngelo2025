valor = int(input("Digiote u8m enteiro entr4e 10 e 100"))

if valor <= 10 or valor >= 100:
 print("valor inválido")
else:
    if valor % 2 == 0:
        if valor == 50:
           print("Você digitou 50")
        else:
           print("Você não digitou 50")
    else:
     print("O valor é impar")


 