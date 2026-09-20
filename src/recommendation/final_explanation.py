def generate_final_explanation(
    track_explanation,
    strengths,
    weaknesses,
    skill_gap_explanation,
    mentor_explanation,
    roadmap_summary
):
    """
    Combine all recommendation explanations
    into one final explainable summary.
    """

    final_explanation = {

        "recommended_track": (
            track_explanation["track"]
        ),

        "track_score": (
            track_explanation["final_score"]
        ),

        "track_reason": (
            track_explanation["reason"]
        ),

        "strengths": strengths,

        "weaknesses": weaknesses,

        "skill_gap_explanation": (
            skill_gap_explanation
        ),

        "recommended_mentor": (
            mentor_explanation["mentor"]
        ),

        "mentor_score": (
            mentor_explanation["final_score"]
        ),

        "mentor_reason": (
            mentor_explanation["reason"]
        ),

        "roadmap_summary": roadmap_summary
    }

    return final_explanation


if __name__ == "__main__":

    track_explanation = {

        "track": "AI / Machine Learning",

        "final_score": 66.4,

        "reason": (
            "The AI / Machine Learning track "
            "was recommended because the candidate "
            "shows strong alignment in skills, "
            "semantic similarity, projects, "
            "career interests, education, "
            "portfolio, and certifications."
        )
    }

    strengths = [

        {
            "category": "Technical Skills",

            "details": (
                "Candidate has 5 skills relevant "
                "to the recommended track."
            ),

            "items": [
                "Python",
                "Machine Learning",
                "Artificial Intelligence",
                "Generative AI",
                "Scikit-learn"
            ]
        },

        {
            "category": "Projects",

            "details": (
                "Candidate has 3 relevant projects "
                "demonstrating practical experience."
            ),

            "items": [
                "Medical AI Assistant",
                "Student Data Analysis",
                "Internship Recommendation Engine"
            ]
        }
    ]

    weaknesses = [

        {
            "category": "Missing Skills",

            "details": (
                "Candidate is missing 3 skills "
                "required or useful for the track."
            ),

            "items": [
                "Deep Learning",
                "Computer Vision",
                "Natural Language Processing"
            ]
        }
    ]

    skill_gap_explanation = (
        "The candidate should strengthen "
        "Deep Learning, Computer Vision, "
        "and Natural Language Processing "
        "through the personalized learning roadmap."
    )

    mentor_explanation = {

        "mentor": "Aamir Khan",

        "final_score": 63.73,

        "reason": (
            "Aamir Khan was recommended because "
            "the mentor shows strong alignment "
            "in Expertise Match and Semantic Match."
        )
    }

    roadmap_summary = {

        "total_steps": 3,

        "completed_steps": 1,

        "in_progress_steps": 1,

        "not_started_steps": 1,

        "overall_progress": 50.0,

        "total_duration_weeks": 9
    }

    final_explanation = generate_final_explanation(

        track_explanation,

        strengths,

        weaknesses,

        skill_gap_explanation,

        mentor_explanation,

        roadmap_summary
    )

    print(
        "\n========== FINAL EXPLAINABLE RECOMMENDATION =========="
    )

    print(
        "\nRecommended Track:"
    )

    print(
        final_explanation["recommended_track"]
    )

    print(
        "Track Score:",
        f"{final_explanation['track_score']}%"
    )

    print(
        "\nWhy This Track:"
    )

    print(
        final_explanation["track_reason"]
    )

    print(
        "\nStrengths:"
    )

    for strength in (
        final_explanation["strengths"]
    ):

        print(
            f"- {strength['category']}: "
            f"{strength['details']}"
        )

    print(
        "\nWeaknesses:"
    )

    for weakness in (
        final_explanation["weaknesses"]
    ):

        print(
            f"- {weakness['category']}: "
            f"{weakness['details']}"
        )

    print(
        "\nSkill Gap Explanation:"
    )

    print(
        final_explanation[
            "skill_gap_explanation"
        ]
    )

    print(
        "\nRecommended Mentor:"
    )

    print(
        final_explanation[
            "recommended_mentor"
        ]
    )

    print(
        "Mentor Score:",
        f"{final_explanation['mentor_score']}%"
    )

    print(
        "\nWhy This Mentor:"
    )

    print(
        final_explanation[
            "mentor_reason"
        ]
    )

    print(
        "\nLearning Roadmap:"
    )

    roadmap = final_explanation[
        "roadmap_summary"
    ]

    print(
        f"- Total Steps: "
        f"{roadmap['total_steps']}"
    )

    print(
        f"- Completed: "
        f"{roadmap['completed_steps']}"
    )

    print(
        f"- In Progress: "
        f"{roadmap['in_progress_steps']}"
    )

    print(
        f"- Not Started: "
        f"{roadmap['not_started_steps']}"
    )

    print(
        f"- Overall Progress: "
        f"{roadmap['overall_progress']}%"
    )

    print(
        f"- Estimated Duration: "
        f"{roadmap['total_duration_weeks']} weeks"
    )

    print(
        "\n======================================================="
    )