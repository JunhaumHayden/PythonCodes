# Exemplo de uso:
from src.domain.PrecisaoDuplaStrategy import PrecisaoDuplaStrategy
from src.domain.PrecisaoSimplesStrategy import PrecisaoSimplesStrategy
from src.domain.RootsCalculator import CalculadoraRaizes

a = 1
b = 100.23

# Calcular com precisão dupla
calculadora_dupla = CalculadoraRaizes(PrecisaoDuplaStrategy())
x1_float64, x2_float64 = calculadora_dupla.calcular_raizes(a, b)

# Calcular com precisão simples
calculadora_simples = CalculadoraRaizes(PrecisaoSimplesStrategy())
x1_float32, x2_float32 = calculadora_simples.calcular_raizes(a, b)


print("Raízes com precisão dupla   (float64):", x1_float64, x2_float64)
print("Raízes com precisão simples (float32):", x1_float32,"     ", x2_float32)