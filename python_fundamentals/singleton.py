#! /usr/bin/env python


class Singleton(object):

    def __init__(self, klass):
        self.klass = klass
        self.first_instance = None
        self.count = 0

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@Singleton
class Sample(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_all(self):
        print('a: %d' %(self.a))
        print('b: %d' %(self.b))
        print('c: %d' %(self.c))



@Singleton
class Sample1(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_all(self):
        print('a: %d' %(self.a))
        print('b: %d' %(self.b))
        print('c: %d' %(self.c))


if __name__ == '__main__':

    o1 = Sample(1, 2, 3)
    o1.print_all()

    print('---------------')
    # del Sample

    o2 = Sample(4, 5, 6)
    o2.print_all()