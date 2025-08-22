
import math

class CircleAreaCalculator:
  """
  Calcula a área de uma circunferência usando diferentes valores de pi.
  """

  def __init__(self, pi_strategy):
    self.pi_strategy = pi_strategy

  def calculate_area(self, radius):
    """Calcula a área da circunferência."""
    return self.pi_strategy.get_pi() * (radius ** 2)












