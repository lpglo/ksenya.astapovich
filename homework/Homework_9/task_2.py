temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda temp: temp > 28, temperatures))

highest_temp = max(hot_days)
lowest_temp = min(hot_days)
average_temp = sum(hot_days) / len(hot_days)

print(f"Hot days: {hot_days}")
print(f"Highest temperature: {highest_temp}")
print(f"Lowest temperature: {lowest_temp}")
print(f"Average temperature: {average_temp:.2f}")
