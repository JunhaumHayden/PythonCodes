import numpy as np

from src.domain.PrecisaoStrategy import PrecisaoStrategy


class PrecisaoDuplaStrategy(PrecisaoStrategy):
  """
  Estratégia para calcular raízes com precisão dupla.
  """
  def calcular_raizes(self, a, b):
    delta = np.sqrt(b**2 - 4*a)
    x1 = (b + delta) / (2*a)
    x2 = (b - delta) / (2*a)
    return x1, x2