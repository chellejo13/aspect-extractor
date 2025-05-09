class Token:
    """
    The most subordinate structure in the class structure (below Utterance). Only really useful in the case where there
    is no nlp package loaded.

    Attribution: This class structure was written in collaboration with Dr. Jon Willits
    """
    def __init__(self, original_token_string):
        self.original_token_string = original_token_string
        self.text = None

        self.create_token()

    def create_token(self) -> None:
        """
        For the default method of creating a list of tokens from an utterance (without a nlp package), this can be used.
        """
        self.text = self.original_token_string.lower()