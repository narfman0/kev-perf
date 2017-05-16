from kev import DateTimeProperty, Document, CharProperty

from .loading import kev_handler


class TestDocument(Document):
    name = CharProperty(required=True, unique=True, min_length=3, max_length=20)
    last_updated = DateTimeProperty(auto_now=True)
    content = CharProperty(required=True, unique=True, min_length=3, max_length=200*1024)

    def __unicode__(self):
        return self.name

    class Meta:
        use_db = 'redis'
        handler = kev_handler
