#A program that sorts elements from largest to smallest.

dt = {3: 34, 2: 67, 1: 23}

sorted_dt = {
  key: value
  for key, value in sorted(dt.items(), key=lambda item: item[1])
}

print(sorted_dt)
