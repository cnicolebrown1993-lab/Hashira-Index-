import json
with open("data/questions.json", "r", encoding="utf-8") as file:
    data = json.load(file)

questions = data["questions"]

def apply_weights(scores, weights):
    for dimension, value in weights.items():
        scores[dimension] += value

    return scores

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

test_scores = {dimension: 0 for dimension in DIMENSIONS}

test_answers = ["B", "D", "A"]

for question, answer in zip(questions, test_answers):
    for response in question["responses"]:
        if response["id"] == answer:
            apply_weights(test_scores, response["weights"])

print(test_scores)

