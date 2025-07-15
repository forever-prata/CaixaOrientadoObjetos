# -*- coding: utf-8 -*-

from notificacao import Notificacao
from log_service import LogService

class CaixaEletronico:
    """
    Representa um caixa eletrônico, gerenciando o estoque de cédulas e as operações de depósito e saque.
    """

    def __init__(self):
        self._cedulas = {
            200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0
        }
        self._notificadores = []

    def adicionar_notificador(self, notificador: Notificacao):
        """
        Adiciona um serviço de notificação à lista.
        """
        if notificador not in self._notificadores:
            self._notificadores.append(notificador)

    def _notificar_evento(self, mensagem):
        """
        Dispara um evento para todos os notificadores registrados.
        """
        for notificador in self._notificadores:
            notificador.registrar_evento(mensagem)

    def get_valor_total(self):
        """
        Calcula e retorna o valor total disponível no caixa eletrônico.
        """
        total = 0
        for cedula, quantidade in self._cedulas.items():
            total += cedula * quantidade
        return total

    def depositar(self, cedulas_depositadas):
        """
        Realiza um depósito de cédulas no caixa eletrônico.
        """
        deposito_str = ", ".join([f"{qtd}x R${c}" for c, qtd in cedulas_depositadas.items()])
        for cedula, quantidade in cedulas_depositadas.items():
            if cedula in self._cedulas:
                self._cedulas[cedula] += quantidade
        
        print(f"Depósito realizado com sucesso. Novo saldo: R$ {self.get_valor_total():.2f}")
        self._notificar_evento(f"Depósito realizado: {deposito_str}")

    def sacar(self, valor):
        """
        Realiza um saque do caixa eletrônico, se possível.
        """
        #verificações iniciais de execução
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        if valor > self.get_valor_total():
            mensagem_erro = f"Erro no saque: Valor solicitado (R$ {valor:.2f}) é maior que o saldo total."
            print(f"Saque de R$ {valor:.2f} não realizado. Saldo insuficiente.")
            self._notificar_evento(mensagem_erro)
            return

        cedulas_para_saque = {}
        valor_restante = valor
        #itera sobre as cédulas da maior para a menor
        for cedula in sorted(self._cedulas.keys(), reverse=True):
            if valor_restante >= cedula:
                quantidade_necessaria = int(valor_restante // cedula)
                quantidade_disponivel = self._cedulas[cedula]
                quantidade_a_sacar = min(quantidade_necessaria, quantidade_disponivel)

                if quantidade_a_sacar > 0:
                    cedulas_para_saque[cedula] = quantidade_a_sacar
                    valor_restante -= quantidade_a_sacar * cedula
        
        #verifica se foi possível compor o valor total do saque
        if valor_restante == 0:
            #atualiza o estoque de cédulas
            for cedula, quantidade in cedulas_para_saque.items():
                self._cedulas[cedula] -= quantidade
            
            saque_formatado = ", ".join([f"{qtd}x R${c}" for c, qtd in cedulas_para_saque.items()])
            print(f"Saque de R$ {valor:.2f} realizado com sucesso: {saque_formatado}")
            print(f"Novo saldo: R$ {self.get_valor_total():.2f}")
            self._notificar_evento(f"Saque realizado: R${valor:.2f} - {saque_formatado}")
        else:
            mensagem_erro = f"Erro no saque: Não foi possível compor o valor de R${valor:.2f} com a combinação de cédulas atual."
            print(mensagem_erro)
            
            valor_sugerido = valor - valor_restante
            if valor_sugerido > 0:
                sugestao_msg = f"(Opcional): Você pode tentar sacar R$ {valor_sugerido:.2f}."
                print(sugestao_msg)
                mensagem_erro += f" Sugestão de saque alternativo: R$ {valor_sugerido:.2f}."

            self._notificar_evento(mensagem_erro)



