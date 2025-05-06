import corpus
import spacy
import stanza
import pandas as pd


def process_data_chunk(data_chunk, spacy_nlp, stanza_nlp):

    '''
    This function uses SpaCy and Stanza to create individual Corpus class instances from a pandas data frame. Upon
    creation of these class instances, each individual document, utterance, and token within the corpus will also
    generate their own instances within their respective subordinate classes, and save values relevant for analysis to
    attributes at each level. Then, the attributes from both the Spacy Corpus and Stanza Corpus are saved in two data
    frames, with each row representing a single utterance in the corpus: agreement_df and disagreement_df. These data
    frames will look the same with the exception that in agreement_df, the tokens in the spacy_main_verb and
    stanza_main_verb columns should be the same, while in disagreement_df, values in those columns are different.
    '''

    # create Corpus class instances for each NLP package
    spacy_corpus = corpus.Corpus()
    spacy_corpus.create_corpus_from_dataframe(data_chunk, tokenizer='spacy', nlp=spacy_nlp)

    stanza_corpus = corpus.Corpus()
    stanza_corpus.create_corpus_from_dataframe(data_chunk, tokenizer='stanza', nlp=stanza_nlp)

    print(f"SpaCy corpus has {len(spacy_corpus.document_list)} documents")
    print(f"Stanza corpus has {len(stanza_corpus.document_list)} documents")

    # create data frames & populate them with relevant attributes for each utterance in each corpus
    agreement_df = []
    disagreement_df = []

    for spacy_doc, stanza_doc in zip(spacy_corpus.document_list, stanza_corpus.document_list):
        for spacy_utterance, stanza_utterance in zip(spacy_doc.utterance_list, stanza_doc.utterance_list):
            spacy_row = {
                'Utterance Index': spacy_utterance.utterance_index,
                'Document Name': spacy_doc.document_name,
                'Transcript Index': spacy_utterance.transcript_index,
                'Target Child Age': spacy_doc.target_child_age,
                'Speaker ID': spacy_utterance.speaker_id,
                'Utterance': spacy_utterance.utterance_string,
                'SpaCy Main Verb': spacy_utterance.main_verb,
                'SpaCy Lemma': spacy_utterance.lemma,
                'SpaCy Verb Type': spacy_utterance.verb_type,
                'SpaCy Inflection': spacy_utterance.inflection,
                'SpaCy Grammatical Aspect': spacy_utterance.tense_aspect,
            }
            stanza_row = {
                'Utterance Index': spacy_utterance.utterance_index,
                'Document Name': spacy_doc.document_name,
                'Transcript Index': spacy_utterance.transcript_index,
                'Target Child Age': spacy_doc.target_child_age,
                'Speaker ID': spacy_utterance.speaker_id,
                'Utterance': spacy_utterance.utterance_string,
                'Stanza Main Verb': stanza_utterance.main_verb,
                'Stanza Lemma': stanza_utterance.lemma,
                'Stanza Verb Type': stanza_utterance.verb_type,
                'Stanza Inflection': stanza_utterance.inflection,
                'Stanza Grammatical Aspect': stanza_utterance.tense_aspect,
            }

        '''
        Before appending the rows to the data frames, checking whether the NLP modules detect a value for the 
        inflection attribute ensures that the "main_verb" is actually something that is being recognized as a verb with
        inflectional information like tense and aspect, thereby preventing tokens that are incorrectly mistaken as 
        verbs (like nouns and function words) from being included in the main verb column.
        
        This code also filters the rows for cases where the speaker is either a child ('CHI') or a caregiver ('MOT', 
        'FAT') for the purposes of the current analysis.
        '''
        if spacy_utterance.inflection and stanza_utterance.inflection:
            if spacy_utterance.speaker_id in ['CHI', 'MOT', 'FAT']:
                if spacy_utterance.main_verb == stanza_utterance.main_verb:
                    agreement_df.append({**spacy_row, **stanza_row})
                if spacy_utterance.main_verb != stanza_utterance.main_verb:
                    disagreement_df.append({**spacy_row, **stanza_row})

    pd.DataFrame(agreement_df).to_csv("../processed_data/agreement_data.csv", mode='a', header=not
                                      pd.io.common.file_exists("../processed_data/agreement_data.csv"), index=False)
    pd.DataFrame(disagreement_df).to_csv("../processed_data/disagreement_data.csv", mode='a', header=not
                                         pd.io.common.file_exists("../processed_data/disagreement_data.csv"),
                                         index=False)

def main():
    # load nlp packages separately
    spacy_nlp = spacy.load('en_core_web_md')
    stanza_nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

    # provide data file path
    file_path = "../indexed_utterances.csv"

    # prompt user to input the target child age range (in days) to be processed
    min_age = int(input("Enter the minimum age value: ").strip())
    max_age = int(input("Enter the maximum age value: ").strip())

    print(f"Processing data for age {min_age} to {max_age}...")

    # create a data frame from the CSV and filter for the specified age range
    data_chunk = pd.read_csv(file_path)
    data_chunk["target_child_age"] = data_chunk["target_child_age"].astype(int) # make all values in column integers
    data_chunk = data_chunk[(data_chunk["target_child_age"] >= min_age) & (data_chunk["target_child_age"] <= max_age)]

    # if the filtered data frame isn't empty, process it
    if not data_chunk.empty:
        process_data_chunk(data_chunk, spacy_nlp, stanza_nlp)
    else:
        print(f"No data found for ages {min_age}-{max_age}.")

if __name__ == '__main__':
    main()