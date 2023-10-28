def LCM(a, b):
  t = a % b
  if t == 0:
        return a
  return a * LCM(b, t) / t

print(LCM(2, 5))