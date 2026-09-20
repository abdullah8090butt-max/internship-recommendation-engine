def normalize_similarity_scores(ranked_tracks):
    if not ranked_tracks:
        return []

    scores = [
        track["score"]
        for track in ranked_tracks
    ]

    highest_score = max(scores)

    if highest_score <= 0:
        for track in ranked_tracks:
            track["match_score"] = 0.0

        return ranked_tracks

    for track in ranked_tracks:

        relative_score = (
            track["score"] / highest_score
        ) * 100

        # Prevent negative recommendation scores.
        relative_score = max(
            0,
            relative_score
        )

        track["match_score"] = round(
            relative_score,
            2
        )

    return ranked_tracks


if __name__ == "__main__":

    ranked_tracks = [
        {
            "name": "AI / Machine Learning",
            "score": 0.6848
        },
        {
            "name": "Data Science",
            "score": 0.6040
        },
        {
            "name": "Cybersecurity",
            "score": 0.2007
        },
        {
            "name": "Web Development",
            "score": 0.1711
        }
    ]

    scored_tracks = normalize_similarity_scores(
        ranked_tracks
    )

    print("\n========== MATCH SCORES ==========")

    for track in scored_tracks:
        print(
            f"{track['name']} → "
            f"{track['match_score']}%"
        )

    print("==================================")