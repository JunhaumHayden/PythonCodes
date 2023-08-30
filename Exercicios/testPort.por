        real peso, altura, imc
        
            escreva("Digite o peso (em kg): ")
            leia(peso)
        
            escreva("Digite a altura (em metros): ")
            leia(altura)
        
            imc = peso / (altura * altura)
        
            escreva("IMC: %.2f\n", imc)
        
            se (imc < 18.5) 
            {
                escreva("Calsificação: Abaixo do peso\n")
            }
            senao se (imc >= 18.5 e imc < 25) 
            {
                escreva("Calsificação: Peso normal\n")
            } 
            senao se (imc >= 25 e imc < 30) 
            {
                escreva("Calsificação: Sobrepeso\n")
            } 
            senao se (imc >= 30 e imc < 35) 
            {
                escreva("Calsificação: Obesidade - Grau I\n")
            } 
            senao se (imc >= 35 e imc < 40) 
            {
                escreva("Calsificação: Obesidade - Grau II\n")
            } 
            senao 
            {
                escreva("Calsificação: Obesidade - Grau III\n")
            }
        
    
        }