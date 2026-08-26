import datetime
import utils

print("Saquib")
now = datetime.datetime.now()
print(now)

sum_result = utils.add(10, 5)
sub_result = utils.subtract(10, 5)

print(f"10 + 5 = {sum_result}")
print(f"10 - 5 = {sub_result}")
print("10 * 5 =", utils.multiply(10, 5))

try:
    print("10 / 2 =", utils.divide(10, 2))
    print("10 / 0 =", utils.divide(10, 0))
except ValueError as e:
    print("Error:", e)