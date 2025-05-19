# Aspect Extractor
This repository contains a script that takes in a CSV of transcribed child and parent speech data and uses NLP packages 
to extract information denoting the lexical and grammatical aspect of each utterance in the corpus, compiling it all 
into two CSVs. Due to the imperfect nature of NLP, resulting CSV files are separated based on whether the packages agree
on the main verb of each utterance (compiled in agreement.csv) or not (compiled in disagreement.csv). These resulting 
CSV files can be used to analyze the degree to which children and adults adhere to predictions of the Aspect 
Hypothesis, which is defined below.

## Tense, Aspect, and Telicity
To understand the Aspect Hypothesis, the linguistic concepts of tense, grammatical aspect, lexical aspect, and telicity
must be understood.
- **Tense** is used to locate an event time with respect to speech time.
  - In English, past, present, and future tense locate events before, around, and after speech time respectively.
- **Grammatical Aspect** is used to characterize the speaker's view of the temporal contour of an event (e.g. continuation, completion).
  - In English, perfective aspect is marked on verbs using the suffix _-ed_ to denote a completed event, while imperfective aspect is marked on verbs using the suffix _-ing_ to denote an ongoing event.
- **Lexical Aspect** expresses the internal structure of an event; denoted by the semantic properties of a verb/verb phrase.
  - **Telicity** is the property of a verb or verb phrase that indicates whether the event has an inherent endpoint or not.

### Vendler's Four-Way Verb Classification
According to Vendler (1967), verbs can fall under four categories depending on their telicity and whether they have duration:
1. **Achievement** verbs characterize instantaneous events with inherent endpoints (telic).
   - In "Johnny _caught_ the ball." the event of "catching" happens in a single moment, and ends there.
2. **Accomplishment** verbs characterize events with some duration (durative), but that have an endpoint (telic).
   - In "He _made his bed_." the event of making a bed is a process that takes some times, but has a clear end result (a tidy bed).
3. **Activity** verbs characterize events that are durative and have no inherent endpoint.
   - In "She is _walking_ to the park.", the act of walking has duration and no assumed end.
4. **State** verbs are like activity verbs in that they are both durative and atelic, but they are not dynamic--they don't require any effort to occur.
   - In "He _wants_ to go home." the verb _want_ does not require any personal energy

## What is the Aspect Hypothesis?
The Aspect Hypothesis is a general set of predictions for how children (in most languages) first start to use inflectional markers for tense 
and aspect with respect to the above notions of grammatical aspect and the four verb types (Shirai & Andersen, 1995).

It states:
1. Children first use past/perfective marking predominantly with achievement and accomplishment verbs, eventually extending their use to activity and finally to stative verbs.
2. In languages that have progressive aspect, children first use progressive marking mostly with activity verbs, then extending it to accomplishment and achievement verbs.
3. Children do not incorrectly overextend progressive markings to stative verbs.

Notably, the telic verb types, which denote end points, correspond to past perfect marking, which denotes event 
completion. 
Meanwhile, the atelic verb types, which denote ambiguous end points, correspond to present progressive marking, which 
denotes incomplete events.

## Corpus Analysis
This repository contains scripts that allow for the extraction of aspectual (lexical and grammatical) features from 
large-scale child and caregiver speech production data from the CHILDES database of child and child-directed speech
using NLP. It can be used to assess how well the predictions of the Aspect Hypothesis are upheld within extremely large 
sets of data that document speech production across a range of target child ages, from infancy into early childhood.

More specifically, two NLP packages (SpaCy and Stanza) are employed to extract the relevant features for analysis:
- main_verb: the main inflected/root verb of an utterance
  - In "She is walking to school", _walking_ is the main verb.
- lemma: the base form of the main verb
  - If the main verb is _walking_, the lemma is _walk_.
- inflection: a code that marks the form of the main verb
- grammatical_aspect: the code for the tense and aspect of an utterance

In addition, the main verb of each utterance is manually classified according to its Vendler classification.

These features, along with utterances, indices, and speaker information, are extracted by both SpaCy and Stanza and 
saved in two CSV files: one where the two packages agree on the main verb of the utterance, and one where they 
disagree. Due to the imperfect nature of NLP, manual correction is unavoidable and necessary for accurate analyses, 
especially with speech production data from children who are still learning their first language. Splitting the 
processed data into agreements and disagreements better allows you to identify cases where one NLP module might be 
more effective than the other at main verb recognition and manually deciding whether to go with one over the other.

