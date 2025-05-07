from document import Document
import pandas as pd

class Corpus:
    """
    The most superordinate (hierarch) class in the structure. It results in a list of all the documents (sub-corpora)
    in the full corpus and counts them as they're created.
    """
    def __init__(self) -> None:
        self.document_list = []
        self.num_documents = 0

    def create_corpus_from_dataframe(self, df, tokenizer=None, nlp=None) -> None:
        """Assigns data frame columns to variables and passes them to the add_utterance function for further
            processing. Creates a list of documents that compose the full corpus and counts them as they are added.

        Args:
            df: The data frame of raw corpus data
            tokenizer: The string identifying which NLP package is being used
            nlp: The loaded nlp package used to tokenize the documents
        """
        current_document_name = None
        current_document = None

        for _, row in df.iterrows():
            utterance_index = row.iloc[0]
            row_document_name = row.iloc[1]
            transcript_index = row.iloc[2]
            utterance_string = str(row.iloc[3]) if pd.notna(row.iloc[3]) else ""
            speaker_id = row.iloc[4]
            target_child_age = row.iloc[14]
            terminator_type = row.iloc[15]

            if row_document_name != current_document_name:
                if current_document_name is not None:
                    self.add_document(current_document)
                current_document_name = row_document_name
                current_document = Document(current_document_name, target_child_age)
            current_document.add_utterance(
                utterance_index, transcript_index, utterance_string, speaker_id, terminator_type, tokenizer, nlp
            )

        if current_document_name is not None:
            self.add_document(current_document)

    def add_document(self, current_document) -> None:
        """Adds current_document to the document list and increases the count of documents for each new one. Prints the
        number of documents that are in the corpus as the full corpus is processing to demonstrate progress.

        Args:
            current_document: The current document to be added
        """
        self.document_list.append(current_document)
        self.num_documents += 1
        if self.num_documents % 100 == 0 and self.num_documents != 0:
            print(f'Corpus has {self.num_documents} documents')