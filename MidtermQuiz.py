class DistanceConversion:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        if self.unit == 'km':
            return self.value * 1000
        elif self.unit == 'cm':
            return self.value / 100
        elif self.unit == 'inch':
            return self.value / 39.37
        else:
            raise ValueError("Invalid unit:" , to_unit)

    def convert_from_meters(self, meters, to_unit):
        if to_unit == 'km':
            return meters / 1000
        elif to_unit == 'cm':
            return meters * 100
        elif to_unit == 'inch':
            return meters * 39.37
        else:
            raise ValueError("Invalid unit:" , to_unit)

def main():
    distance = float(input("Enter the distance: "))
    unit = input("Enter the unit (km, cm, or inch): ")
    converter = DistanceConversion(distance, unit)
    meters = converter.convert_to_meters()

    print("Enter the unit to convert to (km, cm, or inch): ")
    to_unit = input()
    converted = converter.convert_from_meters(meters, to_unit)
    print(str(distance) + " " + unit + " = " + str(converted) + " " + to_unit)

if __name__ == "__main__":
    main()
