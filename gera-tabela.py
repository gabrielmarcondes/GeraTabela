from gerador import *

def le_times ():
    print "\nInsira nomes dos times separados por virgulas:\n"
    times = raw_input ()
    return times.split (',')


def imprime (turno):
    print "\n\n_______________________________________________"
    print   "\nTABELA!!! AEEEEE LOLOLOLOL!!!!!1111111oneoneone"
    print     "-----------------------------------------------\n\n"

    i = 1
    for turno in tabela:
        for rodada in turno:
            print "\nRodada: ", i
            s = rodada.split ("\n")
            i += 1
            for j in s:
                print j
            


if __name__ == "__main__":
    times = le_times ()
    times = valida_lista (times)
    tabela = espalha (times)
    imprime (tabela)
