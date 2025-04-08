from document import Document
import pandas as pd

class Corpus:
    def __init__(self):
        self.document_list = []  # list of documents
        self.num_documents = 0
        self.tokenization_times = {"spacy": [], "stanza": []}

    def add_tokenization_time(self, tokenizer_name, elapsed_time):
        if tokenizer_name in self.tokenization_times:
            self.tokenization_times[tokenizer_name].append(elapsed_time)

    def create_corpus_from_dataframe(self, df, tokenizer=None, nlp=None):
        current_document_name = None
        current_document = None

        for _, row in df.iterrows():
            utterance_index = row.iloc[0]
            row_document_name = row.iloc[1]
            utterance_string = str(row.iloc[3]) if pd.notna(row.iloc[3]) else ""
            speaker_id = row.iloc[4]
            target_child_age = row.iloc[14]
            terminator_type = row.iloc[15]

            if row_document_name != current_document_name:
                if current_document_name is not None:
                    for utterance in current_document.utterance_list:
                        if hasattr(utterance, 'tokenization_times'):
                            for tokenizer_name, times in utterance.tokenization_times.items():
                                self.tokenization_times[tokenizer_name].extend(times)
                    self.add_document(current_document)
                current_document_name = row_document_name
                current_document = Document(current_document_name, target_child_age)

            current_document.add_utterance(
                utterance_index, utterance_string, speaker_id, terminator_type, tokenizer, nlp
            )

        if current_document_name is not None:
            for utterance in current_document.utterance_list:
                if hasattr(utterance, 'tokenization_times'):
                    for tokenizer_name, times in utterance.tokenization_times.items():
                        self.tokenization_times[tokenizer_name].extend(times)
            self.add_document(current_document)

    def add_document(self, current_document):
        self.document_list.append(current_document)
        self.num_documents += 1
        if self.num_documents % 100 == 0 and self.num_documents != 0:
            print(f'Corpus has {self.num_documents} documents')