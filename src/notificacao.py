from abc import ABC, abstractmethod

class Notificacao(ABC):
    """
    Define a interface para os serviços de notificação de eventos do caixa eletrônico.
    """

    @abstractmethod
    def registrar_evento(self, mensagem):
        """
        Registra uma mensagem de evento.

        Args:
            mensagem (str): A mensagem a ser registrada.
        """
        pass
