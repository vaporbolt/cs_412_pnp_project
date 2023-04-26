import random

f = open("big_test.txt", "w")
text = ""
num_vertexes = int(input())
num_edges = (num_vertexes * (num_vertexes - 1)) // 2
text += str(num_vertexes) + " " + str(num_edges) + "\n"
for i in range(num_vertexes):
    for j in range(num_vertexes):
        if i != j and j > i:
            text += str(i) + " " + str(j) + " " + str(random.uniform(0.00, 10000.00)) + "\n"
f.write(text)
f.close()