While the current purpose of the scripts are to compare child and caregiver speech usage of the four verb types in 
combination with either past perfect or present progressive aspect, the class structure it uses can be optimized for 
other purposes depending on what other features need to be extracted for a different analysis, making it useful for 
speech production analyses in general.


## Installation
```
# Install required dependencies
pip install -r requirements.txt

# Process corpus data
python corpus_analysis.py

# Run the statistical analysis
python statistical_analysis.py
```

## Testing
### Processing Data
A sample raw dataset organized as expected by the script is provided in `tests/` as a CSV file (sample_raw_data.csv).
The file path for it is already coded into `corpus_analysis.py` for testing purposes.

When running `corpus_analysis.py`, you will first see in the terminal that Stanza is loading in its models for English: 
tokenize, mwt, pos, lemma, and depparse. Once it's done loading, it should print "Done loading processors!"
Then, you will be prompted to enter the minimum and maximum age values that you want to process data for in days. This 
is included as an option because you may only be interested in a certain target child age range, or you may want to 
process data in batches for time's sake (processing a large range can take a while). In the test file, the lowest age 
is 330 days, while the maximum is 3568.

Once entered, you will see "Processing data for minimum age to maximum age..."
If there is no data for that age range within the file, you will see "No data found for ages minimum age-maximum age."
Otherwise, depending on the range you entered you may have to wait a bit for the entire set of data to be processed by 
each NLP package. As you wait, if there are at least 100 documents in the range of data being processed, you will see 
print statements like "Corpus has 100 documents" for every hundred documents that have been processed so far, 
indicating the progress that has been made by the current package that is processing the data (SpaCy first, Stanza 
second). Once the first package is done, you will know that the second package is processing data as the print 
statements will reset their counts, going back down to "Corpus has 100 documents."

Once both packages are done, you will know that everything worked successfully if, upon the program finishing, the 
terminal prints how many documents there are in SpaCy and Stanza's corpora, and a new directory called `processed_data` 
has been created with two files inside: agreement_df.csv and disagreement_df.csv.
- In agreement_df.csv, there should be 16 columns in this order, with values in SpaCy Main Verb and Stanza Main Verb being the same verb:
  - Utterance Index
  - Document Name
  - Transcript Index
  - Target Child Age
  - Speaker ID
  - Utterance
  - SpaCy Main Verb
  - SpaCy Lemma
  - SpaCy Verb Type
  - SpaCy Inflection
  - SpaCy Grammatical Aspect
  - Stanza Main Verb
  - Stanza Lemma
  - Stanza Verb Type
  - Stanza Inflection
  - Stanza Grammatical Aspect
- disagreement_df.csv should look exactly like agreement_df.csv with the exception that values in the SpaCy Main Verb and Stanza Main Verb columns should differ.

### Analyzing Data
A sample processed dataset is organized as expected by the script is provided in `tests/` as a CSV file 
(sample_processed_data.csv). The file path for it is already coded into `statistical_analysis.py` for testing purposes.

Upon running `statistical_analysis.py`, it will have worked if it creates a new directory called `analyses/` containing 
a set of three CSV files:
1. aggregate_proportions_Caregiver.csv
2. aggregate_proportions_Child.csv
3. verb_counts.csv

These files will contain data frames of simple proportions and counts calculated from the processed data generated in 
`corpus_analysis.py`.

`analyses/` should also contain a directory called `figures/` containing three png images plotting those calculations:
1. aggregate_proportions_Caregiver.png
2. aggregate_proportions_Child.png
3. token_counts.png

## Code Structure
- `src/`
  - `corpus_token.py` - defines the `Token` class
  - `utterance.py` - defines the `Utterance` class
  - `document.py` - defines the `Document` class
  - `corpus.py` - defines the `Corpus` class
  - `replacements.py` - a dictionary of verbs with exceptional spellings that should be replaced with more standardized spelling
  - `vendler_classification.py` - a dictionary of verbs classified as one or a combination of the four Vendler classifications
  - `corpus_analysis.py` - extracts aspectual features from corpus data
  - `statistical_analysis.py` - calculates proportions and plots them

## References
Shirai, Y., & Andersen, R. W. (1995). The acquisition of tense-aspect morphology: A prototype account. Language, 743-762. https://doi.org/10.2307/415743

Vendler, Z. (1967). _Linguistics in Philosophy_. Ithaca, NY: Cornell University Press. https://doi.org/10.7591/9781501743726
