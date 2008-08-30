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


def espalha (times):

    num_times = len (times)
    num_rodadas = num_times - 1
    if num_times % 2 != 0:
        num_rodadas += 1
    print "times: ", num_times, " rodadas: ", num_rodadas

    # Flags para verificar se um time ja jogou ou nao numa rodada
    flags = []
    for i in range (num_times):
        flags.append ([])

    # Rodadas em formato de texto
    rodadas = []
    for i in range (num_rodadas):
        rodadas.append ("")

    for i in range (num_times):
        r = (2 * i) % num_rodadas
        for j in range (i + 1, num_times):
            while r in flags[i]:
                r = (r + 1) % num_rodadas
            p = times[i] + " vs " + times[j] + "\n"
            rodadas[r] += p
            flags[i].append (r)
            flags[j].append (r)

    print "\n\n----------------------------------------------"
    print   "\nTABELA!!! AEEEEE LOLOLOLOL!!!!!1111111oneoneone"
    print     "----------------------------------------------\n\n"

    for i in rodadas:
        print "\nRodada: ", rodadas.index (i)
        s = i.split ("\n")
        for j in s:
            print j


if __name__ == "__main__":
    times = le_times ()
    espalha (times)
