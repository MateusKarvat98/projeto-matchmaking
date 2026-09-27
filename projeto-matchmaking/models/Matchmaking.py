from collections import deque
from .HashJogadores import TabelaHash
from .Jogador import Jogador, Tier
import random
import string

class Matchmaking():

    def __init__(self):
        self.tabela_hash = TabelaHash()
        self.filas = {tier: deque() for tier in Tier}     

    def entrar_na_fila(self, id_jogador):
        busca_jogador = self.tabela_hash.buscar(id_jogador)
        if busca_jogador == None:
            return 'Jogador não encontrado'
        else:
            tier_jogador = busca_jogador.tier
            fila_atual = self.filas[tier_jogador]

            if busca_jogador in fila_atual:
                return f'{busca_jogador.nick} já está na fila de espera!'

            if len(fila_atual) >= 9:
                aliados = [fila_atual.popleft() for fila in range(4)]
                aliados.append(busca_jogador)

                oponentes = [fila_atual.popleft() for fila in range(5)]
                return 'Partida encontrada!'
            else:
                fila_atual.append(busca_jogador)
                return f'Encontrando jogadores... {len(fila_atual)}/10 na fila.'

    def sair_fila(self, id_jogador):
        jogador = self.tabela_hash.buscar(id_jogador)
        if jogador is None:
            return 'Jogador não encontrado'

        fila_atual = self.filas[jogador.tier]

        if jogador in fila_atual:
            fila_atual.remove(jogador)
            return f'{jogador.nick} cancelou a busca e saiu da fila!'
        else:
            return f'{jogador.nick} não está atualmente em nenhuma fila de busca.'        

    def vitoria(self, id_jogador):
        jogador = self.tabela_hash.buscar(id_jogador)
        if jogador is None:
            return 'Jogador não encontrado'

        jogador.vitorias += 1        
        if jogador.vitorias == 10:
            jogador.vitorias = 0
            jogador.tier = jogador.tier.proximo()
            return f'PROMOÇÃO! {jogador.nick} subiu para {jogador.tier.value}!'
    
        return f'Vitória computada para {jogador.nick}! ({jogador.vitorias}/10)'                      

    def derrota(self, id_jogador):
        jogador = self.tabela_hash.buscar(id_jogador)
        if jogador is None:
            return 'Jogador não encontrado'

        jogador.vitorias -= 1
        if jogador.vitorias < 0:
            jogador.vitorias = 9
            jogador.tier = jogador.tier.anterior()
            return f'REBAIXAMENTO! {jogador.nick} caiu para {jogador.tier.value}.'

        return f'Derrota computada para {jogador.nick}. Vitórias acumuladas: {jogador.vitorias}'       
    
    def cadastrar_jogador(self, nick):
        id_aleatorio = 'PL' + ''.join(random.choices(string.digits, k=8))
        novo_jogador = Jogador(id_jogador= id_aleatorio, tier= Tier.unranked, nick= nick)
        self.tabela_hash.inserir(id_aleatorio, novo_jogador)
        return novo_jogador
    


        
         
