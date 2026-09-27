from Jogador import Jogador, Tier
from HashJogadores import TabelaHash

tabela_hash = TabelaHash()
jogador_1 = Jogador("ID999", "KarvatPlays", Tier.desafiador)
jogador_2 = Jogador("ID1050", "Karvatinho", Tier.ferro)
tabela_hash.inserir(jogador_1.id_jogador, jogador_1)
tabela_hash.inserir(jogador_2.id_jogador, jogador_2)

resultado = tabela_hash.buscar("ID999")
print(f'Resultado: {resultado}')

resultado_invalido = tabela_hash.buscar("ID1234")
print(f'Resultado: {resultado_invalido}')