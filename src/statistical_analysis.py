import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
verb_types = ["activity", "achievement", "accomplishment", "state"]
age_bin_order = ["0.5-1.0", "1.0-1.5", "1.5-2.0", "2.0-2.5", "2.5-3.0", "3.0-3.5", "3.5-4.0", "4.0-4.5"]

# Prepare data frames
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
    df["Age Bin"] = pd.Categorical(df["Age Bin"], categories=age_bin_order, ordered=True)
    return df

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


# Calculations
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

def calculate_aggregate_proportions(df) -> pd.DataFrame:
    """Calculates the aggregate proportions of past perfect usage by each speaker at each age range for each verb type

    Args:
        df: The data frame filtered for verb types and grammatical aspect

    Returns:
        pd.DataFrame: A data frame of aggregate proportions for each verb type
    """
    proportions = []
    for verb_type in verb_types:
        grouped = (
            df.groupby(["Age Bin", "Speaker ID", "Aspect Type"], observed=True)
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )
        for aspect in ["past", "prog"]:
            if aspect not in grouped.columns:
                grouped[aspect] = 0
        grouped["Total"] = grouped["past"] + grouped["prog"]
        grouped["Proportion"] = grouped["past"] / grouped["Total"]
        grouped.loc[grouped["Total"] == 0, "Proportion"] = 0
        grouped["SpaCy Verb Type"] = verb_type

        proportions.append(grouped)

    return pd.concat(proportions, ignore_index=True)


# Plotting functions
def plot_verb_counts_by_speaker(child_df, caregiver_df) -> None:
    """Plots the number of verbs occurring at each age range for children and caregivers for each verb type (four
    sub-barplots).

    Args:
        child_df: data frame filtered for child utterances
        caregiver_df: data frame filtered for caregiver utterances
    """
    output_dir = "../analyses/figures/"
    os.makedirs(output_dir, exist_ok=True)

    bar_fig, axes = plt.subplots(2, 2, figsize=(16, 10), sharey=True)
    subplot_order = {"achievement": 0, "accomplishment": 1, "activity": 2, "state": 3}
    color_palette = {"Child": "#c7817d", "Caregiver": "#88b2ac"}

    for verb_type, index in subplot_order.items():
        ax = axes[index // 2, index % 2]
        child_counts = (child_df[child_df["SpaCy Verb Type"] == verb_type].groupby("Age Bin", observed=True).size()
                        .reindex(age_bin_order, fill_value=0))
        caregiver_counts = (caregiver_df[caregiver_df["SpaCy Verb Type"] == verb_type].groupby("Age Bin", observed=True)
                            .size().reindex(age_bin_order, fill_value=0))

        plot_data = pd.DataFrame({
            "Age Bin": age_bin_order * 2,
            "Token Count": list(child_counts.values) + list(caregiver_counts.values),
            "Group": ["Child"] * len(age_bin_order) + ["Caregiver"] * len(age_bin_order),
        })

        sns.barplot(x="Age Bin", y="Token Count", hue="Group", data=plot_data, ax=ax, palette=color_palette, dodge=True)

        ax.set_title(f"{verb_type.capitalize()}")
        ax.set_xlabel("Age Bin")
        ax.set_ylabel("Token Count")
        ax.tick_params(axis="x", rotation=0)

    handles, labels = ax.get_legend_handles_labels()
    bar_fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=2, frameon=False, fontsize=12)
    bar_fig.suptitle("Token Counts by Verb Type for Children and Caregivers", fontsize=18)
    plt.tight_layout()
    plt.savefig("../analyses/figures/token_counts.png")
    plt.close()

def plot_aggregate_proportions(aggregate_df, speaker_label) -> None:
    """Plots the aggregated proportions of verbs occurring in the past perfect at each age range for each verb type,
    separately for each speaker.

    Args:
        aggregate_df: the aggregated proportions of past perfect for each verb type at each age range for either child
        or caregiver
        speaker_label: child or caregiver label
    """
    output_dir = "../analyses/figures/"
    os.makedirs(output_dir, exist_ok=True)

    bar_fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 10), sharey=True)
    plot_config = {
        "achievement": (0, r"Achievement"),
        "accomplishment": (1, r"Accomplishment"),
        "activity": (2, r"Activity"),
        "state": (3, r"State"),
    }

    for verb_type, (index, title) in plot_config.items():
        ax = axes[index // 2, index % 2]
        data = aggregate_df[aggregate_df["SpaCy Verb Type"] == verb_type]
        sns.barplot(x="Age Bin", y="Proportion", data=data, ax=ax, errorbar=None, label="Past Perfect Proportion")

        ax.set_title(title, fontsize=14)
        ax.set_xlabel("Age Bin")
        ax.set_ylabel("Proportion of Past Perfect")
        ax.tick_params(axis="x", rotation=0)
        ax.set_ylim(0, 1)
        ax.legend()

    bar_fig.suptitle(f"Past Perfect Proportions by Verb Type for {speaker_label}", fontsize=18)
    plt.tight_layout()
    plt.savefig(f"../analyses/figures/aggregate_proportions_{speaker_label}.png")
    plt.close()


def main():
    output_dir = "../analyses/"
    os.makedirs(output_dir, exist_ok=True)

    file_path = "../tests/sample_processed_data.csv"
    df = prep_data(file_path)

    # Get a summary of type and token counts for each verb type
    verb_counts = count_verbs(df)
    verb_counts.to_csv("../analyses/verb_counts.csv", index=False) # saves counts to csv

    df["Speaker Group"] = df["Speaker ID"].apply(lambda x: "Child" if x == "CHI" else "Caregiver") # assigns the speaker IDs to speaker labels
    child_df = df[df["Speaker ID"] == "CHI"].copy()
    caregiver_df = df[df["Speaker ID"].isin(["MOT", "FAT"])].copy()

    # Plot verb token counts for each speaker at each age range for each verb type
    plot_verb_counts_by_speaker(child_df, caregiver_df)

    # Calculate and plot aggregate proportions of past perfect usage for each verb type by speaker (child and caregiver)
    for speaker_df, label in [(child_df, "Child"), (caregiver_df, "Caregiver")]:
        aggregate_df = calculate_aggregate_proportions(speaker_df)
        aggregate_df.to_csv(f"../analyses/aggregate_proportions_{label}.csv", index=False) # saves proportions to csv
        plot_aggregate_proportions(aggregate_df, label)

if __name__ == '__main__':
    main()