"""
STATISTIC CLASS

# A class is like a toy factory
# It knows how to make and work with numbers
"""


class Statistics:
    def __init__(self, data):
        # When we create a Statistics object
        # We give it a list of numbers to play with
        self.data = data

    def count(self):
        # This function counts how many numbers we have
        total = 0
        for _ in self.data:
            total += 1
        return total

    def sum(self):
        # This function adds all the numbers together
        total = 0
        for number in self.data:
            total += number
        return total

    def min(self):
        # This function finds the smallest number
        smallest = self.data[0]

        for number in self.data[1:]:
            if number < smallest:
                smallest = number
        return smallest

    def max(self):
        # This function finds the biggest number
        biggest = self.data[0]

        for number in self.data[1:]:
            if number > biggest:
                biggest = number
        return biggest

    def range(self):
        # Range means: biggest number minus smallest number
        return self.max() - self.min()

    def mean(self):
        # Mean is the 'average'
        # Add everything, then divide by how many numbers we have
        return self.sum() / self.count()

    def median(self):
        # Median is the middle number when everything is sorted
        sorted_data = sorted(self.data)
        middle = self.count() // 2

        # If we have even numbers, we take two middle numbers
        if self.count() % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2

        # If odd, we take the middle one
        return sorted_data[middle]

    def mode(self):
        # Mode is the number that appears the most
        freq = {}

        # Count how many times each number appears
        for number in self.data:
            freq[number] = freq.get(number, 0) + 1

        # Find the number with the biggest count
        biggest_count = 0
        most_common = None
        for key, value in freq.items():
            if value > biggest_count:
                biggest_count = value
                most_common = key

        return {"mode": most_common, "count": biggest_count}

    def var(self, type="population"):
        # Variance tells us how spread out the numbers are
        mean = self.mean()
        total = 0

        # Subtract mean, square it, and add it up
        for number in self.data:
            total += (number - mean) ** 2

        # Sample variance uses (count - 1)
        if type == "sample":
            return total / (self.count() - 1)

        # Population variance uses count
        return total / self.count()

    def std(self):
        # Standard deviation is just square root of variance
        return self.var() ** 0.5

    def freq_dist(self):
        # Frequency distribution shows how often numbers appear in percent
        freq = {}

        for number in self.data:
            freq[number] = freq.get(number, 0) + 1

        result = []
        for key, value in freq.items():
            percent = (value / self.count()) * 100
            result.append((round(percent, 1), key))

        # Sort from biggest percent to smallest
        return sorted(result, reverse=True)
