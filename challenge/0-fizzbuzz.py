if i % 3 == 0 and i % 5 == 0:
    tmp_result.append("FizzBuzz")
elif i % 3 == 0:
    tmp_result.append("Fizz")
elif i % 5 == 0:
    tmp_result.append("Buzz")
else:
    tmp_result.append(str(i))
