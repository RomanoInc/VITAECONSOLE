import read_cv 


data = read_cv.read_db()

print(type(data))

for i,j in enumerate(data):
    print(j)


