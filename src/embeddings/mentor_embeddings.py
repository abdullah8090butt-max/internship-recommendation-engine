from data.mentors import MENTORS
from matching.semantic_matcher import get_model


def create_mentor_text(mentor):
    """
    Convert mentor information into text
    for embedding generation.
    """

    expertise = ", ".join(
        mentor["expertise"]
    )

    text = (
        f"Track: {mentor['track']}. "
        f"Expertise: {expertise}. "
        f"Specialization: "
        f"{mentor['specialization']}."
    )

    return text


def generate_mentor_embeddings():

    model = get_model()

    mentor_texts = []

    for mentor in MENTORS:

        text = create_mentor_text(
            mentor
        )

        mentor_texts.append(text)

    embeddings = model.encode(
        mentor_texts
    )

    return mentor_texts, embeddings


if __name__ == "__main__":

    mentor_texts, embeddings = (
        generate_mentor_embeddings()
    )

    print(
        "\n========== MENTOR EMBEDDINGS =========="
    )

    print(
        "Number of mentors:",
        len(mentor_texts)
    )

    print(
        "Embedding shape:",
        embeddings.shape
    )

    for index, text in enumerate(
        mentor_texts
    ):

        print(
            f"\nMentor {index + 1}:"
        )

        print(
            "Text:",
            text
        )

        print(
            "Embedding dimensions:",
            len(embeddings[index])
        )

    print(
        "\n========================================"
    )