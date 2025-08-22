
from src.domain.PrecisaoDuplaStrategy import PrecisaoDuplaStrategy
from src.domain.PrecisaoSimplesStrategy import PrecisaoSimplesStrategy
from src.domain.RootsCalculator import CalculadoraRaizes


def test_roots_calculator_precisao_simples():
    a = 1
    b = 100.23
    # Calcular com precisão dupla
    calculadora_dupla = CalculadoraRaizes(PrecisaoDuplaStrategy())
    x1_float64, x2_float64 = calculadora_dupla.calcular_raizes(a, b)
    assert x1_float64 == 100.220021953892
    assert x2_float64 == 0.009978046107995908

def test_root_calculator_precisao_dupla():
    a = 1
    b = 100.23
    # Calcular com precisão simples
    calculadora_simples = CalculadoraRaizes(PrecisaoSimplesStrategy())
    x1_float32, x2_float32 = calculadora_simples.calcular_raizes(a, b)
    assert x1_float32 == 100.220024
    assert x2_float32 == 0.009979248