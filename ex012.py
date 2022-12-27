#Desafio 11 
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a 
#pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado
print("Digite a quantidade de dias alugados e km rodados para saber o valor a ser pago")
d = int(input("Dias alugados: "))
km = float(input("Km rodados: "))
gd = d * 60 
gkm = km * 0.15
vt = gd + gkm 
print("Foi gasto R${} com os dias alugados e R${} por km rodados. O valor total a ser pago é de R${}".format(gd, gkm, vt))