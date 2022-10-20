class CountFromBy:

     def __init__(self, v: int=0, i: int=1) -> None:
             self.val = v
             self.incr = i

     def increase(self) -> None:
             self.val += self.incr


     def __repr__(self) -> str:
             return str(self.val)
     
     @staticmethod
     def total() -> str:
          return '10'


if __name__ == '__main__':
        c = CountFromBy(100,10)
        c.increase()
        print(c)

