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
        body_mass_index = "%.1f" % (weight/squared_height)
        return body_mass_index
