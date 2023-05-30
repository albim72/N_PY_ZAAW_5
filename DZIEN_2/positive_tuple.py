class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped_values = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_values += 1
        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_values = skipped_values
        return instance

pos = PositiveTuple(4,78,90,-23,-2,9,12,0,-24,1)
print(pos)
print(type(pos))
print(pos.skipped_values)


