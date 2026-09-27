class TabelaHash():
    def __init__(self):
        self.tamanho = 8
        self.buckets = [[] for i in range (self.tamanho)]

    def HashConversao(self, id_jogador):
        return sum(ord(c) for c in str(id_jogador)) % self.tamanho

    def inserir(self, id_jogador, jogador):
        indice = self.HashConversao(id_jogador)

        for par in self.buckets[indice]:
            if par[0] == id_jogador:
                par[1] = jogador
                return

        self.buckets[indice].append([id_jogador, jogador])

    def buscar(self, id_jogador):
        indice = self.HashConversao(id_jogador)

        for busca in self.buckets[indice]:
            if busca[0] == id_jogador:
                return busca[1]

        return None


