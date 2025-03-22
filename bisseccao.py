# implementação simples do método da bissecção em Python

f = lambda x: x**2 - 1

print("Digite um ponto x com f(x) < 0:")
a = float(input())
print("Digite um ponto x com f(x) > 0:")
b = float(input())

mid = (a + b)/2

e = 6
zero = 10**(-e)

while(abs(f(mid)) > zero): # a comparação é com um valor não-nulo para evitar problemas de precisão numérica
    if f(mid) < 0:
        a = mid
    else:
        b = mid
    
    mid = (a + b)/2
    
print("o ponto do zero é: %.6f" % mid)