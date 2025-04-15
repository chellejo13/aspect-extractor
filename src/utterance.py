from corpus_token import Token
import time
from replacements import replacements
from vendler_classification import classified_verbs


class Utterance:
    def __init__(self, utterance_index, transcript_index, utterance_string, speaker_id, terminator_type, tokenizer=None, nlp=None):
        self.utterance_index = utterance_index
        self.transcript_index = transcript_index
        self.utterance_string = str(utterance_string) if utterance_string is not None else ""  # Ensure string
        self.token_list = []
        self.terminator_type = terminator_type # terminators are what the utterance ends with (e.g. period, question mark, exclamation point)
        self.speaker_id = speaker_id
        self.tokenizer = tokenizer
        self.nlp = nlp

        self.main_verb = None
        self.lemma = None
        self.inflection = None
        self.tense_aspect = None
        self.verb_type = None

        self.utterance_string = self.utterance_string.replace("_", " ") # gets rid of underscores
        self.create_utterance(nlp)
        self.verb_type = self.classify_main_verb(self.lemma)

    def create_utterance(self, nlp):
        if self.tokenizer is not None:
            if self.tokenizer == 'spacy':
                self.create_spacy_token_list(nlp)
            elif self.tokenizer == 'stanza':
                self.create_stanza_token_list(nlp)
            elif self.tokenizer == 'allennlp':
                self.create_allennlp_token_list(nlp)
            else:
                raise Exception(f'Unrecognized tokenizer: {self.tokenizer}')
        else:
            self.create_token_list()

    # split into tokens (4 options)
    def create_allennlp_token_list(self, nlp):
        prediction = nlp.predict(sentence=self.utterance_string)
        tokens = prediction['words']
        pos_tags = prediction['pos']
        dependencies = prediction['dependencies']

        for i, token_text in enumerate(tokens):
            token_dict = {
                'text': token_text,
                'pos': pos_tags[i],
                'dep': dependencies[i],
            }
            self.token_list.append(token_dict)
            self.identify_main_verb(token_dict)
            self.identify_inflection(token_dict)
            self.identify_control_verb(self)

    def create_stanza_token_list(self, nlp):
        start_time = time.time()
        doc = nlp(self.utterance_string)
        elapsed_time = time.time() - start_time

        self.add_tokenization_time("stanza", elapsed_time)

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

    def create_spacy_token_list(self, nlp):
        start_time = time.time()
        tokens = nlp(self.utterance_string)
        elapsed_time = time.time() - start_time

        self.add_tokenization_time("spacy", elapsed_time)

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
        token_string_list = self.utterance_string.split()
        for token_string in token_string_list:
            new_token = Token(token_string)
            self.token_list.append(new_token)

    def add_tokenization_time(self, tokenizer_name, elapsed_time):
        if not hasattr(self, 'tokenization_times'):
            self.tokenization_times = {"spacy": [], "stanza": []}
        self.tokenization_times[tokenizer_name].append(elapsed_time)

        if len(self.tokenization_times[tokenizer_name]) % 20 == 0:
            avg_time = sum(self.tokenization_times[tokenizer_name]) / len(self.tokenization_times[tokenizer_name])
            print(f"[{tokenizer_name}] Processed 20 utterances. Avg time per utterance: {avg_time:.4f} seconds")

    # identify relevant features (main verb, inflection)
    def identify_main_verb(self, token):
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

        elif self.tokenizer == 'allennlp':
            if token.get('dep') == 'ROOT':
                self.main_verb = token.get('text')
                self.main_verb = replacements.get(self.main_verb, self.main_verb)
        else:
            pass

    def identify_inflection(self, token):
        if self.tokenizer is not None:
            if self.tokenizer == 'spacy':
                if token.get('pos') in ['VERB', 'AUX']:
                    self.inflection = token.get('tag')
                    self.tense_aspect = token.get('morph')
            elif self.tokenizer == 'stanza':
                if token.get('pos') in ['VERB', 'AUX']:
                    self.inflection = token.get('tag')
                    self.tense_aspect = token.get('morph')
            elif self.tokenizer == 'allennlp':
                if token.get('pos') in ['VERB', 'AUX']:
                    self.inflection = token.get('pos')
                    self.tense_aspect = token.get('morph')
        else:
            pass

    def classify_main_verb(self, lemma):
        self.verb_type = classified_verbs.get(lemma, "unknown")
        return self.verb_type