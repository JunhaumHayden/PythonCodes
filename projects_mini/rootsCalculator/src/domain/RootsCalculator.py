class CalculadoraRaizes:
  """
  Classe que calcula raízes de uma equação do segundo grau usando uma estratégia de precisão.
  """
  def __init__(self, strategy):
    self._strategy = strategy

  def calcular_raizes(self, a, b):
    """
    Calcula as raízes da equação usando a estratégia definida.

    Args:
      a: Coeficiente 'a' da equação.
      b: Coeficiente 'b' da equação.

    Returns:
      Uma tupla contendo as duas raízes da equação.
    """
    return self._strategy.calcular_raizes(a, b)