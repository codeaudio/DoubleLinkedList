from queue import LifoQueue

stack = LifoQueue()
with open('stack.txt', 'r') as f:
    data = [list(n.split()) for n in f.read().split('\n')]
for elem in data:
    if 'push' in elem:
        if not stack.empty():
            stack.put(max(int(elem[1]), stack.queue[-1]))
        else:
            stack.put(int(elem[1]))
    elif 'pop' in elem:
        if len(stack.queue) >= 1:
            stack.queue.pop()
        else:
            print('error')
    elif 'get_max' in elem:
        try:
            print(stack.queue[-1])
        except:
            print('None')
