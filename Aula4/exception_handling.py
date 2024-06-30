# try / except


def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("Erro: Divisão por Zero")
    except TypeError:
        print("Erro: Tipos de dados inválidos.")
    else:
        print("Resultado:", resultado)
    finally:
        print("Operação Concluída")


print("-------------")
dividir(10, 2)
print("-------------")
dividir(10, 0)
print("-------------")
dividir(10, "a")
print("-------------")
