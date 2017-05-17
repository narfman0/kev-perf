import time

from kev_perf.models import TestDocument


def execute_test():
    test1 = TestDocument(name='kev')
    test1.content = 'yo content'
    test1.save()
    start = time.time()
    TestDocument.objects().filter({'name': 'kev'})
    end = time.time()
    print('Duration: {}'.format(end-start))


if __name__ == "__main__":
    execute_test()
