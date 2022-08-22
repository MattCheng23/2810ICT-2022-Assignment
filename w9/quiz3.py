k = ["five", "twelve", "seventeen", "two", "eight", "seventeen"],["twenty", "fourteen", "eleven", "seven", "seventeen", "five", "two", "ten", "four", "twelve", "eleven"],["two", "nineteen", "seventeen", "ten", "seventeen", "nineteen", "seven", "four", "fifteen", "two"], ["seventeen", "fifteen", "nineteen", "eleven", "twelve", "ten", "nineteen", "one", "two", "three", "six", "eighteen"]]

j = {}
for y in k:
    if y in j:
       j[y] += 1
    else:
       j[y] =1
for e,c in j.items():
    print(e,c)


