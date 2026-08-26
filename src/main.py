import datetime
import utils

print("Saquib")
now = datetime.datetime.now()
print(now)

sum_result = utils.add(10, 5)
sub_result = utils.subtract(10, 5)

print(f"10 + 5 = {sum_result}")
print(f"10 - 5 = {sub_result}")