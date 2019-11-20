from werkzeug.local import LocalStack

s = LocalStack()
# 推入栈中
s.push(1)
print(s.top)
print('----')
print(s.top)
print('----')
print(s.pop())
print('----')
print(s.top)
