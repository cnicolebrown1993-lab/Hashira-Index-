import json

DIMENSIONS = [
    "SI",
    "SR",
    "DS",
    "ET",
    "AU",
    "EE",
    "CC",
    "LM",
    "FT",
    "RS",
    "CW"
]


def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["questions"]


def apply_weights(scores, weights):
    for dimension, value in weights.items():
        scores[dimension] += value

    return scores


def score_assessment(questions, answers):
    scores = {dimension: 0 for dimension in DIMENSIONS}

    for question, answer in zip(questions, answers):
        for response in question["responses"]:
            if response["id"] == answer:
                apply_weights(scores, response["weights"])
                break

    return scores


if __name__ == "__main__":
    questions = load_questions()

    test_answers = ["B", "D", "A"]

    raw_scores = score_assessment(
        questions,
        test_answers
    )

    print(raw_scores)