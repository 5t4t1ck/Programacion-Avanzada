salario = int(input("Por favor ingrese su salario: "))
print(type(salario))

def calcularSalario(int:salario):
    global salario
    print(type(salario))
    #salario = 300
    seguro = 50
    salarioTotal = salario - seguro
    return salarioTotal

print(calcularSalario(salario))
print(type(salario))
