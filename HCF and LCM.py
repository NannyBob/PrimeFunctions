class HCF_LCM:
    # finds the Highest common factor using an optimised euclid's algorithm

    @staticmethod
    def find_hcf(x: int, y: int):
        while True:
            if x == 0:
                return y
            elif y == 0:
                return x
            elif x > y:
                x = x % y
            else:
                y = y % x

    @staticmethod
    def find_hcf_recursive(x: int, y: int):
        if x == 0:
            return y
        elif y == 0:
            return x
        elif x > y:
            return HCF_LCM.find_recursive(x % y, y)
        else:
            return HCF_LCM.find_recursive(y % x, x)

    # Finds lowest common multiple, building on Euclid's algorithm
    @staticmethod
    def find_lcm(x, y):
        return x * y / HCF_LCM.find(x, y)
