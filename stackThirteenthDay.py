browsing = []
browsing.append(1)
browsing.append(2)
browsing.append(3)

browsing.pop()
print("redirect", browsing[-1])
print(browsing)

browsing.pop()
browsing.pop()
if not browsing:
    print("disable")