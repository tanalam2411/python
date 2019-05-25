

import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, hostname):

        if hostname not in self._cache:
            self._cache[hostname] = socket.gethostbyname(hostname)

        return self._cache[hostname]

    def clear(self):
        self._cache.clear()

    def has_host(self, hostname):
        return hostname in self._cache


if __name__ == '__main__':

    r = Resolver()
    print r('python.org')

    from timeit import timeit
    timeit(setup="resolve = Resolver()", stmt="reslove("
                                                      "'python.org')", number=1)
