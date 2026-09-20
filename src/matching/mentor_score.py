def calculate_expertise_score(candidate, mentor):
    """
    Calculate how many of the mentor's expertise
    areas match the candidate's skills.
    """

    if not candidate.skills:
        return 0

    mentor_expertise = [
        skill.lower().strip()
        for skill in mentor["expertise"]
    ]

    candidate_skills = [
        skill.lower().strip()
        for skill in candidate.skills
    ]

    matched_skills = 0

    for mentor_skill in mentor_expertise:

        for candidate_skill in candidate_skills:

            if (
                mentor_skill in candidate_skill
                or candidate_skill in mentor_skill
            ):
                matched_skills += 1
                break

    score = (
        matched_skills
        / len(mentor_expertise)
    ) * 100

    return round(score, 2)


def calculate_track_score(
    candidate,
    mentor
):
    """
    Check whether the candidate's career
    interests match the mentor's track.
    """

    if not candidate.career_interests:
        return 0

    track = mentor["track"].lower()

    matched = 0

    for interest in candidate.career_interests:

        if (
            interest.lower() in track
            or track in interest.lower()
        ):
            matched += 1

    score = (
        matched
        / len(candidate.career_interests)
    ) * 100

    return round(score, 2)


def calculate_experience_score(mentor):
    """
    Convert mentor experience into a
    normalized experience score.
    """

    experience = mentor["experience_years"]

    max_experience = 10

    score = (
        experience
        / max_experience
    ) * 100

    return round(
        min(score, 100),
        2
    )


def calculate_mentor_score(
    expertise_score,
    semantic_score,
    track_score,
    experience_score
):
    """
    Calculate the final mentor matching score.
    """

    final_score = (
        expertise_score * 0.35
        + semantic_score * 0.35
        + track_score * 0.20
        + experience_score * 0.10
    )

    return round(
        final_score,
        2
    )


if __name__ == "__main__":

    expertise_score = 75
    semantic_score = 85
    track_score = 100
    experience_score = 50

    mentor_score = calculate_mentor_score(
        expertise_score,
        semantic_score,
        track_score,
        experience_score
    )

    print(
        "\n========== MENTOR SCORE =========="
    )

    print(
        f"Expertise Match: "
        f"{expertise_score}%"
    )

    print(
        f"Semantic Match: "
        f"{semantic_score}%"
    )

    print(
        f"Track Match: "
        f"{track_score}%"
    )

    print(
        f"Experience Score: "
        f"{experience_score}%"
    )

    print(
        "----------------------------------"
    )

    print(
        f"Final Mentor Score: "
        f"{mentor_score}%"
    )

    print(
        "=================================="
    )