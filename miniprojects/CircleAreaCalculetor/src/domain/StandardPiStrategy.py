import math

from src.domain.PiStrategy import PiStrategy


class StandardPiStrategy(PiStrategy):
  """Estratégia para pi com valor padrão."""

  def get_pi(self):
    return math.pi