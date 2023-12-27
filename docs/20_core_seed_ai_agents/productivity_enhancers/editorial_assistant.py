import data_detective


class EditorialAssistant:
    def __init__(self):
        self.corrections = []

    def check_grammar(self, text):
        # Use the data_detective module to check the grammar of the text
        self.corrections = data_detective.check_grammar(text)
        return self.corrections

    def improve_style(self, text):
        # Use the data_detective module to improve the style of the text
        improved_text = data_detective.improve_style(text)
        return improved_text
