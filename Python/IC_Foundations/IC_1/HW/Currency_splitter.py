denominations = [200,100,50,20,10,5,2,1]
result = { }
amount = 287
for coin in denominations:
    count = amount // coin
    if count > 0:
        result[coin] = count
        amount = amount % coin

print (result)
