# implementação simples do método da bissecção em Python

f = lambda x: x**2 - 1 # altere a função desejada aqui

print("Digite um ponto x com f(x) < 0:")
a = float(input())
print("Digite um ponto x com f(x) > 0:")
b = float(input())

mid = (a + b)/2

e = 6
zero = 10**(-e)

while(abs(f(mid)) > zero): # a comparação é uma inequação para evitar problemas de precisão numérica. Trata-se de uma medição de proximidade ao zero real.
    if f(mid) < 0:
        a = mid
    else:
        b = mid
    
    mid = (a + b)/2

    if f(a)*f(b) > 0:
        print("Não foi possível encontrar o zero da função com os pontos especificados")
        break

    
print("o ponto do zero é: %.6f" % mid)
