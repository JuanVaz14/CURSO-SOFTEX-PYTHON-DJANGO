# VERIFICADOR DE SENHA

# Defina uma senha secreta em uma variael (str, por exemplo, "python123")
# Peça ao usuário para digitar uma senha.
# Use if-else para verificar se a senha digitada é igual a senha secreta. Imprima "Acesso permitido" ou "Senha incorreta"

# MENSAGEM DE SAUDAÇÃO

print("Bem vindo ao sistema")

# Define a senha correta
senha1 = "janela1206"

# Pede para o usuário digitar a senha
senha2 = input("Insira a senha: ")

# Compara as duas senhas
if senha2 == senha1:
    print("Acesso permitido")
else:
    print("Senha incorreta")