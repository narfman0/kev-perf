from kev import Document, CharProperty

from .loading import kev_handler


class TestDocument(Document):
    name = CharProperty(required=True, unique=True, min_length=3, max_length=20)
    content = CharProperty(required=True, unique=True, min_length=3, max_length=20)
    # TODO add date and maybe other stuff for testing :)

    def __unicode__(self):
        return self.name

    class Meta:
        use_db = 'redis'
        handler = kev_handler
