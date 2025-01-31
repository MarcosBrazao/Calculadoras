"""Caculadora com While"""

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numval = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numval = True
    except:
        numval = None
        
    if numval is None:
            print('Um ou ambos os números digitados são inválidos!!!!')
            continue
        
    operador_permitido = '+-/*'
    
    if operador not in operador_permitido:
        print('Operador inválido!!!!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizando sua conta. Confira o resultado:')

    if operador == '+':
        print(f'{num1_float} + {num2_float} =', num1_float + num2_float)
    elif operador =='-':
        print(f'{num1_float} - {num2_float} =', num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} =', num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} =', num1_float * num2_float)
    else:
        print('Nunca deveria chegar aqui!!')

        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    