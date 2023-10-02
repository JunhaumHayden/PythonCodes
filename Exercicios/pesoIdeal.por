//Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
//Para Homens: (72,7* altura) – 58
//Para Mulheres: (62,1 * altura) – 44.7
//• Na leitura do sexo só poderão ser aceitos M (masculino) ou F (feminino)
//• Realizar a seguinte pergunta ao usuário: ‘DESEJA CONTINUAR (S/N) ?’ e repetir caso a resposta for afirmativa.


programa {
  funcao inicio() {

//Declaracao de variaveis
logico flag
cadeia sexo
real altura, pesoIdeal



faca
{
  flag = verdadeiro
  enquanto(flag == verdadeiro)
  {
    escreva("Digite o sexo (M para masculino, F para feminino): ")
    leia(sexo)
  
    se (sexo != "m" e sexo != "f")
    { 
      escreva ("Valor invalido, Digite novamente!\n")
    }
    senao
    {
      flag = falso
    }

  }

  escreva("Digite a altura: \n")
  leia(altura)


   // Calcula o peso ideal
  se (sexo == "m") 
  {
    pesoIdeal = (72.7 * altura) - 58
    escreva("O peso ideal para um homem com ",altura," metros de altura é ", pesoIdeal," kg.\n")
  } 
  senao 
  {
    pesoIdeal = (62.1 * altura) - 44.7
    escreva("O peso ideal para um mulher com ",altura," metros de altura é ", pesoIdeal," kg.\n")
  }

  escreva("DESEJA CONTINUAR (S/N)? ")
  leia(sexo)

}

enquanto(sexo == "s")

escreva("\n")
escreva("******************\n")
escreva("\n")
escreva("Programa Encerrado!\n")
escreva("\n")
escreva("******************\n")

    
    
  }
}