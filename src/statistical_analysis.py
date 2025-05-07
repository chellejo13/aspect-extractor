import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import random

verb_types = ["activity", "achievement", "accomplishment", "state"]
age_bin_order = ["0.5-1.0", "1.0-1.5", "1.5-2.0", "2.0-2.5", "2.5-3.0", "3.0-3.5", "3.5-4.0", "4.0-4.5"]

def assign_age_bin(age_days) -> str:
    """Converts target child age from days to years and assigns it to an age range.

    Args:
        age_days: a given target child age range in days

    Returns:
        str: the age bin (string) that the given age falls under
    """
    age_years = age_days / 365.0
    age_bins = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
    age_bin_labels = age_bin_order

    for i in range(len(age_bins) - 1):
        if age_bins[i] <= age_years < age_bins[i + 1]:
            return age_bin_labels[i]
    return None # returns None in case it doesn't fall into an age bin

def prep_data(file_path) -> pd.DataFrame:
    """Loads the raw data into a data frame and filters for cases where:
    1. The verb type falls under the globally-defined verb types above (no overlapping types)
    2. The grammatical aspect is either past perfect or present progressive.

    Args:
        file_path: The file path to the CSV of raw data

    Returns:
        pd.DataFrame: A data frame filtered for verb types and grammatical aspect
    """
    df = pd.read_csv(file_path)
    df = df[df["SpaCy Verb Type"].isin(verb_types)] # filter for cases where verbs only have one classification

    df["Aspect Type"] = df["SpaCy Grammatical Aspect"].apply(
        lambda x: "past" if x in ["{'Tense': 'Past', 'VerbForm': 'Fin'}",
                                  "{'Aspect': 'Perf', 'Tense': 'Past', 'VerbForm': 'Part'}"]
        else ("prog" if x == "{'Aspect': 'Prog', 'Tense': 'Pres', 'VerbForm': 'Part'}" else None)
    )
    df = df[df["Aspect Type"].notnull()]

    df["Age Bin"] = df["Target Child Age"].apply(assign_age_bin)
    df = df[df["Age Bin"].notnull()]
    df["Age Bin"] = pd.Categorical(df["Age_Bin"], categories=age_bin_order, ordered=True)
    return df

def count_verbs(df) -> pd.DataFrame:
    """Gets counts of types (unique verbs) and tokens (occurrences of each verb) from the prepared data frame

    Args:
        df: The data frame filtered for verb types and grammatical aspect

    Returns:
        pd.DataFrame: A data frame of type and token counts by each verb type
    """
    token_counts = df.groupby("SpaCy Verb Type").size().reset_index(name="Token Count")
    type_counts = df.groupby("SpaCy Verb Type")["SpaCy Lemma"].nunique().reset_index(name="Type Count")

    count_df = pd.merge(token_counts, type_counts, on="SpaCy Verb Type")
    return count_df

def main():
    file_path = "../agreement_df.csv"
    df = prep_data(file_path)

    verb_counts = count_verbs(df)
    verb_counts.to_csv("../results/verb_counts.csv", index=False) # saves counts to csv

if __name__ == '__main__':
    main()