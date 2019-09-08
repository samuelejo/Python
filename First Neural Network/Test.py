glob = 5

def work():
    global glob
    glob = 2
    print (glob)

work()
print (glob)
