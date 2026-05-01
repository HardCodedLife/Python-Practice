class Pizza:
    @staticmethod
    def validate_topping(topping: str) -> bool:
        return True if topping in ('apple', 'banana','pineapple') else False

    @classmethod
    def margherita(cls):
        print('Pizza ordered: Margherita')

if __name__ == "__main__":
    Pizza.margherita()
    print( "Is topping valid?: ", True if Pizza.validate_topping("pineapple") else False)
