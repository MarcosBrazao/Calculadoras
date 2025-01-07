# Função para somar dois números
def somar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    return a / b

# Obter os números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Obter a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Calcular o resultado
if operacao == "+":
    resultado = somar(numero1, numero2)
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
elif operacao == "*":
    resultado = multiplicar(numero1, numero2)
elif operacao == "/":
    resultado = dividir(numero1, numero2)
else:
    resultado = "Operação inválida."

# Imprimir o resultado
print(f"O resultado é: {resultado}")
