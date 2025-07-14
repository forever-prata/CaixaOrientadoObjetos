class CaixaEletronico:
    """
    Representa um caixa eletrônico, gerenciando o estoque de cédulas e as operações de depósito e saque.
    """

    def __init__(self):

        self._cedulas = {
            200: 0,
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0
        }

    def get_valor_total(self):
        """
        Calcula e retorna o valor total disponível no caixa eletrônico.

        Returns:
            float: O valor total.
        """
        total = 0
        for cedula, quantidade in self._cedulas.items():
            total += cedula * quantidade
        return total

    def depositar(self, cedulas_depositadas):
        """
        Realiza um depósito de cédulas no caixa eletrônico.

        Args:
            cedulas_depositadas (dict): Um dicionário onde a chave é o valor da cédula e o valor é a quantidade.
        """
        for cedula, quantidade in cedulas_depositadas.items():
            if cedula in self._cedulas:
                self._cedulas[cedula] += quantidade
        
        print(f"Depósito realizado com sucesso. Novo saldo: R$ {self.get_valor_total():.2f}")


    def sacar(self, valor):
        """
        Realiza um saque do caixa eletrônico, se possível.

        Args:
            valor (float): O valor a ser sacado.
        """

        #verificações iniciais de execução
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        if valor > self.get_valor_total():
            print(f"Saque de R$ {valor:.2f} não realizado. Saldo insuficiente.")
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
        else:
            print(f"Não foi possível realizar o saque de R$ {valor:.2f} com as cédulas disponíveis.")


if __name__ == '__main__':

    caixa = CaixaEletronico()
    print(f"--- Início da Simulação ---")
    print(f"Valor inicial no caixa: R$ {caixa.get_valor_total():.2f}")

    #deposito inicial
    deposito = {100: 10, 50: 10, 20: 10, 10: 10} # R$1000 + R$500 + R$200 + R$100 = R$1800
    print("\n--- Realizando Depósito ---")
    caixa.depositar(deposito)

    #testes de saque
    print("\n--- Testando Saques ---")
    caixa.sacar(380) # funciona: 3x R$100, 1x R$50, 1x R$20, 1x R$10
    print("-" * 20)
    caixa.sacar(500) # funciona: 5x R$100
    print("-" * 20)
    caixa.sacar(125) # falha (sem notas de 5)
    print("-" * 20)
    caixa.sacar(2000) # falha (saldo insuficiente)
    print("-" * 20)

    print(f"Valor final no caixa: R$ {caixa.get_valor_total():.2f}")
    print("--- Fim da Simulação ---")
