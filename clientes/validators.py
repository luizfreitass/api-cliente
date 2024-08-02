import re
from validate_docbr import CPF

# Validações

def cpf_valido(numero_do_cpf):
    """Verifica se o CPF é válido"""
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    """Verifica se o nome é válido"""
    return nome.isalpha()

def rg_valido(numero_do_rg):
    """Verifica se o RG é válido"""
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    """Verifica se o celular é válido (XX 9XXXX-XXXX)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_do_celular) # Verifica se o número do celular passado se enquadra no modelo
    return resposta
        