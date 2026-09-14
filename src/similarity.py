import json
import math

from scoring import DIMENSIONS


def load_profiles():
    with open("data/profiles.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["profiles"]


def euclidean_distance(user_scores, profile_scores):
    squared_differences = []

    for dimension in DIMENSIONS:
        difference = (
            user_scores[dimension]
            - profile_scores[dimension]
        )

        squared_differences.append(
            difference ** 2
        )

    return math.sqrt(
        sum(squared_differences)
    )


def calculate_similarities(user_scores, profiles):
    similarities = {}

    for name, profile_scores in profiles.items():
        distance = euclidean_distance(
            user_scores,
            profile_scores
        )

        similarity = 1 / (1 + distance)

        similarities[name] = similarity

    return similarities


def normalize_similarities(similarities):
    total = sum(similarities.values())

    percentages = {}

    for name, similarity in similarities.items():
        percentages[name] = round(
            100 * similarity / total,
            2
        )

    return percentages