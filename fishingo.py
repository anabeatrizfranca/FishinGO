import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name('dados.json')
ESPECIES = ('Tilápia', 'Sardinha', 'Atum', 'Pescada', 'Outros')  # tupla


def dados_iniciais():
    return {'pescadores': [], 'peixarias': [], 'lotes': []}  # dicionário com listas


def carregar():
    if not ARQUIVO.exists():
        return dados_iniciais()
    try:
        with ARQUIVO.open('r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        if not isinstance(dados, dict) or any(not isinstance(dados.get(chave), list) for chave in ('pescadores', 'peixarias', 'lotes')):
            raise ValueError('Estrutura inválida no arquivo')
        return dados
    except (OSError, json.JSONDecodeError, ValueError) as erro:
        print(f'Não foi possível carregar os dados: {erro}')
        print('Corrija ou remova o arquivo dados.json antes de continuar.')
        return None


def salvar(dados):
    try:
        with ARQUIVO.open('w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        return True
    except OSError as erro:
        print(f'Erro ao salvar: {erro}')
        return False


def proximo_id(registros):
    return max((registro['id'] for registro in registros), default=0) + 1


def texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print('Campo obrigatório. Tente novamente.')


def numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if 0 < valor < float('inf'):
                return round(valor, 2)
            print('Digite um número positivo e finito.')
        except ValueError:
            print('Valor inválido. Exemplo: 12,50')


def procurar(registros, identificador):
    for registro in registros:
        if registro['id'] == identificador:
            return registro
    return None


def escolher_id(registros, nome):
    try:
        return int(input(f'ID de {nome}: '))
    except ValueError:
        print('O ID deve ser um número inteiro.')
        return None


def cadastrar_pessoa(dados, tipo):
    nome = texto_obrigatorio('Nome do pescador: ' if tipo == 'pescadores' else 'Nome da peixaria: ')
    contato = texto_obrigatorio('Contato: ')
    registro = {'id': proximo_id(dados[tipo]), 'nome': nome, 'contato': contato}
    dados[tipo].append(registro)
    if salvar(dados):
        print(f'Cadastro concluído! ID: {registro["id"]}')


def listar(dados, tipo):
    if not dados[tipo]:
        print('Nenhum registro encontrado.')
        return
    for registro in dados[tipo]:
        print(' | '.join(f'{campo}: {valor}' for campo, valor in registro.items()))


def editar_pessoa(dados, tipo):
    listar(dados, tipo)
    registro = procurar(dados[tipo], escolher_id(dados[tipo], 'cadastro'))
    if registro is None:
        print('Cadastro não encontrado.')
        return
    registro['nome'] = texto_obrigatorio('Novo nome: ')
    registro['contato'] = texto_obrigatorio('Novo contato: ')
    if salvar(dados):
        print('Cadastro atualizado.')


def excluir_pessoa(dados, tipo):
    listar(dados, tipo)
    registro = procurar(dados[tipo], escolher_id(dados[tipo], 'cadastro'))
    if registro is None:
        print('Cadastro não encontrado.')
        return
    if tipo == 'pescadores' and any(lote['pescador_id'] == registro['id'] for lote in dados['lotes']):
        print('Exclusão bloqueada: existem lotes ligados a este pescador.')
        return
    if input('Confirmar exclusão? (s/n): ').strip().lower() != 's':
        print('Cancelado.')
        return
    dados[tipo].remove(registro)
    if salvar(dados):
        print('Cadastro excluído.')


def escolher_especie():
    for indice, especie in enumerate(ESPECIES, start=1):
        print(f'{indice}. {especie}')
    while True:
        try:
            numero = int(input('Número da espécie: '))
            if 1 <= numero <= len(ESPECIES):
                return ESPECIES[numero - 1]
        except ValueError:
            pass
        print('Escolha uma das espécies da lista.')


def cadastrar_lote(dados):
    if not dados['pescadores']:
        print('Cadastre um pescador antes de criar um lote.')
        return
    listar(dados, 'pescadores')
    pescador_id = escolher_id(dados['pescadores'], 'pescador')
    if procurar(dados['pescadores'], pescador_id) is None:
        print('Pescador não encontrado.')
        return
    especie = escolher_especie()
    quantidade = numero_positivo('Quantidade (kg): ')
    preco = numero_positivo('Preço por kg (R$): ')
    origem = texto_obrigatorio('Local de captura: ')
    lote = {'id': proximo_id(dados['lotes']), 'pescador_id': pescador_id,
            'especie': especie, 'quantidade_kg': quantidade,
            'preco_kg': preco, 'origem': origem}
    print(f'Revisão do lote: {lote}')
    if input('Publicar lote? (s/n): ').strip().lower() != 's':
        print('Cadastro cancelado.')
        return
    dados['lotes'].append(lote)
    if salvar(dados):
        print('Lote cadastrado com sucesso!')


def editar_lote(dados):
    listar(dados, 'lotes')
    lote = procurar(dados['lotes'], escolher_id(dados['lotes'], 'lote'))
    if lote is None:
        print('Lote não encontrado.')
        return
    lote['especie'] = escolher_especie()
    lote['quantidade_kg'] = numero_positivo('Nova quantidade (kg): ')
    lote['preco_kg'] = numero_positivo('Novo preço por kg (R$): ')
    lote['origem'] = texto_obrigatorio('Nova origem: ')
    if salvar(dados):
        print('Lote atualizado.')


def excluir_lote(dados):
    listar(dados, 'lotes')
    lote = procurar(dados['lotes'], escolher_id(dados['lotes'], 'lote'))
    if lote is None:
        print('Lote não encontrado.')
        return
    if input('Confirmar exclusão do lote? (s/n): ').strip().lower() == 's':
        dados['lotes'].remove(lote)
        if salvar(dados):
            print('Lote excluído.')
    else:
        print('Cancelado.')


def menu():
    dados = carregar()
    if dados is None:
        return
    acoes = {
        '1': lambda: cadastrar_pessoa(dados, 'pescadores'),
        '2': lambda: listar(dados, 'pescadores'),
        '3': lambda: editar_pessoa(dados, 'pescadores'),
        '4': lambda: excluir_pessoa(dados, 'pescadores'),
        '5': lambda: cadastrar_pessoa(dados, 'peixarias'),
        '6': lambda: listar(dados, 'peixarias'),
        '7': lambda: editar_pessoa(dados, 'peixarias'),
        '8': lambda: excluir_pessoa(dados, 'peixarias'),
        '9': lambda: cadastrar_lote(dados),
        '10': lambda: listar(dados, 'lotes'),
        '11': lambda: editar_lote(dados),
        '12': lambda: excluir_lote(dados),
    }
    while True:
        print('\n=== FishinGO — MVP Acadêmico ===')
        print('PESCADORES: 1 Criar | 2 Listar | 3 Editar | 4 Excluir')
        print('PEIXARIAS:  5 Criar | 6 Listar | 7 Editar | 8 Excluir')
        print('LOTES:      9 Criar | 10 Listar | 11 Editar | 12 Excluir')
        print('0 Sair')
        opcao = input('Opção: ').strip()
        if opcao == '0':
            print('Até logo!')
            break
        acao = acoes.get(opcao)
        if acao is None:
            print('Opção inválida.')
        else:
            acao()


if __name__ == '__main__':
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print('\nEncerrado.')
