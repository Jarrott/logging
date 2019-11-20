from werkzeug.local import Local
import threading
import time
# 线程隔离的对象


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('in new thread b is' + str(my_obj.b))


new_t = threading.Thread(target=worker(), name='Test')
new_t.start()
time.sleep(5)
print('in main thread b is' + str(my_obj.b))