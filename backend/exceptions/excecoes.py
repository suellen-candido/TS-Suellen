class NomeInvalidoError(Exception):
    """Lançada quando o nome do produto está vazio ou inválido."""

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ValorErradoError(Exception):
    """Lançada quando o preço do produto está vazio ou inválido."""

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg