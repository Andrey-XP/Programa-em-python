n1 = int(input('Digite um numero: '))
n2 = int(input('Outro Numero: '))
operacao = input('Escolha a operação : (+, -, *, /)')

if operacao == '+':
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
elif operacao == '-':
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
elif operacao == '*':
    resultado = n1 * n2
    print(f'{n1} * {n2} = {resultado}')
elif operacao == '/':
    if n2 == 0:
        print('Erro: divisão por zero.')
    else:
        resultado = n1 / n2
        print(f'{n1} / {n2} = {resultado}')
else:
    print('Operação inválida. Escolha entre +, -, * ou /.')
