a =  float (input("Informe o valor de a:"))
b =  float (input("Informe o valor de b:"))
c =  float (input("informe o valor de c:"))

e = (b ** 2 - 4 * a * c)

x1= ((-b + e ** (1/2)) / (2 * a))

x2= ((-b - e ** (1/2)) / (2 * a))


print("resposta" ,x1)
print("resposta" , x2)

# ano bisexto
ano = int(input(":informe um ano "))
bisexto = False

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            bisexto = True
    else:
        bisexto = True

if bisexto:
    print(ano, "ano é bisexto")
else:
    print(ano, "Não é bisexto")
