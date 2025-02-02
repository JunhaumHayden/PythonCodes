class CreditCardValidator:

    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self):
        if self._is_valid_length() and self._passes_luhn_algorithm():
            return self._get_card_type()
        return "Invalid"

    def _is_valid_length(self):
        """Verificação do Comprimento do Número do Cartão:
        O método verifica se o comprimento do número do cartão está entre 13 e 19 dígitos. Se o comprimento não estiver dentro desse intervalo, o cartão é considerado inválido.
        """
        return 13 <= len(self.card_number) <= 19

    def _passes_luhn_algorithm(self):
        """ "Verificação do Algoritmo de Luhn:
        Se o comprimento for válido, o método aplica o algoritmo de Luhn para verificar a validade do número do cartão. O algoritmo de Luhn é um método comum de verificação de números de cartões de crédito.
        """
        total = 0
        reverse_digits = self.card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def _get_card_type(self):
        """Determinação do Tipo de Cartão:
        Se ambas as verificações anteriores forem bem-sucedidas, o método determina o tipo de cartão (por exemplo, Visa, MasterCard, American Express, etc.) com base nos primeiros dígitos do número do cartão.
        """
        if self.card_number.startswith(("34", "37")):
            return "American Express"
        elif self.card_number.startswith("4"):
            return "Visa"
        elif self.card_number.startswith(("51", "52", "53", "54", "55")):
            return "MasterCard"
        elif self.card_number.startswith("6"):
            return "Discover"
        else:
            return "Unknown"


if __name__ == "__main__":
    # Example usage for different card types:
    card_numbers = {
        "American Express": "378282246310005",
        "Visa": "4111111111111111",
        "MasterCard": "5105105105105100",
        "Discover": "6011111111111117",
        "Unknown": "123456789012345",
    }

    for card_type, number in card_numbers.items():
        validator = CreditCardValidator(number)
        print(f"{card_type}: {validator.validate()}")
