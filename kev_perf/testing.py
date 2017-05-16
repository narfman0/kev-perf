import time

from .models import TestDocument


def execute_test():
    test1 = TestDocument(name='kev', content='yo content')
    test1.save()
    start = time.time()
    TestDocument.objects().filter({'name': 'kev'})
    end = time.time()
    print('Duration: {}'.format(end-start))


if __name__ == "__main__":
    execute_test()
