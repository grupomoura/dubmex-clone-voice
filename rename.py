import os

def rename(caminho, nome_atual, novo_nome):
    # Obtém o caminho completo do arquivo atual
    caminho_arquivo_antigo = os.path.join(caminho, nome_atual)
    
    # Separa o nome do arquivo da sua extensão
    nome, extensao = os.path.splitext(nome_atual)
    
    # Constrói o novo caminho com o novo nome e extensão
    caminho_arquivo_novo = os.path.join(caminho, f"{novo_nome}{extensao}")
    
    # Renomeia o arquivo
    os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
