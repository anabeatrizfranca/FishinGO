def validar_telefone(telefone: str) -> bool:
#Valida se o telefone está no formato correto (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
   
   apenas_numeros "".join(c for c in telefone if c.isdigit())

print ("=== QUEM É VOCÊ? ===")
print ("1 - Sou um pescador")
print ("2 - Sou uma peixaria")

opcao = int(input("Escolha uma opção:"))
match opcao:
    case 1:
        print ("Abrindo página de cadastro do pescador")

        print ("Passo 1 de 3 - Cadastro do pescador")
        nome_pescador = input("Digite seu nome: ")
        rgp_pescador = input("Digite seu RGP: ")
        if rgp_pescador == 0:
            print ("RGP inválido. Tente novamente.")
        usuário_pescador = input("Digite seu usuário: ")
        localizacao_pescador = input("Digite sua localização: ")
        contato_pescador = input("Digite seu contato com DDD: ")
        print ("Cadastro do pescador concluído!")
        print ("Próximos passos: Adicione suas capturas recentes e cadastre-se com peixarias próximas!")



    case 2:
        print ("Abrindo página de cadastro da peixaria")