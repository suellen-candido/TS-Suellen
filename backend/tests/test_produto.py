import backend.entity.produto
import pytest
from backend.exceptions.excecoes import NomeInvalidoError, ValorErradoError

def test_1_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == 3 and cafe._codigo_barras == 1234567890 and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_2_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(NomeInvalidoError):
        backend.entity.produto.Produto("", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_3_criar_produto_sem_preco():
    """Garante que o Produto rejeite um preço vazio."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", None, 50, 3, 1234567890, "alimenticio", 250)

def test_4_criar_produto_sem_quantidade():
    """Garante que o Produto rejeite uma quantidade em estoque vazia."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, None, 3, 1234567890, "alimenticio", 250)

def test_5_criar_produto_sem_validade():
    """Garante que o Produto rejeite uma validade vazia."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, None, 1234567890, "alimenticio", 250)

def test_6_criar_produto_sem_codbarras_():
    """Garante que o Produto rejeite um código de barras vazio."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, None, "alimenticio", 250)

def test_7_criar_produto_sem_categoria():
    """Garante que o Produto rejeite uma categoria vazia."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "", 250)

def test_8_criar_produto_sem_peso():
    """Garante que o Produto rejeite um peso vazio."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", None)

def test_9_criar_produto_com_todos_campos_validos():
    """Garante que o Produto seja criado com todos os campos válidos."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto._nome == "cafe"
    assert produto._preco == 18
    assert produto._quant_estoque == 50
    assert produto._validade == 3
    assert produto._codigo_barras == 1234567890
    assert produto._categoria == "alimenticio"
    assert produto._peso == 250

def test_10_criar_produto_com_nome_invalido():
    """Garante que o Produto rejeite um nome inválido."""
    with pytest.raises(NomeInvalidoError):
        backend.entity.produto.Produto("   ", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_11_criar_produto_com_preco_invalido():
    """Garante que o Produto rejeite um preço inválido."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", -5, 50, 3, 1234567890, "alimenticio", 250)

def test_12_criar_produto_com_quantidade_invalida():
    """Garante que o Produto rejeite uma quantidade em estoque inválida."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, -10, 3, 1234567890, "alimenticio", 250)

def test_13_criar_produto_com_validade_invalida():
    """Garante que o Produto rejeite uma validade inválida."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, -1, 1234567890, "alimenticio", 250)

def test_14_criar_produto_com_codigo_barras_invalido():
    """Garante que o Produto rejeite um código de barras inválido."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, -1234567890, "alimenticio", 250)

def test_15_criar_produto_com_categoria_invalida():
    """Garante que o Produto rejeite uma categoria inválida."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "   ", 250)

def test_16_criar_produto_com_peso_invalido():
    """Garante que o Produto rejeite um peso inválido."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", -250)  

def test_17_criar_produto_com_nome_none():
    """Garante que o Produto rejeite um nome None."""
    with pytest.raises(NomeInvalidoError):
        backend.entity.produto.Produto(None, 18, 50, 3, 1234567890, "alimenticio", 250)
def test_18_criar_produto_com_categoria_none():
    """Garante que o Produto rejeite uma categoria None."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, None, 250)

def test_19_criar_produto_com_codigo_barras_none():
    """Garante que o Produto rejeite um código de barras None."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, None, "alimenticio", 250)

def test_20_criar_produto_com_peso_none():
    """Garante que o Produto rejeite um peso None."""
    with pytest.raises(ValueError):
        backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", None)
def test_21_getter_nome():
    """Garante que o getter de nome retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.nome == "cafe"

def test_22_setter_nome_valido():
    """Garante que o setter de nome atualize o valor com um nome válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.nome = "acucar"
    assert produto.nome == "acucar"

def test_23_setter_nome_invalido():
    """Garante que o setter de nome rejeite um nome inválido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(NomeInvalidoError):
        produto.nome = "   "

def test_24_getter_preco():
    """Garante que o getter de preço retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.preco == 18

def test_25_setter_preco_valido():
    """Garante que o setter de preço atualize o valor com um preço válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.preco = 25
    assert produto.preco == 25

def test_26_setter_preco_invalido():
    """Garante que o setter de preço rejeite um preço negativo."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.preco = -10

def test_27_getter_quant_estoque():
    """Garante que o getter de quantidade em estoque retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.quant_estoque == 50

