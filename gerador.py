"""
LICENSE

Essa porra eh GPL.
Qualquer uma, caraio.
"""


def le_times ():
    times = []
    nome_time = "foo"
    print "Insira nomes dos times. Digite \"fim\" para parar:\n"
    while nome_time != "fim":
        nome_time = raw_input ()
        if nome_time != "fim":
            times.append (nome_time)
    num_times = len (times)
    return times


def espalha (times, returno):

    num_times = len (times)
    num_rodadas = num_times - 1
    if num_times % 2 != 0:
        num_rodadas += 1

    # Flags para verificar se um time ja jogou ou nao numa rodada
    flags = []
    for i in range (num_times):
        flags.append ([])

    # Rodadas em formato de texto
    rodadas_turno = []
    rodadas_returno = []
    for i in range (num_rodadas):
        rodadas_turno.append ("")
        rodadas_returno.append ("")
    
    mandante = True

    for i in range (num_times):
        r = (2 * i) % num_rodadas
        for j in range (i + 1, num_times):
            while r in flags[i]:
                r = (r + 1) % num_rodadas
            p_manda = times[i] + " vs " + times[j] + "\n"
            p_visita = times[j] + " vs " + times[i] + "\n"

            if mandante:
                rodadas_turno[r] += p_manda
                rodadas_returno[r] += p_visita
            else:
                rodadas_turno[r] += p_visita
                rodadas_returno[r] += p_manda
                
            flags[i].append (r)
            flags[j].append (r)
            mandante = not mandante

    print "\n\n-----------------------------------------------"
    print   "\nTABELA!!! AEEEEE LOLOLOLOL!!!!!1111111oneoneone"
    print     "-----------------------------------------------\n\n"

    for i in rodadas_turno:
        print "\nRodada: ", rodadas_turno.index (i) + 1
        s = i.split ("\n")
        for j in s:
            print j
    
    if returno:
        for i in rodadas_returno:
            print "\nRodada: ", rodadas_returno.index (i) + num_rodadas + 1
            s = i.split ("\n")
            for j in s:
                print j        
        


if __name__ == "__main__":
    times = le_times ()
    espalha (times, True)
