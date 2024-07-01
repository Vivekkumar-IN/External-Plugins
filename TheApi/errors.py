class InvalidAmountError(Exception):
    def __init__(self, amount, method, max):
        super().__init__(
            f"Invalid amount of {method} requested: {amount}. Maximum allowed is {max} Minimum allowed is 1."
        )
