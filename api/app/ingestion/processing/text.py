import string


class TextProcessor:

    def __init__(self, text: str):

        self.text = text

    def count_words(self) -> int:
        """Number of words in the text"""
        return len(self.text.split())

    def count_chars(self) -> int:
        return len(self.text.replace(" ", ""))

