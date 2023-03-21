# Closure e funções que retornam outras funções;

def criar_saudacao(saudacao):
    """Criar uma saudação para alguem."""
    def saudar(nome):
        """Mostra na tela a saudação."""
        return f'{saudacao}, {nome}!'
    return saudar


saudacao_bom_dia = criar_saudacao('Boa noite')
saudacao_boa_tarde = criar_saudacao('Bom dia')
saudacao_boa_noite = criar_saudacao('Bom Noite')

print(saudacao_bom_dia('Luiz')) # Closure
print(saudacao_boa_tarde('Duda')) # Closure 
print(saudacao_boa_noite('Vitória')) # Closure 
