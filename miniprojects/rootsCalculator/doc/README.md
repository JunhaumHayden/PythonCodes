# Calculo de Raizes de Equações

``` mermaid
classDiagram
    class PrecisaoStrategy {
        <<interface>>
        +calcular_raizes(a: float, b: float) float
    }

    class PrecisaoDuplaStrategy {
        +calcular_raizes(a: float, b: float) float
    }

    class PrecisaoSimplesStrategy {
        +calcular_raizes(a: float, b: float) float
    }

    class CalculadoraRaizes {
        - _strategy: PrecisaoStrategy
        +calcular_raizes(a: float, b: float) float
    }

    PrecisaoStrategy <|-- PrecisaoDuplaStrategy
    PrecisaoStrategy <|-- PrecisaoSimplesStrategy
    CalculadoraRaizes --> PrecisaoStrategy : Usa

```

## Explicação do Diagrama
- `PrecisaoStrategy` é uma interface que define o método calcular_raizes().
- `PrecisaoDuplaStrategy` e `PrecisaoSimplesStrategy` herdam da interface PrecisaoStrategy, cada uma implementando seu próprio método de cálculo.
- `CalculadoraRaizes` contém um atributo `_strategy`, que usa uma instância de PrecisaoStrategy para calcular as raízes da equação.