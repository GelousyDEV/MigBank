print("=================================")
print("          🏦 MIGBANK 🏦          ")
print("    O banco do seu futuro!      ")
print("=================================")

# 1. TELA DE CADASTRO
print("\n--- [ CADASTRO DE NOVA CONTA ] ---")
usuario_cadastrado = input("Crie seu nome de usuário: ")
senha_cadastrada = input("Crie sua senha numérica: ")

print("\n✅ Cadastro realizado com sucesso no MigBank!")
print("Agora faça o seu login para acessar a conta.\n")

# 2. TELA DE LOGIN
print("---------------------------------")
print("       LOGIN NO MIGBANK          ")
print("---------------------------------")

usuario_login = input("Digite seu usuário: ")
senha_login = input("Digite sua senha: ")

# 3. ENTRANDO NO APP
print("\n🔄 Verificando dados...")
print("🔑 Seja muito bem-vindo de volta,", usuario_login, "!")

# Saldo inicial na conta
saldo = 300

print("\n---------------------------------")
print("Conta: 1234-5 | Agência: 0001")
print("Seu saldo inicial é: R$", saldo)
print("---------------------------------")

# 4. ÁREA DE DEPÓSITO
print("\n--- [ ÁREA DE DEPÓSITO ] ---")
deposito = int(input("Quanto você deseja depositar? R$ "))
saldo = saldo + deposito
print("💵 Depósito feito! Novo saldo: R$", saldo)

# 5. ÁREA DE SAQUE
print("\n--- [ ÁREA DE SAQUE ] ---")
saque = int(input("Quanto você deseja sacar? R$ "))
saldo = saldo - saque
print("💸 Saque feito! Novo saldo: R$", saldo)

# 6. ÁREA DO PIX
print("\n--- [ ÁREA DE PIX ] ---")
chave_pix = input("Digite a chave PIX de quem vai receber: ")
valor_pix = int(input("Quanto você quer mandar no PIX? R$ "))

# Desconta o valor do PIX do saldo
saldo = saldo - valor_pix

print("⚡ PIX enviado com sucesso para a chave:", chave_pix)
print("Novo saldo após o PIX: R$", saldo)

# RESUMO FINAL
print("\n=================================")
print("       RESUMO DA SUA CONTA       ")
print("=================================")
print("Titular:", usuario_login)
print("Saldo final no MigBank: R$", saldo)
print("\nObrigado por usar o MigBank! 🚀")