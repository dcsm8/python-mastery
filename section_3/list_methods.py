# List methods
basket = [1, 2, 3, 4, 5]

# adding
basket.append(100)

# insert
basket.insert(6, 200)

# extending
basket.extend([300, 400])

# removing
last_item = basket.pop()

print(last_item)

basket.remove(100)

print(basket)

print(basket.count(200))

print(200 in basket)


# sort

print(sorted(basket))

basket.sort()
print(basket)

# reverse
basket.reverse()
print(basket)
