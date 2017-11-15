import collections
import lxml


from math import hypot
card=collections.namedtuple('card',['rand','suit'])
class frendchdeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs heards'.split(' ')
    def __init__(self):
        self._cards=[card(rand,suit) for suit in self.suits for rand in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, item):
        return self.cards[item]

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        return(','.join([str(self.x),str(self.y)]))
    def __abs__(self):
        return hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

city=collections.namedtuple('city','name country population coordinates')
tokyo=city('tokyo','jp','13',(31,12))

a=[12,3,4]
b=slice(2,3)

print(a[b])

print(b)
print(help(lxml))
print(lxml.get_include())