from scoring import DIMENSIONS


def calculate_bounds(questions):
    minimums = {dimension: 0 for dimension in DIMENSIONS}
    maximums = {dimension: 0 for dimension in DIMENSIONS}

    for question in questions:
        for dimension in DIMENSIONS:
            values = [
                response["weights"].get(dimension, 0)
                for response in question["responses"]
            ]

            minimums[dimension] += min(values)
            maximums[dimension] += max(values)

    return minimums, maximums


def normalize_scores(raw_scores, minimums, maximums):
    normalized_scores = {}

    for dimension in DIMENSIONS:
        raw = raw_scores[dimension]
        minimum = minimums[dimension]
        maximum = maximums[dimension]

        normalized = (
            100
            * (raw - minimum)
            / (maximum - minimum)
        )

        normalized_scores[dimension] = round(
            normalized,
            2
        )

    return normalized_scores