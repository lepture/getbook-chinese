from getbook.core import Parser


class MarxistsParser(Parser):
    NAME = 'piaotian'
    ALLOWED_DOMAINS = ['www.marxists.org']
    SOUP_FEATURES = 'html5lib'

    @classmethod
    def check_url(cls, url):
        return url.endswith('.htm')

    def parse_lang(self):
        return 'zh'

    def parse_publisher(self):
        return u'中文马克思主义文库'

    def parse_title(self):
        return getattr(self, '__title', '')

    def parse_content(self):
        node = self.dom.find('body')

        started = False
        prev_hr = False

        for el in node.find_all(True, recursive=False):
            if not started:
                classes = el.get('class')
                if classes and 'title1' in classes:
                    self.__title = el.get_text()
                    started = True
                el.extract()

            if prev_hr and el.name == 'span' and el.get('style'):
                el.name = 'div'

            prev_hr = el.name == 'hr'

        node.name = 'div'
        return node

    def clean_content(self, content):
        content = content.replace('->', '', 1)
        sections = content.split('<hr/><div>')
        if len(sections) == 2:
            article = sections[0]
            return _format_content(article) + '<hr/><div>' + sections[1]
        else:
            return content


def _format_paragraph(text):
    text = text.strip()
    if not text:
        return ''

    if text.startswith('<') or text.endswith('>'):
        return text
    return '<p>' + text + '</p>'


def _format_content(content):
    return ''.join(_format_paragraph(p) for p in content.split('<br/>'))