def test_28_setter_quant_estoque_valido():
    """Garante que o setter de quantidade em estoque atualize o valor com um valor válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.quant_estoque = 100
    assert produto.quant_estoque == 100

def test_29_setter_quant_estoque_invalido():
    """Garante que o setter de quantidade em estoque rejeite um valor negativo."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.quant_estoque = -5

def test_30_getter_validade():
    """Garante que o getter de validade retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.validade == 3

def test_31_setter_validade_valido():
    """Garante que o setter de validade atualize o valor com um valor válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.validade = 6
    assert produto.validade == 6

def test_32_setter_validade_invalido():
    """Garante que o setter de validade rejeite um valor negativo."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.validade = -1

def test_33_getter_codigo_barras():
    """Garante que o getter de código de barras retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.codigo_barras == 1234567890

def test_34_setter_codigo_barras_valido():
    """Garante que o setter de código de barras atualize o valor com um valor válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.codigo_barras = 9876543210
    assert produto.codigo_barras == 9876543210

def test_35_setter_codigo_barras_invalido():
    """Garante que o setter de código de barras rejeite um valor negativo."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.codigo_barras = -123

def test_36_getter_categoria():
    """Garante que o getter de categoria retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.categoria == "alimenticio"

def test_37_setter_categoria_valido():
    """Garante que o setter de categoria atualize o valor com um valor válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.categoria = "bebida"
    assert produto.categoria == "bebida"

def test_38_setter_categoria_invalido():
    """Garante que o setter de categoria rejeite uma categoria vazia."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.categoria = "   "

def test_39_getter_peso():
    """Garante que o getter de peso retorne o valor correto."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert produto.peso == 250

def test_40_setter_peso_valido():
    """Garante que o setter de peso atualize o valor com um valor válido."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.peso = 500
    assert produto.peso == 500

def test_41_setter_peso_invalido():
    """Garante que o setter de peso rejeite um valor negativo."""
    produto = backend.entity.produto.Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    with pytest.raises(ValueError):
        produto.peso = -1

def test_42_nome_invalido_error_armazena_mensagem():
    """Garante que a exceção armazene a mensagem passada no construtor."""
    erro = NomeInvalidoError("Nome não pode ser vazio")
    assert erro.msg == "Nome não pode ser vazio"

def test_43_nome_invalido_error_e_excecao():
    """Garante que NomeInvalidoError seja uma subclasse de Exception."""
    assert issubclass(NomeInvalidoError, Exception)

def test_44_nome_invalido_error_pode_ser_levantada():
    """Garante que a exceção possa ser levantada e capturada normalmente."""
    with pytest.raises(NomeInvalidoError):
        raise NomeInvalidoError("erro qualquer")

def test_45_nome_invalido_error_str_retorna_mensagem():
    """Garante que str(erro) retorne a mensagem de erro."""
    erro = NomeInvalidoError("Nome não pode ser vazio")
    assert str(erro) == "Nome não pode ser vazio"

def test_46_nome_invalido_error_mensagem_diferente():
    """Garante que a mensagem seja preservada mesmo variando o conteúdo."""
    erro = NomeInvalidoError("Nome inválido: contém apenas espaços")
    assert erro.msg == "Nome inválido: contém apenas espaços"

def test_47_valor_errado_error_armazena_mensagem():
    """Garante que a exceção armazene a mensagem passada no construtor."""
    erro = ValorErradoError("Preço não pode ser vazio")
    assert erro.msg == "Preço não pode ser vazio"

def test_48_valor_errado_error_e_excecao():
    """Garante que ValorErradoError seja uma subclasse de Exception."""
    assert issubclass(ValorErradoError, Exception)

def test_49_valor_errado_error_pode_ser_levantada():
    """Garante que a exceção possa ser levantada e capturada normalmente."""
    with pytest.raises(ValorErradoError):
        raise ValorErradoError("erro qualquer")

def test_50_valor_errado_error_str_retorna_mensagem():
    """Garante que str(erro) retorne a mensagem de erro."""
    erro = ValorErradoError("Preço não pode ser vazio")
    assert str(erro) == "Preço não pode ser vazio"

def test_51_valor_errado_error_mensagem_diferente():
    """Garante que a mensagem seja preservada mesmo variando o conteúdo."""
    erro = ValorErradoError("Preço não pode ser negativo")
    assert erro.msg == "Preço não pode ser negativo"