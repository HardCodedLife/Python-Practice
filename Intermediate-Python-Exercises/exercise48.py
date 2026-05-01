def exercise48(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero!"
    except TypeError:
        result = "Error: Please provide numbers (integers or floats)."
    finally:
        print("Operation complete")
        return result
if __name__ == "__main__":
   print(exercise48(10, 2))
   print(exercise48(10, 0))
   print(exercise48(10, "apple"))
