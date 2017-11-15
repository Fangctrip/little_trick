import time
from dis import dis
import itertools
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0=time.time()
        result=func(*args,**kwargs)
        e=time.time()-t0
        name=func.__name__
        al=[]
        if args:
            al.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs=['{k}={w}'.format(k=k,w=w) for k,w in sorted(kwargs.items())]
            al.append(','.join(pairs))
        astr=','.join(al)
        print('[{:.4f}]{}{}--->{}'.format(e,name,astr,result))
        return result
    return clocked
#@clock
#def fc(n):
#    return 1 if n < 2 else n*fc(n-1)

DEFAULT_FMT = '[{el:0.8f}],{name},{args}----->{result}'

def clock2(fmt=DEFAULT_FMT):
    print(1)
    def decorate(func):
        print(2)
        def clocked(*_args):
            print(3)
            t0=time.time()
            _result=func(*_args)
            el=time.time()-t0
            name=func.__name__
            args=','.join(repr(arg) for arg in _args )
            result=repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

@clock2()
def sb(t):
    time.sleep(t)

for i in range(3):
    sb(0.123)
