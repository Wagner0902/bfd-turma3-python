nome = input("digite seu nome:")
idade = float(input("digite sua idade:"))

if idade <= 17:
    print("não permitiodo a entrada de menores")
elif idade > 18:
    print("permitido a entrada")
peso = float(input("digite seu peso:"))

if peso <= 80:
    print("peso permitido")
elif peso >=81:
    print("acima do peso permitido, proibida a entrada!")
    
print(nome) 
print(idade)
print("anos") 
print(peso) 
print("kilos")
