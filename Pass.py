from prettytable import PrettyTable

tabela = PrettyTable(["Usuário", "Senha"])

def newuser():
    createuser = input("Crie um usuário: ")
    createpassw = input("Crie uma senha: ")
    account = (createuser, createpassw)
    tabela.add_row([createuser, createpassw])

newuser()
print(tabela)

