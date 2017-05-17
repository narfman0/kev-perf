import random
import string
import time

from kev_perf.models import TestDocument


def create_documents(name, count=10, content_length_min=300, content_length_max=200*1024):
    for i in range(count):
        content_length = random.randint(content_length_min, content_length_max)
        doc = TestDocument(name='kev%d' % i)
        doc.content = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(content_length))
        doc.save()


def execute_test():
    start_creation = time.time()
    for i in range(5):
        create_documents('name%d' % i)
    creation_time = int((time.time() - start_creation))
    start_filter = time.time()
    TestDocument.objects().filter({'name': 'name1'})
    filter_time = int((time.time() - start_filter)*1000)
    print('Creation duration: {}s filter duration: {}ms'.format(creation_time, filter_time))


if __name__ == "__main__":
    execute_test()
