class BMI:

    def bmi(self,weight,height):
        try:
            weight = float(weight)
            height = float(height)
        except ValueError:
            print("Input was not a float.")
            raise TypeError

        if(weight < 0 or height < 0):
            print("Input(s) were values less than 0.")
            raise ValueError


        weight *= 0.45
        height *= 0.025
        squared_height = height * height
        body_mass_index = "%.1f" % (weight/squared_height)
        return body_mass_index
