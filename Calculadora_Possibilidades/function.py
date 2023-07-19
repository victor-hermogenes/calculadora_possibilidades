
def regrade3():
    valor1 = int(input("Diga qual o valor primário: "))
    valor2 = int(input("Por quanto o valor primário deve ser multiplicado? "))
    valor3 = int(input("Por quanto o valor multiplicado deve ser dividido? "))
    fazer_regra = valor1 * valor2 / valor3

    return fazer_regra


print(regrade3())
