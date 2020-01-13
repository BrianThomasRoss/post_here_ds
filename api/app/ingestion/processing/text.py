import string


class TextProcessor:

    def __init__(self, text: str):

        self.text = text

    def filter_escapes(self) -> str:
        """Remove escape characters"""
        escape_chars = ['\r', '\n', '\t', '\b', "/", '\v', '\ooo', '\x']

        txt = self.txt

        for c in escape_chars:
            if c in txt:
                txt = txt.replace(c, "")
        return txt

    def filter_web(self) -> str:
        """Removes common URL strings"""
        web_chars =['https://', '.com', '.co.uk', 'www.', 'index.html', '/path',
            'docid']

        txt = self.text

        for word in txt:
            website = word.find(any(web_chars)
            if website:
                word = ""        
        return txt

        
