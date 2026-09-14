from scoring import load_questions, score_assessment
from normalization import calculate_bounds, normalize_scores
from similarity import (
    load_profiles,
    calculate_similarities,
    normalize_similarities
)


questions = load_questions()
profiles = load_profiles()

test_answers = ["B", "D", "A"]

raw_scores = score_assessment(
    questions,
    test_answers
)

minimums, maximums = calculate_bounds(
    questions
)

normalized_scores = normalize_scores(
    raw_scores,
    minimums,
    maximums
)

similarities = calculate_similarities(
    normalized_scores,
    profiles
)

percentages = normalize_similarities(
    similarities
)

print("NORMALIZED SCORES")
print(normalized_scores)

print()

print("HASHIRA MATCHES")

for name, percentage in sorted(
    percentages.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(name, percentage)