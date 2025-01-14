# Desenvolva um sistema que simule a enumeração de serviços em um servidor, dado um conjunto de portas e serviços associados. Você deve receber uma lista de números de portas e, para cada porta, retornar o serviço associado. Se a porta não estiver no dicionário, retorna "Desconhecido". O dicionário de portas e serviços é fornecido no código. O código deve receber uma string de portas separadas por vírgula e retornar uma lista de serviços correspondentes.

# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",  # Serviço de transferência de arquivos
    22: "SSH",  # Secure Shell (acesso remoto seguro)
    23: "Telnet",  # Protocolo de acesso remoto inseguro
    25: "SMTP",  # Serviço de envio de emails
    53: "DNS",  # Serviço de tradução de nomes de domínio
    80: "HTTP",  # Protocolo de transferência de hipertexto (web)
    110: "POP3",  # Serviço de recebimento de emails
    143: "IMAP",  # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",  # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",  # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL",  # Banco de dados PostgreSQL
    6379: "Redis",  # Banco de dados Redis
}


# Função que converte uma string de portas separadas por vírgula em uma lista de inteiros
def parse_ports(ports_str):
    return [int(port.strip()) for port in ports_str.split(",")]


# Função que realiza a enumeração de serviços
def enumerate_services(ports):
    # Inicializamos uma lista para armazenar os serviços correspondentes
    services = []

    # Itere sobre cada porta fornecida na lista de portas
    for port in ports:
        # Verifique se a porta existe no dicionário de serviços
        if port in port_services:
            # Se existir, adicione o serviço correspondente à lista de serviços
            services.append(port_services[port])
        else:
            # Se a porta não estiver mapeada, adicione "Desconhecido"
            services.append("Desconhecido")

    return services


# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    ports_input = input()

    # Converta a string de entrada para uma lista de inteiros (números de portas)
    ports = parse_ports(ports_input)

    # Chame a função de enumeração para obter a lista de serviços correspondentes:
    services = enumerate_services(ports)

    print(services)


if __name__ == "__main__":
    main()
