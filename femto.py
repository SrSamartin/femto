import os
import shutil
import platform
import socket
import psutil
import subprocess
from datetime import datetime
import getpass
import time
import random
import string

# Cabeçalho e Menu

print(""" Bem-vindo ao...
 _______   _______   __  __    _______    _______ 
|  _____| |  _____| |  \/  |  |__   __|  /  ____ |
| |       | |___    | \  / |     | |    |  |    | |
| |___    | |___|   | |\/| |     | |    |  |    | |
|  ___|   | |____   | |  | |     | |    |  |____| |
|_|       |______|  |_|  |_|     |_|     \_______/ 

1. Fazer diagnóstico completo
2. Ver uso de CPU/RAM/Disco
3. Ver IP e status da rede
4. Testar velocidade da internet
5. Limpeza do Sistema
6. Gerar senha segura
0. Sair
""")
resposta = input('Escolha uma opção: ')

# Função 1 - Diagnóstico Completo da Máquina
if resposta == '1':
    def diagnostico_completo():

        #Usuário e Sistema
        user = getpass.getuser() # Guarda o username da maquina na variavel
        so = platform.system() # Guarda o sistema operacional da maquina na variavel
        versao = platform.version() # Guarda a versão do sistema operacional na variavel
        print(f'Usuário: {user}') # Exibe usuario
        print(f'Sistema Operacional: {so} - Versão: {versao}') # Exibe SO detalhado

        # Uso da CPU
        cpu = psutil.cpu_percent(interval=1) # Guarda quantidade de uso da CPU na variavel
        print(f'Uso da CPU: {cpu}%') # Exibe conteudo da variavel

        # Uso da memória

        ram = psutil.virtual_memory() # Guarda quantidade de uso da RAM numa variavel
        print(F'RAM usada: {ram.used // (1024**2 )} / MB {ram.total // 1024**2} MB {ram.percent}%') # Exibe conteúdo da variável
        
        # Espaço em disco

        disco = shutil.disk_usage('C:/') # Obtém informações de uso do disco a partir da raiz (C:/)
        usado = disco.used // (1024**2) # Guarda numa variável a quantidade usada do armazenamento
        total = disco.total // (1024**2) # Armazena a capacidade total do disco
        print(f'Espaço em disco: {usado} MB usados de {total} MB ({usado / total * 100:.2f}%)') # exibe todas as informações tratadas

        # Ip local
        hostname = socket.gethostname()
        try:
            ip_local = socket.gethostbyname(hostname)
        except:
            ip_local = "Não disponível."
        print(f'IP local: {ip_local}')

        # Status da rede - Interfaces ativas
        interfaces = psutil.net_if_addrs()
        print('\nInterfaces de Rede:')
        for interface_name, addresses in interfaces.items():
            print(f'    {interface_name}:')
            for addr in addresses:
                if addr.family == socket.AF_INET:
                    print(f'    IPv4: {addr.address}')
                elif addr.family == socket.AF_INET:
                    print(f'    IPv6: {addr.address}')
    diagnostico_completo()
    print('\nDiagnóstico Concluído!\n')


# Verifica status de CPU, RAM e Armazenamento

if resposta == '2':
    def cpu_ram_disco():
        
        print('\n[cpu_ram_disco]\n')
        cpu_ram_disco()

        # Uso da CPU
        cpu = psutil.cpu_percent(interval=1)
        print(f'Uso da CPU: {cpu}%')

        # Uso da memória

        ram = psutil.virtual_memory()
        print(F'RAM usada: {ram.used // (1024**2 )} / MB {ram.total // 1024**2} MB {ram.percent}%')
        
        # Espaço em disco

        disco = shutil.disk_usage()
        usado = disco.used // (1024**2)
        total = disco.total // (1024**2)
        print(f'Espaço em disco: {usado} GB usados de {total} GB ({usado / total * 100:.2f}%)')
    cpu_ram_disco()

# Verifica Status da Conexão

if resposta == '3':
    print('\n[ver_ip_statusRede]\n')

    def ver_ip_statusRede():
     # Ip local
     hostname = socket.gethostname()
     try:
        ip_local = socket.gethostby(hostname)
     except:
        ip_local = "Não disponível."
        print(f'IP local: {ip_local}')

    # Status da rede - Interfaces ativas
    interfaces = psutil.net_if_addrs()
    print('\nInterfaces de Rede:')
    for interface_name, addresses in interfaces.items():
         print(f'    {interface_name}:')
    for addr in addresses:
        if addr.family == socket.AF_INET:
              print(f'    IPv4: {addr.address}')
        elif addr.family == socket.AF_INET:
            print(f'    IPv6: {addr.address}')
    ver_ip_statusRede()

# Testar velocidade da Conexão

if resposta == '4':

    def testar_velocidade_internet():
        try:
            import speedtest

            print('Testando a velociade da sua internet...')
            st = speedtest.Speedtest()
            st.get_best_server()

            download = st.download()
            upload = st.upload()
            ping = st.results.ping

            print('\nResultado do teste de velocidade:')
            print(f'Download: {download / 1_000_000:.2f} Mbps')
            print(f'Upload: {upload / 1_000_000:.2f} Mbps')
            print(f'Ping: {ping:.0f} ms/n')
        
        except Exception as e:
            print('Ocorreu um erro ao testar a velocidade da internet:')
            print(e)

    testar_velocidade_internet()

# Limpar arquivos temporários:

if resposta == '5':
    def limpar_temporarios():
        sistema = platform.system()

        # Define local do arquivo com base no OS
        if sistema == "Windows":
            temp_path = os.getenv('TEMP')
        elif sistema == "Linux":
            temp_path = "/tmp"
        else:
            print("Sistema operacional não suportado.")
            return

        print(f"Limpando arquivos temporários em: {temp_path}")

        arquivos_removidos = 0

        #Pega os dados apurados e os insere numa lista dentro de variavel
        try:
            itens = os.listdir(temp_path)
        except Exception as erro:
            print(f"Erro ao acessar a pasta temporária: {erro}")
            return
        
        # Para cada item em "itens", os deleta um por um e adiciona +1 à contagem
        for item in itens:
            item_path = os.path.join(temp_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    arquivos_removidos += 1
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    arquivos_removidos += 1
            except Exception as e:
                print(f"Não foi possível remover {item_path}: {e}")

        print(f"\n{arquivos_removidos} arquivos/pastas removidos com sucesso.")
    limpar_temporarios()

# Gerar senha segura para usuário
if resposta == '6':
    def gerar_senha():
        tamanho = 11 # Define escopo da senha
        caracteres = string.ascii_letters + string.digits + string.punctuation # Define caracteres a serem usados (ascii, digitos e pontuações)
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # Define a senha como escolhas aleatorias dentre os caracteres
        print(f'\n Senha gerada com sucesso: \n{senha}\n') # Exibe a senha emitida
        time.sleep(120) # Tempo de 120 segundos (2 min) para que o user anote a senha
    
    gerar_senha()

# Encerrar FEMTO

if resposta == '0':
    print('Encerrando...')
    time.sleep(2)
    exit()