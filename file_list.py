import os

files_list = []

def file_list(folder_path):
    files_list = []
    # Percorre todos os itens na pasta
    for filename in os.listdir(folder_path):
        # Verifica se é um arquivo (ignora diretórios)
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Adiciona o nome do arquivo à lista
            files_list.append(filename)
    
    # Ordena a lista de arquivos numericamente
    files_list.sort(key=lambda x: float(x.split('-')[0]))
    
    return files_list
