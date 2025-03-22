# implementação do método de Newton-Raphson simples

f = lambda x: x**2 + 1

print("Digite um chute inicial:")
x0 = float(input())

inc_order = 3
h = 10**(-inc_order) # admitirá um incremento de inc_order casas após a vírgula

df = lambda x: (f(x + h) - f(x))/h # definindo derivada numérica para f

e = 8 # ordem de precisão (numero de casas após a vírgula para considerar um valor como sendo zero)
zero = 10**(-e)

x = x0 - f(x0)/df(x0)

has_zero_in_guess = True
max_iter = 100 # definindo um número máximo de iterações

if abs(df(x)) <= zero:
    has_zero_in_guess = False

for i in range(max_iter):
    if abs(df(x)) <= zero:
        print("Derivada muito pequena. Método falhou.")
        has_zero_in_guess = False
        break

    if abs(f(x)) <= zero:
        break
    else:
        x = x - f(x)/df(x)

if has_zero_in_guess:
    print("O zero da função está em %.8f" % x)
else:
    print("Não foi possível encontrar um zero na função com o chute inicial especificado")
