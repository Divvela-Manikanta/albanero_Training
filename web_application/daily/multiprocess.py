import multiprocessing

print(multiprocessing.cpu_count())

def hello():
    for i in range(500):
        print("hello")

def hii():
    for i in range(500):
        print("hii")

myprocess1 = multiprocessing.Process(target=hello)
myprocess2 = multiprocessing.Process(target=hii)
if __name__ == '__main__':
    myprocess1.start()
    myprocess2.start()
# hello()
# hii()