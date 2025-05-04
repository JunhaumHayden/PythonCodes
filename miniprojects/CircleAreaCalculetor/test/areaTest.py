# Cria uma instância com pi padrão
from src.domain.CircleAreaCalculator import CircleAreaCalculator
from src.domain.HighPrecisionPiStrategy import HighPrecisionPiStrategy
from src.domain.StandardPiStrategy import StandardPiStrategy

def test_area_pi_padrao():
  # Cria uma instância com pi padrão
  calculator = CircleAreaCalculator(StandardPiStrategy())
  area = calculator.calculate_area(5)
  assert area == 78.53981633974483

def test_area_pi_alta_precisao():
  # Cria uma instância com alta precisão de pi
  calculator = CircleAreaCalculator(HighPrecisionPiStrategy())
  area = calculator.calculate_area(5)
  assert area == 78.53981633974483

