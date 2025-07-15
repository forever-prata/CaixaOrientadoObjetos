from caixa_eletronico import CaixaEletronico
from log_service import LogService

if __name__ == '__main__':
    # --- Configuração ---
    caixa = CaixaEletronico()
    log_service = LogService() # Cria o serviço de log
    caixa.adicionar_notificador(log_service) # Registra o serviço no caixa

    # --- Simulação ---
    print(f"--- Início da Simulação ---")
    print(f"Valor inicial no caixa: R$ {caixa.get_valor_total():.2f}")

    #deposito inicial
    deposito = {100: 10, 50: 5, 20: 10, 10: 5} # Total R$1000 + R$250 + R$200 + R$50 = R$1500
    print("\n--- Realizando Depósito ---")
    caixa.depositar(deposito)

    #testes de saque
    print("\n--- Testando Saques ---")
    caixa.sacar(380) # Saque normal
    print("-" * 20)
    caixa.sacar(125) # Saque que vai falhar e gerar sugestão
    print("-" * 20)
    caixa.sacar(120) # Saque da sugestão anterior
    print("-" * 20)
    caixa.sacar(2000) # Saldo insuficiente
    print("-" * 20)

    print(f"\nValor final no caixa: R$ {caixa.get_valor_total():.2f}")
    print("--- Fim da Simulação ---")
    print("\nVerifique o arquivo 'log_caixa.txt' para ver os eventos registrados.")
