from utterance import Utterance


class Document:
    """
    The second most superordinate class in the structure (below Corpus). Documents are sub-corpora that make up the
    full corpus in CHILDES. Each Document instance has a target child age attribute (the age of the child being studied
    in that sub-corpus). It also has a list of all the utterances within that sub-corpus.
    """
    def __init__(self, document_name: str, target_child_age: int) -> None:
        self.document_name = document_name
        self.utterance_list = []
        self.target_child_age = target_child_age

    def add_utterance(self,
                      utterance_index: int,
                      transcript_index: int,
                      utterance_string: str,
                      speaker_id: str,
                      terminator_type: str,
                      tokenizer=None,
                      nlp=None
                      ) -> None:
        """Creates an instance of the Utterance class and adds it to the list of utterances.

        Args:
            utterance_index: The index of the utterance in the entire corpus
            transcript_index: The index of the utterance in the current document
            utterance_string: The utterance itself
            speaker_id: The ID of the speaker of the utterance (e.g. 'CHI' for target child, 'MOT' for mother)
            terminator_type: The punctuation at the end of an utterance (e.g. period, question mark, exclamation point)
            tokenizer: The string identifying which NLP package is being used
            nlp: The loaded nlp package used to tokenize the utterances
        """
        new_utterance = Utterance(utterance_index, transcript_index, utterance_string, speaker_id, terminator_type, tokenizer, nlp)
        self.utterance_list.append(new_utterance)