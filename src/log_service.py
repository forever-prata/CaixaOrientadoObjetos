from datetime import datetime
from notificacao import Notificacao

class LogService(Notificacao):
    """
    Implementação de um serviço de notificação que registra eventos em um arquivo de log.
    """

    def __init__(self, nome_arquivo="log_caixa.txt"):
        """
        Inicializa o serviço de log.

        Args:
            nome_arquivo (str): O nome do arquivo onde os logs serão salvos.
        """
        self._nome_arquivo = nome_arquivo

    def registrar_evento(self, mensagem):
        """
        Registra uma mensagem de evento no arquivo de log, com data e hora.

        Args:
            mensagem (str): A mensagem a ser registrada.
        """
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_mensagem = f"[{timestamp}] {mensagem}\n"
        
        try:
            with open(self._nome_arquivo, "a", encoding="utf-8") as arquivo:
                arquivo.write(log_mensagem)
        except IOError as e:
            print(f"Erro ao escrever no arquivo de log: {e}")

