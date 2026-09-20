from matching.semantic_matcher import get_model


def generate_embedding(text):

    model = get_model()

    embedding = model.encode(
        text
    )

    return embedding


if __name__ == "__main__":

    candidate_text = """
    Skills: Python, Machine Learning, Artificial Intelligence
    Education: FSc ICS
    Certifications: AI Fundamentals
    Career Interests: Artificial Intelligence, Generative AI
    Projects: Medical AI Assistant, Student Data Analysis
    """

    embedding = generate_embedding(
        candidate_text
    )

    print(
        "Embedding generated successfully!"
    )

    print(
        "Embedding shape:",
        embedding.shape
    )

    print(
        "First 10 values:",
        embedding[:10]
    )