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
and aspect with respect to the above notions of grammatical aspect and the four verb types.

It states:
1. Children first use past/perfective marking predominantly with achievement and accomplishment verbs, eventually extending their use to activity and finally to stative verbs.
2. In languages that have progressive aspect, children first use progressive marking mostly with activity verbs, then extending it to accomplishment and achievement verbs.
3. Children do not incorrectly overextend progressive markings to stative verbs.

Notably, the telic verb types, which denote end points, correspond to past perfect marking, which denotes event 
completion. 
Meanwhile, the atelic verb types, which denote ambiguous end points, correspond to present progressive marking, which 
denotes incomplete events.

## Corpus Analysis


## Installation
```bash
# Install required dependencies
pip install -r requirements.txt

# Process corpus data
python corpus_analysis.py

# Run the statistical analysis
python statistical_analysis.py
```

## Testing


## References
