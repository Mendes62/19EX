numero = int(input('digite o valor da compra'))
desconto = numero*0.1
if numero > 100:
    print(f'o valor e {numero-desconto} ')
else:
    print(f"o valor e {numero}")


