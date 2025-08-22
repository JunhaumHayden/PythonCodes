# PythonCodes
Codes in Python



<h1 align="center"> Sistema de Controle de Lavação de Veículos </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Description

Português-Br

<h2 align = "center"> Sumário Executivo </h>

O proprietário de uma lavação de veículos solicitou um sistema de controle de lavação. 
Em sua explanação do controle atual, o referido proprietário apontou que o controle é composto pela entrega do veículo para execução de serviços, sendo eles de vários tipos, por exemplo:
- Lavação completa;
- Impermeabilização de bancos;
- Lavação de motor;
- Polimento;
- Polimento espelhado.

Destacou ainda, que cada tipo de serviço possui um valor que é determinado com o tamanho do veículo (categoria), podendo ser:
- Pequeno;
- Médio;
- Grande;
- Padrão/Comum; 
- Moto.

Quanto ao tamanho, o proprietário comentou que em alguns tipos de serviço é adotada uma tarifa comum ou padrão independente do tamanho do veículo, por exemplo, o serviço de polimento de rodas, cuja taxa é comum a todos os tipos de veículos.
Perguntado ao proprietário, quais seriam as informações relevantes para se manter no sistema, ele respondeu:
- É necessário conhecer as características do veículo, sendo elas, placa de identificação, o modelo do veículo, assim como sua marca, além de apontar a categoria do mesmo.
- É importante ainda ter informações relevantes a respeito do proprietário do veículo, também chamado de cliente da lavação. Destaca-se que o cliente/proprietário pode ser tanto pessoa física quanto jurídica, e interessa saber quem é proprietário do veículo quando há uma necessidade de contato com o mesmo.
- Considerando que a lavação presta serviços aos seus clientes, é importante manter no sistema os tipos de serviços que podem ser prestados de acordo com os tipos de categorias de veículos, levando em consideração dados como descrição e valor do serviço.
- Requisito muito importante para o sistema, é manter os registros de ordem de serviços. Vale ressaltar que uma ordem de serviço (OS) poderá ser composta por vários serviços e que a mesma esteja vinculada diretamente a um veículo. A OS deverá ter necessariamente número, agenda (data), total da ordem e possivelmente uma taxa de desconto que pode ser aplicada em situações demandadas. É necessário considerar que uma OS apresente os seguintes estados: ABERTA, FECHADA ou CANCELADA. A OS aberta, permitirá atualizações na ordem, enquanto que fechada ou cancelada, não podem permitir qualquer tipo de movimentação. Em relação a este controle, foi apontado ainda, que cada serviço da OS pode apresentar valor diferente daquele registrado no cadastro de serviço, isto é, se um determinado serviço custa X, na prestação de serviço para um determinado
cliente e/ou ocasião, o serviço poderá ser cobrado no valor de Y sem que isso afete
o cadastro de serviço, ou seja, é algo momentâneo.
- Considera-se ainda a possibilidade de que o sistema apresente um controle de
pontuação para um plano de fidelidade ao cliente. Assim sendo, cada serviço executado em uma OS implica no acúmulo de pontos ao cliente que, eventualmente, poderá ser trocado por serviços ou descontos diretamente na lavação. Vale destacar que a pontuação é exclusiva e intransferível para uso do cliente.


<h2 align="center"> Modelo Conceitual: </h2>

Para desenvolver um modelo de dados e definir as operações principais que o sistema deve suportar. Abaixo, segue um modelo conceitual e funcionalidades básicas que podem ser implementadas.


1. **Veículo:**
   - Placa de Identificação
   - Modelo
   - Marca
   - Categoria (Pequeno, Médio, Grande, Padrão/Comum, Moto)

2. **Cliente:**
   - Nome
   - Tipo (Pessoa Física ou Jurídica)
   - Informações de Contato

3. **Serviço:**
   - Descrição
   - Valor Padrão

4. **Ordem de Serviço (OS):**
   - Número
   - Data (Agenda)
   - Total da Ordem
   - Estado (ABERTA, FECHADA, CANCELADA)
   - Taxa de Desconto
   - Veículo Associado
   - Cliente Associado

5. **Item de Serviço na OS:**
   - Serviço (referenciando o serviço padrão)
   - Valor Personalizado para a OS
   - Pontuação Acumulada para o Cliente

### Funcionalidades:

1. **Cadastro e Gerenciamento:**
   - Cadastro, atualização e remoção de veículos, clientes e serviços.
   - Associação de serviços às categorias de veículos.
   - Controle de pontos para o plano de fidelidade.

2. **Ordem de Serviço (OS):**
   - Criação de uma nova OS associada a um veículo e cliente.
   - Adição/remoção de serviços à OS, com a opção de definir valores personalizados.
   - Cálculo do total da ordem considerando os serviços e descontos.
   - Alteração do estado da OS (ABERTA, FECHADA, CANCELADA).

3. **Relatórios:**
   - Exibição de relatórios de serviços realizados, faturamento, pontos acumulados, etc.



<h2 align="center"> Esboço de um Diagrama de Classe: </h2>

+------------------+       +------------------+       +--------------------+
|     Veiculo      |       |     Cliente      |       |     Servico        |
+------------------+       +------------------+       +--------------------+
| - placa: string  |       | - nome: string   |       | - descricao: string|
| - modelo: string |       | - tipo: string   |       | - valor_padrao:    |
| - marca: string  |       | - info_contato:  |       |   float            |
| - categoria:     |       |   string         |       +--------------------+
|   string         |       |                  |
+------------------+       +------------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-------v-----------+       +-----v------------------------+
|  OrdemServico     |       | ItemServico                  |
+-------------------+       +------------------------------+
| - numero: string  |       | - servico: Servico           |
| - data: string    |       | - valor_personalizado: float |
| - veiculo: Veiculo|       | - pontuacao_acumulada: int   |
| - cliente: Cliente|       +------------------------------+ 
| - estado: string  |                
| - total_ordem:    |       
|   float           |
| - taxa_desconto:  |
|   float           |
+-------------------+
