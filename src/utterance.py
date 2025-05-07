from corpus_token import Token
from replacements import replacements
from vendler_classification import classified_verbs


class Utterance:
    """The second most subordinate class in the structure (below Document)."""
    def __init__(self,
                 utterance_index: int,
                 transcript_index: int,
                 utterance_string: str,
                 speaker_id: str,
                 terminator_type: str,
                 tokenizer=None,
                 nlp=None
                 ) -> None:

        self.utterance_index = utterance_index
        self.transcript_index = transcript_index
        self.utterance_string = str(utterance_string) if utterance_string is not None else ""  # Ensure string
        self.terminator_type = terminator_type
        self.speaker_id = speaker_id
        self.tokenizer = tokenizer
        self.nlp = nlp

        self.token_list = []
        self.main_verb = None
        self.lemma = None
        self.inflection = None
        self.tense_aspect = None
        self.verb_type = None

        self.utterance_string = self.utterance_string.replace("_", " ") # gets rid of underscores
        self.create_utterance(nlp)
        self.verb_type = self.classify_main_verb(self.lemma)

    # turn the utterance into a list of tokens
    def create_utterance(self, nlp) -> None:
        """Uses the nlp argument to determine how an utterance (a list of tokens) will be created.

        Args:
            nlp: The loaded nlp package used to tokenize the utterances
        """
        if self.tokenizer is not None:
            if self.tokenizer == 'spacy':
                self.create_spacy_token_list(nlp)
            elif self.tokenizer == 'stanza':
                self.create_stanza_token_list(nlp)
            else:
                raise Exception(f'Unrecognized tokenizer: {self.tokenizer}')
        else:
            self.create_token_list()

    def create_stanza_token_list(self, nlp) -> None:
        """The method for making an utterance (list of tokens) when Stanza is the loaded nlp package.

        Args:
            nlp: The loaded nlp package used to tokenize the utterances (Stanza)
        """
        doc = nlp(self.utterance_string)

        for sentence in doc.sentences:
            for token in sentence.tokens:
                for word in token.words:
                    token_dict = {
                    "text": word.text,
                    "lemma": word.lemma,
                    "pos": word.upos,
                    "dep": word.deprel,
                    "tag": word.xpos,
                    "morph": word.feats if word.feats else {},
                    }
                    self.token_list.append(token_dict)
                    self.identify_main_verb(token_dict)
                    self.identify_inflection(token_dict)

    def create_spacy_token_list(self, nlp) -> None:
        """The method for making an utterance (list of tokens) when SpaCy is the loaded nlp package.

        Args:
            nlp: The loaded nlp package used to tokenize the utterances (SpaCy)
        """
        tokens = nlp(self.utterance_string)

        for token in tokens:
            token_dict = {
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "dep": token.dep_,
                "tag": token.tag_,
                "morph": token.morph.to_dict(),
            }
            self.token_list.append(token_dict)
            self.identify_main_verb(token_dict)
            self.identify_inflection(token_dict)

    def create_token_list(self):
        """The default method for making an utterance (list of tokens) when no nlp package is loaded."""
        token_string_list = self.utterance_string.split()
        for token_string in token_string_list:
            new_token = Token(token_string)
            self.token_list.append(new_token)


    # identify relevant features for analysis (main verb, inflection, and verb classification)
    def identify_main_verb(self, token: str) -> None:
        """Uses the NLP modules to identify whether the token is the main verb of its utterance.

        Args:
            token: The current token in the utterance
        """
        if self.tokenizer == 'spacy':
            if token.get('dep') == 'ROOT':
                self.main_verb = token.get('text')
                self.main_verb = replacements.get(self.main_verb, self.main_verb)
                if self.nlp:
                    updated_token = self.nlp(self.main_verb)[0] # the main verb is a list item, so it's indexed
                    self.lemma = updated_token.lemma_
        elif self.tokenizer == 'stanza':
            if token.get('dep') == 'root':
                self.main_verb = token.get('text')
                self.main_verb = replacements.get(self.main_verb, self.main_verb)
                if self.nlp:
                    doc = self.nlp(self.main_verb)
                    for sent in doc.sentences:
                        for word in sent.words:
                            self.lemma = word.lemma
                            return # exits nested loops early, prevents correct lemma from being overwritten
        else:
            pass

    def identify_inflection(self, token: str) -> None:
        """Uses the NLP modules to get the corresponding code for the verb form of the main verb and the tense/aspect
        code of the utterance.

        Args:
            token: The current token in the utterance
        """
        if self.tokenizer is not None:
            if self.tokenizer == 'spacy':
                if token.get('pos') in ['VERB', 'AUX']:
                    self.inflection = token.get('tag')
                    self.tense_aspect = token.get('morph')
            elif self.tokenizer == 'stanza':
                if token.get('pos') in ['VERB', 'AUX']:
                    self.inflection = token.get('tag')
                    self.tense_aspect = token.get('morph')
        else:
            pass

    def classify_main_verb(self, lemma: str) -> str:
        """Uses the imported Vendler_classification dictionary to assign a main verb's classification.

        Args:
            lemma: The uninflected base form of the main verb (e.g. the lemma of 'walking' is 'walk')

        Returns:
            str: The four-way Vendler classification of the verb
        """
        self.verb_type = classified_verbs.get(lemma, "unknown")
        return self.verb_type