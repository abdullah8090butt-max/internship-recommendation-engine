from nlp.skill_normalizer import normalize_skills


def normalize_candidate_skills(candidate):
    candidate.skills = normalize_skills(
        candidate.skills
    )

    return candidate


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.skills = [
        "Python",
        "ML",
        "AI",
        "sklearn",
        "np",
        "pd"
    ]

    print(
        "Original Skills:",
        test_candidate.skills
    )

    test_candidate = normalize_candidate_skills(
        test_candidate
    )

    print(
        "Normalized Skills:",
        test_candidate.skills
    )