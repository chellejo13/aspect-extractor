# BCOG200 Final Project

The goal of this project is to write a program that (1) takes a large csv file of transcribed natural language from the 
CHILDES corpus (database of child and parent speech) as an input, (2) has a set of NLP modules (most likely SpaCy, 
Stanza, and one other module) run a set of analyses on that file, and (3) compiles the results into two data frames to 
allow me to compare the modules' accuracies. A program like this would be useful for someone (like me) who needs to 
classify features of transcribed data such as: the type of verb that is used in an utterance, or how it is inflected 
(e.g. present or past tense). Comparing NLP modules to each other is worthwhile because depending on the module, they 
may differ in the way they parse sentences (especially naturalistic speech, which is full of disfluencies and 
interruptions), where one may make mistakes in cases where another doesn't. The main idea is to organize the full set 
of data into three class levels: corpus, utterance, and token. At each level, attributes can be extracted using the NLP
tools. For example, at the utterance level, the main verb from each utterance can be extracted, but at the token level, 
the linguistic features of the verb itself can be extracted as well.

## Input data format
This program requires a csv file of utterances to be loaded in. It expects 16 columns with
information related to the utterance and assigns values to them (e.g. the speaker ID, the utterance index in the corpus,
etc.), so it will need to be organized accordingly.

## Example Use-Cases
This program will be useful for anyone working with large scale corpus data who wants to identify main verbs, classify
verbs based on their inherent telicity, and/or extract information about the tense and aspect of each utterance. These 
program functions are non-specific to my project and would definitely come in handy for other research topics within the 
realm of linguistics.

## Functions
The main three functions in my program will be:
1. A function that takes the path of the corpus file as an argument, loads the csv file, and creates class instances at each level as defined above.
2. A function (or more like a set of functions) that has each nlp module extract features from the full dataset at the utterance level and the token level and assigns those features to class attributes.
3. A function that separates the extracted features into two dataframes: one where all of the NLP modules agree on what the extracted features are, and one where they disagree (to be looked at for manual correction).