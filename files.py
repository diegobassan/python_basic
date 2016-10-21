# Escrita em Arquivo
write = open("example.txt", "w")
write.write("Testing")
write.close()

# Leitura em Arquivo
reading = open('example.txt', 'r')
print(reading.read())
