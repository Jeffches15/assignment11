from app.models.calculation import Addition, Subtraction, Multiplication, Division, Calculation
from app.schemas.calculation import CalculationType

# The factory replaces manual if/else logic where you choose 
    # and instantiate calculation subclasses (Addition, Subtraction, etc.) based on the type.
class CalculationFactory:

    @staticmethod
    def create_calculation(calc_type: CalculationType, a: float, b: float) -> Calculation:
        if calc_type == CalculationType.ADDITION:
            return Addition(a=a, b=b)
        elif calc_type == CalculationType.SUBTRACTION:
            return Subtraction(a=a, b=b)
        elif calc_type == CalculationType.MULTIPLICATION:
            return Multiplication(a=a, b=b)
        elif calc_type == CalculationType.DIVISION:
            return Division(a=a, b=b)
        else:
            raise ValueError(f"Unknown calculation type: {calc_type}")