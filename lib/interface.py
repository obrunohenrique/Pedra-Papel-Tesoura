def linha(tam = 40):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt}'.center(40))
    linha()

def reinicio():
    from time import sleep
    cabecalho('Aguarde o retorno...')
    sleep(1)