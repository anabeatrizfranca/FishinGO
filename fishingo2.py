def validar_telefone(telefone: str) -> bool:
#Valida se o telefone está no formato correto (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
# o "str" é usado para indicar que "telefone" = string
# bool indica que a função retorna um valor booleano (True ou False)

 apenas_numeros = "".join(c for c in telefone if c.isdigit())

#isdigit() é um método de string, uma operação que podemos executar sobre determinado tipo de objeto.
# Nesse caso, ele verifica se um caractere é numérico.

 #Ex: print("8".isdigit())
 # print("A".isdigit())
 # print("-".isdigit())

#O resultado vai ser True, True, False.

 #O if significa "se". É uma estrutura condicional. Estamos dizendo:
#"Para cada caractere do telefone, se esse caractere for um dígito, mostre-o."

#E o join no início da linha juta todos os caracteres da lista "telefone"

#A construção geral junta todos os caracteres em uma única string, validando os números e descartando símbolos de DDD.

 if len(apenas_numeros) == 10 or len(apenas_numeros) == 11:
    return True
 else:
    return False

#Len significa "length" (comprimento). Ele retorna o número de caracteres de uma string.

print ("=== QUEM É VOCÊ? ===")
print ("1 - Sou um pescador")
print ("2 - Sou uma peixaria")

opcao = int(input("Escolha uma opção:"))
match opcao:
    case 1:
        print ("Abrindo página de cadastro do pescador")

        print ("Passo 1 de 2 - Cadastro do pescador")
        nome_pescador = input("Digite seu nome: ")
        rgp_pescador = input("Digite seu RGP: ")
        if rgp_pescador == 0:
            print ("RGP inválido. Tente novamente.")
        usuário_pescador = input("Digite seu usuário: ")
        localizacao_pescador = input("Digite sua localização: ")

            # Validação do telefone
        while True:
           contato_pescador = input("Digite seu contato com DDD: ")
           if validar_telefone(contato_pescador):
              break
           else:
              print ("Telefone inválido. Tente novamente.")
        print ("Cadastro do pescador concluído!")


        print ("Passo 2 de 2 - Perfil de pesca!")
        anos_experiencia = int(input("Digite seus anos de experiência: "))
        metodo_de_pesca = input ("Selecione seu método de pesca: ")
        print ("Próximos passos: Adicione suas capturas recentes e cadastre-se com peixarias próximas!")

        print ("Agora vamos cadastrar seus pescados!")

        #próximo passo: cadastro de pescados em lote e preço por kilo e ter uma carteira com o seu saldo. O administrador da peixaria deve poder ver os lotes dos pescados, o preço e comprar.



    case 2:
        print ("Abrindo página de cadastro da peixaria")