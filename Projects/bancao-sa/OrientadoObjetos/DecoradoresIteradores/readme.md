```mermaid

classDiagram
    Cliente <|-- PessoaFisica
    Conta <|-- ContaCorrente
    Transacao <|-- Saque
    Transacao <|-- Deposito

    class Cliente {
        -str endereco
        -list contas
        -int indice_conta
        +realizar_transacao(conta, transacao)
        +adicionar_conta(conta)
    }

    class PessoaFisica {
        -str nome
        -str data_nascimento
        -str cpf
    }

    class Conta {
        -int _saldo
        -str _numero
        -str _agencia
        -Cliente _cliente
        -Historico _historico
        +sacar(valor)
        +depositar(valor)
        +historico
    }

    class ContaCorrente {
        -int _limite
        -int _limite_saques
        +sacar(valor)
        +__str__()
    }

    class Historico {
        -list _transacoes
        +adicionar_transacao(transacao)
        +gerar_relatorio(tipo_transacao)
        +transacoes_do_dia()
    }

    class Transacao {
        <<abstract>>
        +valor
        +registrar(conta)
    }

    class Saque {
        -int _valor
        +valor
        +registrar(conta)
    }

    class Deposito {
        -int _valor
        +valor
        +registrar(conta)
    }

    class ContasIterador {
        -list contas
        -int _index
        +__iter__()
        +__next__()
    }

    Cliente o-- Conta
    Conta o-- Historico
    Cliente o-- Transacao
````
