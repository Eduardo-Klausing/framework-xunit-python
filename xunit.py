# xunit.py

class TestCase:
    """
    A classe TestCase serve como a base para a criação de novos casos de teste.
    Cada método de teste em uma subclasse deve ser executado de forma independente.
    """

    def __init__(self, test_method_name):
        """
        Construtor que armazena o nome do método de teste a ser executado.
        
        :param test_method_name: O nome (string) do método de teste.
        """
        self.test_method_name = test_method_name

    def set_up(self):
        """
        Método de setup (fixture). É executado antes de cada método de teste.
        Subclasses podem sobrescrevê-lo para preparar o ambiente de teste.
        """
        pass

    def tear_down(self):
        """
        Método de teardown (fixture). É executado após cada método de teste.
        Subclasses podem sobrescrevê-lo para limpar o ambiente de teste.
        """
        pass

    def run(self):
        """
        Este é o Template Method que orquestra a execução de um teste.
        Ele garante que set_up e tear_down sejam chamados na ordem correta.
        """
        self.set_up()
        
        # getattr é usado para obter o método a partir do seu nome (string) e executá-lo.
        method = getattr(self, self.test_method_name)
        method()
        
        self.tear_down()