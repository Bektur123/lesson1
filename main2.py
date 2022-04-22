second = int(input('Vedite cheslo!:'))
hour = second % 60
minute = hour % 60
second = minute % 60
print(f"hour{hour}, minute{minute}, second{second}")
# print(f"time {time:.2f}")
# print("time %d" % (second))