#  Lets say we need to store data of apple stock prices for 5 days
import sys

apple_stock = [230, 330, 300, 420, 440]

# day1 what is the stock price
# apple_stock[0] - O(1)

# In which day the price is 330
# for price in apple_stock : - O(n)

# stock.insert() - O(n) because need to shift elements

# stock.remove(2) - O(n) need to shift

# size is increases = currentsize*2
# total size is = currentsize*2 + currentsize
# this is called geomatical progression

# arrays can store text, numbers and complex objects
# arrays can have multiple dimensions


