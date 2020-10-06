class Poly:
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.coe = list(coefficient)

    # This method is a helper method
    @staticmethod
    def extend_zero(thelist, n):
        for _ in range(n - len(thelist)):
            thelist.append(0)

    def add(self, p):
        a_list = list(self.coe)
        b_list = p.coe
        Poly.extend_zero(a_list, max(len(a_list), len(b_list)))
        Poly.extend_zero(b_list, max(len(a_list), len(b_list)))
        c_list = [x + y for x, y in zip(a_list, b_list)]
        return Poly(c_list)

    def scalar_multiply(self, n):
        return Poly([n * x for x in self.coe])

    def multiply(self, p):
        itself = list(self.coe)
        other = list(p.coe)
        output = [0 for _ in range(len(itself) * len(other))]
        for i_it, num_it in enumerate(itself):
            for i_ot, num_ot in enumerate(other):
                output[i_it + i_ot] += num_ot * num_it

        return Poly(output)

    def power(self, n):
        if n == 0:
            return Poly([1])
        if n == 1:
            return Poly(self.coe)

        output = self
        for _ in range(n - 1):
            output = self.multiply(output)

        return output

    def diff(self):
        altered = list(self.coe[1::])
        output = [(i+1) * num for i, num in enumerate(altered)]
        return Poly(output)

    def integrate(self):
        altered = list(self.coe)
        output = [num / (i+1) for i, num in enumerate(altered)]
        output.insert(0, 0)
        return Poly(output)

    def eval(self, n):
        output = 0
        for i, num in enumerate(self.coe):
            output += num * (n ** i)

        return output

    def print(self):
        output = ""
        for i, num in enumerate(self.coe):
            if num == 0:
                continue
            if i == 0:
                output += str(num)
                continue
            if num < 0 and output != "":
                output += " - "
            elif output != "":
                output += " + "
            if i == 1:
                output += f"{abs(num)}x"
                continue

            output += f"{abs(num)}x^{i}"

        print(output)