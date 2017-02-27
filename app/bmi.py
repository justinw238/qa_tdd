class BMI:

    def bmi(self,weight,height):
        try:
            weight = float(weight)
            height = float(height)
        except ValueError:
            raise(ValueError("Invalid Input"))

        weight *= 0.45
        height *= 0.025
        squared_height = height * height
        BMI = weight/squared_height
        return ("%.1f" % BMI)
