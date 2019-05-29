import re
from getbook.core import Parser, Book

BOOK_PATTERN = re.compile(r'/read/(\d+)$')
PAGE_PATTERN = re.compile(r'/chapter/\d+/\d+$')


class ZhaishuyuanParser(Parser):
    NAME = 'zhaishuyuan'
    ALLOWED_DOMAINS = ['www.zhaishuyuan.com']
    SOUP_FEATURES = 'html5lib'

    @classmethod
    def check_url(cls, url):
        return True

    def parse(self):
        m = BOOK_PATTERN.findall(self.url)
        if m:
            book_id = m[0]
            return self.parse_book(book_id)
        return super(ZhaishuyuanParser, self).parse()

    def parse_book(self, book_id):
        self.fetch()
        uid = '{}-{}'.format(self.NAME, book_id)
        el = self.dom.find('h1')
        title = el.get_text()
        book = Book(uid, title, lang='zh')

        els = self.dom.select('div#smallcons > span > a')
        if els:
            author = els[0].get_text()
            book.author = author
        book.chapters = list(self._parse_book_chapters())
        return book

    def parse_lang(self):
        return 'zh'

    def parse_publisher(self):
        return u'斋书苑'

    def parse_title(self):
        el = self.dom.find('h1')
        title = el.get_text()
        return title.strip()

    def parse_content(self):
        return self.dom.find('div', id='content')

    def _parse_book_chapters(self):
        els = self.dom.select('div#readerlists li > a')
        for el in els:
            href = el.get('href')
            href = self.urljoin(href)
            title = el.get_text()
            yield {'title': title, 'url': href}
