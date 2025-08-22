from src.domain.CircleAreaCalculator import CircleAreaCalculator
from src.domain.HighPrecisionPiStrategy import HighPrecisionPiStrategy
from src.domain.StandardPiStrategy import StandardPiStrategy

# Exemplo de uso:

# Cria uma instância com pi padrão
calculator = CircleAreaCalculator(StandardPiStrategy())
area = calculator.calculate_area(5)
print("Área com pi padrão:", area)

# Cria uma instância com alta precisão de pi
calculator = CircleAreaCalculator(HighPrecisionPiStrategy())
area = calculator.calculate_area(5)
print("Área com pi de alta precisão:", area)