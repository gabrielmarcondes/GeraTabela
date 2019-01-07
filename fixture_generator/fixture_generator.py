from typing import Iterable


class InvalidInputException(Exception):
    pass


class FixturesGenerator:
    def __init__(self, names: Iterable[str] = None):
        self._names = names
        self._validated_names = None

    def validate(self) -> bool:
        self._validated_names = [
            name.strip()
            for name
            in self._names
            if name.strip()
        ]
        if not self._validated_names:
            raise InvalidInputException

        return True

    def generate(self):
        times = self._validated_names

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

        return {
            'first': rodadas_turno,
            'second': rodadas_returno,
        }
