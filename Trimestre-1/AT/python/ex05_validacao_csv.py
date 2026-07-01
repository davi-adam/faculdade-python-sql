# Exercício 5 - Funções de Strings
#
# Uma equipe de TI precisa validar registros de um CSV de contatos antes de
# integrá-los ao CRM. Valide CEP (8 dígitos), nome (dois nomes com maiúscula),
# e-mail (padrão básico, iniciando com o primeiro nome, domínio permitido) e
# telefone (formatos aceitos). Exiba um relatório por registro com os erros
# encontrados enumerados.

dados_csv = [
    "12345678,Ana Silva,ana@empresa.com.br,(21) 91234-5678",
    "87654321,Joao,joao123@gmail.com,(21) 1234-567",
    "11223344,Maria Souza,maria@universidade.edu.br,(11) 93456-7890",
    "99887766,Carlos Lima,carlos@empresa.org,(31) 98888-7777",
    "44556677,Pedro Alves,pedro@empresa.com,(85) 3333-2222"
]

dominios_proibidos = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
dominios_permitidos = [".com", ".com.br", ".edu.br"]

def validar_cep(cep):
    return len(cep) == 8 and cep.isdigit()

def validar_nome(nome):
    partes = nome.split(" ")
    if len(partes) < 2:
        return False
    for parte in partes:
        if not parte[0].isupper():
            return False
    return True

def validar_email(email, nome):
    erros = []
    primeiro_nome = nome.split(" ")[0].lower()
    arroba = email.find("@")

    if arroba == -1:
        erros.append("E-mail inválido (sem @)")
        return erros

    prefixo = email[:arroba]
    dominio = email[arroba + 1:]

    if not prefixo.startswith(primeiro_nome):
        erros.append("E-mail não inicia com o primeiro nome")

    dominio_proibido = False
    for d in dominios_proibidos:
        if dominio == d:
            erros.append(f"Domínio de e-mail proibido ({dominio})")
            dominio_proibido = True
            break

    if not dominio_proibido:
        permitido = False
        for d in dominios_permitidos:
            if dominio.endswith(d):
                permitido = True
                break
        if not permitido:
            erros.append(f"Domínio de e-mail não permitido ({dominio})")

    return erros

def validar_telefone(tel):
    if not tel.startswith("(") or tel[3] != ")":
        return False
    ddd    = tel[1:3]
    numero = tel[5:].strip()
    if not ddd.isdigit():
        return False
    partes = numero.split("-")
    if len(partes) != 2:
        return False
    prefixo, sufixo = partes
    if len(sufixo) != 4 or not sufixo.isdigit():
        return False
    if len(prefixo) == 5 and prefixo[0] == "9" and prefixo[1:].isdigit():
        return True
    if len(prefixo) == 4 and prefixo.isdigit():
        return True
    return False

erros_gerais = []

for linha in dados_csv:
    campos  = linha.split(",")
    cep     = campos[0]
    nome    = campos[1]
    email   = campos[2]
    telefone = campos[3]
    erros   = []

    if not validar_cep(cep):
        erros.append("CEP inválido")
    if not validar_nome(nome):
        erros.append("Nome incompleto")

    erros += validar_email(email, nome)

    if not validar_telefone(telefone):
        erros.append("Telefone inválido")

    print(f"Registro: {linha}")
    if erros:
        print("Erros:")
        for i, erro in enumerate(erros, 1):
            print(f"  {i}) {erro}")
        erros_gerais.append(erros)
    else:
        print("Validação: OK")
    print()