
from validate_docbr import CPF

def valide_cpf(cpf_form):
    cpf = CPF()
    cpf.validate(cpf_form)
    return not cpf

