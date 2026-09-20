from data.internship_tracks import INTERNSHIP_TRACKS
from matching.semantic_matcher import get_model


def generate_track_embeddings():

    model = get_model()

    track_texts = [
        track["description"]
        for track in INTERNSHIP_TRACKS
    ]

    embeddings = model.encode(
        track_texts
    )

    return embeddings


if __name__ == "__main__":

    track_embeddings = generate_track_embeddings()

    print(
        "Track embeddings generated successfully!"
    )

    print(
        "Embedding shape:",
        track_embeddings.shape
    )

    for index, track in enumerate(
        INTERNSHIP_TRACKS
    ):

        print(
            f"{track['name']} → "
            f"{track_embeddings[index].shape}"
        )