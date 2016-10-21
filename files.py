# Writing File.
write = open("example.txt", "w")
write.write("Testing")
write.close()

# Reading File.
reading = open('example.txt', 'r')
print(reading.read())
