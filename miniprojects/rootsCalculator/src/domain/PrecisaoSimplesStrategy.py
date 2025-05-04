import numpy as np

from src.domain.PrecisaoStrategy import PrecisaoStrategy


class PrecisaoSimplesStrategy(PrecisaoStrategy):
  """
  Estratégia para calcular raízes com precisão simples.
  """
  def calcular_raizes(self, a, b):
    a = np.float32(a)
    b = np.float32(b)
    delta = np.sqrt(b**2 - 4*a)
    x1 = (b + delta) / (2*a)
    x2 = (b - delta) / (2*a)
    return x1, x2