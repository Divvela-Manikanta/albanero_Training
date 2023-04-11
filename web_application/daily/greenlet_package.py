# import greenlet

# def function1():
#     print("In in function 1")
#     g2.switch()
#     print("In in function 1 again")
#     g2.switch()


# def function2():
#     print("In the funtion 2")
#     g1.switch()
#     print("In in function 2 again")

# g1 = greenlet.greenlet(function1)
# g2 = greenlet.greenlet(function2)

# g1.switch()


# def add():
#     print("in add ")
#     g3.switch()


# def sub():
#      print("in sub ")

# def mul():
#     print("in mul ")
#     g2.switch()

# g1 = greenlet.greenlet(add)
# g2 = greenlet.greenlet(sub)
# g3 = greenlet.greenlet(mul)

# g1.switch()




# check = True

# def marks(m1,m2):
#     if(m1<30 or m2<30):
#         global check
#         check = False
#     g2.switch(3)
    
# def attend(att):
#     if(att<60):
#         global check
#         check = False
#     g3.switch()
    

# def result():
#     if(check):
#         print("student have cleared the sem")
#     else:
#         print("student have not cleared the sem")

# g1 = greenlet.greenlet(marks)
# g2 = greenlet.greenlet(attend)
# g3 = greenlet.greenlet(result)

# g1.switch(90,80)

# import gevent
# from gevent import socket
# urls = ['www.google.com', 'www.example.com', 'www.python.org']
# jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls]
# gevent.joinall(jobs,timeout=2)
# for job in jobs:
#     print(job)

# from gevent import monkey
# import gevent 
# monkey.patch_all()
# import requests


# urls = [
#     'https://www.google.com/',
#     'https://www.apple.com/',
# ]

# def response(url):
#     print('Starting %s' % url)
#     data = requests.get(url).text
#     print('%s: %s bytes: %r' % (url, len(data), data[:500]))

# jobs = [gevent.spawn(response, _url) for _url in urls]

# gevent.wait(jobs)



# import requests
# import greenlet

# def response(url):
#     val = requests.get(url).text
#     print(val[:500])

# g1 = greenlet.greenlet(response)

# urls = [
#     'https://www.google.com/',
#     'https://www.apple.com/',
# ]

# for url in urls:
#     g1.switch(url)

# import threading
# import requests

# def response(url):
#     val = requests.get(url)
#     if(val.status_code==200):
#         print(val.text[:500])
#     else:
#         print("not connected to api")

# t1 = threading.Thread(target=response,args=('https://www.google.com/',))
# t2 =  threading.Thread(target=response,args=('https://www.google.com/',))
# try:
#     t1.start()
# except Exception as ex:
#     print(ex)

# t1.join()
# t2.start()
# t2.join()

# import asyncio
# import time

# async def main1():
#     print(1)
#     await asyncio.sleep(1)
#     time.sleep(1)
#     print(2)

# async def call():
#     await asyncio.gather(main1(),main1(),main1())

# if __name__ == '__main__':
#     asyncio.run(call())

# async def f():
#     sum =0 
#     for i in range(10):
#         sum=sum+i
#     await asyncio.sleep(1)
#     return sum


# async def g():
#     y = await f()
#     print(y)

# async def call():
#     await asyncio.gather(g(),f())

# if __name__ =='__main__':
#     asyncio.run(call())



# import asyncio

# @asyncio.coroutine
# def py34_coro():
#     """Generator-based coroutine"""
#     # No need to build these yourself, but be aware of what they are
#     s = yield from stuff()
#     return s

# async def py35_coro():
#     """Native coroutine, modern syntax"""
#     s = await stuff()
#     return s

# async def stuff():
#     return 0x10, 0x20, 0x30

# import asyncio

# async def f():
#     sum =0 
#     for i in range(10):
#         sum=sum+i
#     await asyncio.sleep(1)
#     return sum

# async def g():
#     y = await f()
#     print(y)

# async def call():
#     task1 = asyncio.create_task( g())
#     task2 = asyncio.create_task( f())

#     await task1
#     await task2

#     print("the tasks are done")

# if __name__ =='__main__':
#     asyncio.run(call())



