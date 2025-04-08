
class Token:

    def __init__(self, original_token_string):

        self.original_token_string = original_token_string
        self.text = None
        self.pos = None
        self.tense = None
        self.aspect = None

        self.create_token()

    def __str__(self):
        output_string = self.text
        return output_string

    def create_token(self):
        self.text = self.original_token_string.lower()