# Análise e Projeto de Algoritmos
# AC1: Ciência da Computação
#
# Email Impacta: bruno.albertino@aluno.faculdadeimpacta.com.br

def somatorio(n):
    if n==0:
        return (n)
    else:
        return n + somatorio(n-1)

	pass

def potencia_de_2(n):
    if (n==1):
        return True
    elif n % 2==1:
        return False
    else:
        return potencia_de_2(n//2)

	pass

def qtd_digitos(n):
    if (n==1):
        return 1
    else:
      if n >= 1:
        return 1 + qtd_digitos(n//10)
      else:
        return 0

	pass


def soma_digitos(n):
    if n < 10:
        return n
    else:
      if n >= 1:
        return n % 10 + soma_digitos(n//10)
      else:
        return 0

	pass

def soma_lista(lista, i):
    if (i - 1) == len(lista) -1:
        return 0

    if i == len(lista) - 1:
        return lista[i]
        return lista[i] + soma_lista(lista,i + 1)
    else:
        return lista[i] + soma_lista(lista, i + 1)

	pass


