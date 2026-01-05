import statistics

ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]


print(f"Count: {len(ages)}")
print(f"Sum: {sum(ages)}")
print(f"Min: {min(ages)}")
print(f"Max: {max(ages)}")
print(f"Range: {max(ages) - min(ages)}")
print(f"Mean: {statistics.mean(ages)}")
print(f"Median: {statistics.median(ages)}")
print(f"Mode: {statistics.mode(ages)}")
print(f"Variance: {statistics.variance(ages)}")
print(f"Standard Deviation: {statistics.stdev(ages)}")
