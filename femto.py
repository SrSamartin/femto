import os
import shutil
import platform
import socket
import psutil
import getpass
import time
import random
import string

# Diagnostico da Máquina: usuário, sistema operacional, versão do sistema; uso de CPU, RAM e Armazenamento // ipconfig

def diagnostico_completo():
    user = getpass.getuser()
    so = platform.system()
    versao = platform.version()
    print(f'Usuário: {user}')
    print(f'Sistema Operacional: {so} - Versão: {versao}')

    cpu = psutil.cpu_percent(interval=1)
    print(f'Uso da CPU: {cpu}%')

    ram = psutil.virtual_memory()
    print(f'RAM usada: {ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB ({ram.percent}%)')

    disco = shutil.disk_usage('C:/')
    usado = disco.used // (1024**2)
    total = disco.total // (1024**2)
    print(f'Espaço em disco: {usado} MB usados de {total} MB ({usado / total * 100:.2f}%)')

    hostname = socket.gethostname()
    try:
        ip_local = socket.gethostbyname(hostname)
    except:
        ip_local = "Não disponível."
    print(f'IP local: {ip_local}')

    interfaces = psutil.net_if_addrs()
    print('\nInterfaces de Rede:')
    for interface_name, addresses in interfaces.items():
        print(f'  {interface_name}:')
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print(f'    IPv4: {addr.address}')
            elif addr.family == socket.AF_INET6:
                print(f'    IPv6: {addr.address}')
    print('\nDiagnóstico Concluído!\n')

# Teste apenas de CPU, RAM e Armazenamento

def cpu_ram_disco():
    print('\n[cpu_ram_disco]\n')

    cpu = psutil.cpu_percent(interval=1)
    print(f'Uso da CPU: {cpu}%')

    ram = psutil.virtual_memory()
    print(f'RAM usada: {ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB ({ram.percent}%)')

    disco = shutil.disk_usage('C:/')
    usado = disco.used // (1024**3)
    total = disco.total // (1024**3)
    print(f'Espaço em disco: {usado} GB usados de {total} GB ({usado / total * 100:.2f}%)')

# Teste só IPconfig

def ver_ip_statusRede():
    print('\n[ver_ip_statusRede]\n')
    hostname = socket.gethostname()
    try:
        ip_local = socket.gethostbyname(hostname)
    except:
        ip_local = "Não disponível."
    print(f'IP local: {ip_local}')

    interfaces = psutil.net_if_addrs()
    print('\nInterfaces de Rede:')
    for interface_name, addresses in interfaces.items():
        print(f'  {interface_name}:')
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print(f'    IPv4: {addr.address}')
            elif addr.family == socket.AF_INET6:
                print(f'    IPv6: {addr.address}')

# Teste de velocidade da internet

def testar_velocidade_internet():
    try:
        import speedtest
        print('Testando a velocidade da sua internet...')
        st = speedtest.Speedtest()
        st.get_best_server()

        download = st.download()
        upload = st.upload()
        ping = st.results.ping

        print('\nResultado do teste de velocidade:')
        print(f'Download: {download / 1_000_000:.2f} Mbps')
        print(f'Upload: {upload / 1_000_000:.2f} Mbps')
        print(f'Ping: {ping:.0f} ms')
    except Exception as e:
        print('\n[!] O teste de velocidade não está disponível neste ambiente...') # <------ ÚNICA RESPOSTA POSSÍVEL NA ATUAL VERSÃO. Possível restrição por parte do SVd arcom
        print(f'Erro: {e}')

# Limpa arquivos temporários. Tem algumas restrições...

def limpar_temporarios():
    sistema = platform.system()
    if sistema == "Windows":
        temp_path = os.getenv('TEMP')
    elif sistema == "Linux":
        temp_path = "/tmp"
    else:
        print("Sistema operacional não suportado.")
        return

    print(f"Limpando arquivos temporários em: {temp_path}")
    arquivos_removidos = 0

    try:
        itens = os.listdir(temp_path)
    except Exception as erro:
        print(f"Erro ao acessar a pasta temporária: {erro}")
        return

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

# Gera uma senha forte

def gerar_senha():
    tamanho = 11
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f'\nSenha gerada com sucesso:\n{senha}\n')
    time.sleep(15) # Timer para usuário copiar senha

# Menu interativo com loop | Executa a função correspondente à resposta
while True:
    print("""
 Bem-vindo ao...
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

    opcoes = {
        '1': diagnostico_completo,
        '2': cpu_ram_disco,
        '3': ver_ip_statusRede,
        '4': testar_velocidade_internet,
        '5': limpar_temporarios,
        '6': gerar_senha
    }
    # Condição nova. Controle do loop do menu
    if resposta in opcoes:
        opcoes[resposta]()
    elif resposta == '0':
        print('Encerrando...')
        time.sleep(2)
        break
    else:
        print('Opção inválida.')