from kev import DateTimeProperty, Document, CharProperty

from kev_perf.settings import active_db, kev_handler


class TestDocument(Document):
    name = CharProperty(required=True, unique=True, min_length=3, max_length=20)
    last_updated = DateTimeProperty(auto_now=True)
    content = CharProperty(min_length=3, max_length=200*1024)

    def __unicode__(self):
        return self.name

    class Meta:
        use_db = active_db
        handler = kev_handler
