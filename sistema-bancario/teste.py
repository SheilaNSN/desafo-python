valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

print(f"O preço final do pedido é R${(valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)}. Seu troco é R$ {valorPago - ((valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida))} ")
