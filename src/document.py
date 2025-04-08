from utterance import Utterance


class Document:
    def __init__(self, document_name, target_child_age):
        self.document_name = document_name
        self.utterance_list = []
        self.speaker_list = []
        self.target_child_age = target_child_age

    def add_utterance(self, utterance_index, utterance_string, speaker_id, terminator_type, tokenizer=None, nlp=None):
        new_utterance = Utterance(utterance_index, utterance_string, speaker_id, terminator_type, tokenizer, nlp)
        self.utterance_list.append(new_utterance)