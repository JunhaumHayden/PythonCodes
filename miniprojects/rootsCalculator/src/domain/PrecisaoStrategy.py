class PrecisaoStrategy:
  """
  Interface para estratégias de cálculo com diferentes precisões.
  """
  def calcular_raizes(self, a, b):
    raise NotImplementedError("Subclasses devem implementar este método.")