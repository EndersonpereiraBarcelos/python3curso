# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar - [S]air ')
# senha_digitada = input('Senha: ')
# # print(entrada)
senha_permitida = '123456'
# acesso = senha_digitada == senha_permitida

# if (entrada == 'E' or entrada == 'e') and acesso:
#     print('Entrar')
# else:
#     print('Sair')

# senha = input('Senha: ') or 'Sem senha'
# print(senha)

# print(True or False)
# print(True or True)


#Not inverte a expressão assim tornando mais rápido a verificação
# Quando usar no if inverter os valores dele para funcionar

senha = input('Senha: ')

if not senha == senha_permitida:
    print('Cadê a senha?')
else:
    print('Entrou')