//Desenvolver um programa para gerenciar a entrada de dados, processamento e saídas 
//de informações de uma empresa de lavação de carros.
//Para isso, o programa deverá 
// - Solicitar no início a quantidade de atendimentos que serão processados.
// - A cada atendimento deverão ser solicitados
//   - O nome do cliente
//   - O tipo (conforme o tamanho) do veículo, que pode ser identificado como 
//      1 - Pequeno (populares) 
//      2 - Médio (SUV e Picape)
//      3 /- Grande (Van e micro-ônibus). 
//Nota prever a validação do dado para aceitar apenas 1, 2 ou 3.
// - O serviço, que pode ser identificado como 
//      1 - Lavação externa
//      2 - Lavação externa + interna
//      3 - Lavação externa + interna + cera. 
//Nota prever a validação do dado para aceitar apenas 1, 2 ou 3.
//Considere a seguinte tabela de valores

//Serviço
//        Tipo do Veículo        	1	2	3
//        1        	        R$ 30        	        R$ 50        	        R$ 70        
//        2        	        R$ 50        	        R$ 70        	        R$ 90        
//        3        	        R$ 70        	        R$ 90        	        R$ 110        
//Para cada cliente, deverá ser apresentado a identificação do tipo do veículo; a identificação do serviço; e o valor a ser pago.
//Ao final, apresentar
//- Os percentuais dos atendimentos pelo tipo do veículo;
//- Os percentuais dos atendimentos pelo serviço;
//- O valor total arrecadado;
//- Qual o tipo do veículo foi o mais atendido;
//- Qual o serviço foi o mais atendido.


programa
{
    funcao
    {


        inteiro atend, sel
        cadeia cliente, tipo_veiculo, tipo_servico
        logico flag = verdadeiro
        escreva("Informe a quantidade de atendimentos \n")
        leia(atend)
        enquanto(atend != 0)
        {
            escreva("Informe o nome do cliente \n")
            leia (cliente)
            enquanto(flag == verdadeiro)
            {
                escreva("Selecionar o tipo de veiculo \n 1 - Pequeno (populares)\n 2 - Médio (SUV e Picape)\n 3 /- Grande (Van e micro-ônibus)\n Opção ")
                leia(sel)
                se (sel== 1)
                {
                    tipo_veiculo = "Pequeno (populares)"
                    flag = falso
                }
                senao se (sel== 2)
                {
                    tipo_veiculo = "Médio (SUV e Picape)"
                    flag = falso
                }
                senao se  (sel== 3)
                {
                    tipo_veiculo = "Grande (Van e micro-ônibus)"
                    flag = falso
                }
                senao
                {
                    escreva(
                            "Opção Invalida!
                            \nTente Novamente."
                            )
                } 
            }
            flag = verdadeiro
            sel = 0
            enquanto(flag == verdadeiro)
            {
                escreva("Selecionar o tipo de serviço
                        \n 1 - Lavação externa
                        \n 2 - Lavação externa + interna
                        \n 3 - Lavação externa + interna + cera
                        \nOpção "
                        )
                leia(sel)
                se (sel== 1)
                {
                    tipo_servico = "Lavação externa"
                    flag = falso
                }
                senao se (sel== 2)
                {
                    tipo_servico = "Lavação externa + interna"
                    flag = falso
                }
                senao se  (sel== 3)
                {
                    tipo_servico = "3 - Lavação externa + interna + cera"
                    flag = falso
                }
                senao
                {
                    escreva(
                            "Opção Invalida!
                            \nTente Novamente."
                            )
                } 
            }
            escreva("O cliente ",cliente, "Selecionou\n",tipo_servico,"para ", tipo_veiculo)
        } 







        
    }
}
