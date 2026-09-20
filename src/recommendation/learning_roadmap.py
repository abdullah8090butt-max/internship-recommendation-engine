from matching.skill_scorer import TRACK_SKILLS


SKILL_LEARNING_INFO = {

    "deep learning": {
        "stage": "Intermediate",
        "duration": "3 weeks",
        "resource_type": "Deep Learning course/tutorial",
        "milestone": "Build and train a basic neural network"
    },

    "computer vision": {
        "stage": "Intermediate",
        "duration": "3 weeks",
        "resource_type": "Computer Vision course/tutorial",
        "milestone": "Build a basic image classification project"
    },

    "natural language processing": {
        "stage": "Intermediate",
        "duration": "3 weeks",
        "resource_type": "NLP course/tutorial",
        "milestone": "Build a basic text classification project"
    },

    "data science": {
        "stage": "Beginner",
        "duration": "2 weeks",
        "resource_type": "Data Science course/tutorial",
        "milestone": "Complete a basic data science project"
    },

    "data analysis": {
        "stage": "Beginner",
        "duration": "2 weeks",
        "resource_type": "Data Analysis course/tutorial",
        "milestone": "Analyze and visualize a real dataset"
    },

    "statistics": {
        "stage": "Beginner",
        "duration": "2 weeks",
        "resource_type": "Statistics course/tutorial",
        "milestone": "Understand fundamental statistics concepts"
    },

    "visualization": {
        "stage": "Beginner",
        "duration": "1 week",
        "resource_type": "Data Visualization course/tutorial",
        "milestone": "Create meaningful data visualizations"
    }
}


SKILL_ORDER = {

    "deep learning": 1,
    "computer vision": 2,
    "natural language processing": 3,

    "data science": 1,
    "data analysis": 2,
    "statistics": 3,
    "visualization": 4
}


STATUS_PROGRESS = {

    "Not Started": 0,

    "In Progress": 50,

    "Completed": 100
}


def create_learning_roadmap(
    missing_skills,
    track_name
):
    """
    Create an ordered personalized
    learning roadmap.
    """

    if not missing_skills:
        return []

    roadmap = []

    for skill in missing_skills:

        if not skill:
            continue

        skill_key = str(skill).strip().lower()

        learning_info = (
            SKILL_LEARNING_INFO.get(
                skill_key,
                {
                    "stage": "Beginner",
                    "duration": "2 weeks",
                    "resource_type": (
                        f"{skill} course/tutorial"
                    ),
                    "milestone": (
                        f"Complete a basic {skill} project"
                    )
                }
            )
        )

        sequence = SKILL_ORDER.get(
            skill_key,
            99
        )

        status = "Not Started"

        roadmap.append({

            "skill": skill,

            "track": track_name,

            "sequence": sequence,

            "priority": "High",

            "stage": learning_info[
                "stage"
            ],

            "duration": learning_info[
                "duration"
            ],

            "resource_type": learning_info[
                "resource_type"
            ],

            "milestone": learning_info[
                "milestone"
            ],

            "status": status,

            "progress": STATUS_PROGRESS[
                status
            ]
        })

    roadmap.sort(
        key=lambda item: item["sequence"]
    )

    return roadmap


def update_skill_status(
    roadmap,
    skill_name,
    new_status
):
    """
    Update roadmap skill status.
    """

    if not roadmap:
        return roadmap

    if not skill_name:
        return roadmap

    if new_status not in STATUS_PROGRESS:
        return roadmap

    for item in roadmap:

        if (
            item["skill"].lower()
            == str(skill_name).strip().lower()
        ):

            item["status"] = new_status

            item["progress"] = (
                STATUS_PROGRESS[
                    new_status
                ]
            )

    return roadmap


def calculate_overall_progress(roadmap):
    """
    Calculate overall roadmap progress.
    """

    if not roadmap:
        return 0

    total_progress = sum(
        item.get("progress", 0)
        for item in roadmap
    )

    return round(
        total_progress / len(roadmap),
        2
    )


def generate_roadmap_summary(roadmap):
    """
    Generate roadmap summary.
    """

    if not roadmap:

        return {
            "total_steps": 0,
            "completed_steps": 0,
            "in_progress_steps": 0,
            "not_started_steps": 0,
            "overall_progress": 0
        }

    completed_steps = 0
    in_progress_steps = 0
    not_started_steps = 0

    for item in roadmap:

        if item["status"] == "Completed":
            completed_steps += 1

        elif item["status"] == "In Progress":
            in_progress_steps += 1

        elif item["status"] == "Not Started":
            not_started_steps += 1

    return {

        "total_steps": len(roadmap),

        "completed_steps": completed_steps,

        "in_progress_steps": in_progress_steps,

        "not_started_steps": not_started_steps,

        "overall_progress": (
            calculate_overall_progress(
                roadmap
            )
        )
    }


def calculate_total_duration(roadmap):
    """
    Calculate total estimated learning duration.
    """

    if not roadmap:
        return 0

    total_weeks = 0

    for item in roadmap:

        duration = item.get(
            "duration",
            ""
        )

        try:

            number = int(
                duration.split()[0]
            )

            total_weeks += number

        except (
            ValueError,
            IndexError
        ):

            continue

    return total_weeks


def generate_personalized_roadmap(
    missing_skills,
    track_name
):
    """
    Main roadmap integration function.

    Creates the roadmap, calculates progress,
    generates the summary, and calculates
    total estimated duration.
    """

    roadmap = create_learning_roadmap(
        missing_skills,
        track_name
    )

    summary = generate_roadmap_summary(
        roadmap
    )

    total_duration = (
        calculate_total_duration(
            roadmap
        )
    )

    return {

        "track": track_name,

        "roadmap": roadmap,

        "summary": summary,

        "total_duration_weeks": (
            total_duration
        )
    }


if __name__ == "__main__":

    track_name = "AI / Machine Learning"

    required_skills = TRACK_SKILLS[
        track_name
    ]

    candidate_skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Generative AI",
        "Scikit-learn"
    ]

    candidate_skills = [
        skill.lower()
        for skill in candidate_skills
    ]

    missing_skills = []

    for skill in required_skills:

        if skill.lower() not in candidate_skills:

            missing_skills.append(
                skill
            )

    result = generate_personalized_roadmap(
        missing_skills,
        track_name
    )

    roadmap = result["roadmap"]

    roadmap = update_skill_status(
        roadmap,
        "deep learning",
        "In Progress"
    )

    roadmap = update_skill_status(
        roadmap,
        "computer vision",
        "Completed"
    )

    result["summary"] = (
        generate_roadmap_summary(
            roadmap
        )
    )

    print(
        "\n========== FINAL PERSONALIZED ROADMAP =========="
    )

    print(
        "Track:",
        result["track"]
    )

    for item in roadmap:

        print(
            f"\nStep {item['sequence']}: "
            f"{item['skill']}"
        )

        print(
            f"Priority: "
            f"{item['priority']}"
        )

        print(
            f"Stage: "
            f"{item['stage']}"
        )

        print(
            f"Duration: "
            f"{item['duration']}"
        )

        print(
            f"Resource: "
            f"{item['resource_type']}"
        )

        print(
            f"Milestone: "
            f"{item['milestone']}"
        )

        print(
            f"Status: "
            f"{item['status']}"
        )

        print(
            f"Progress: "
            f"{item['progress']}%"
        )

    print(
        "\n--------------- ROADMAP SUMMARY ---------------"
    )

    summary = result["summary"]

    print(
        f"Total Steps: "
        f"{summary['total_steps']}"
    )

    print(
        f"Completed: "
        f"{summary['completed_steps']}"
    )

    print(
        f"In Progress: "
        f"{summary['in_progress_steps']}"
    )

    print(
        f"Not Started: "
        f"{summary['not_started_steps']}"
    )

    print(
        f"Overall Progress: "
        f"{summary['overall_progress']}%"
    )

    print(
        f"Total Estimated Duration: "
        f"{result['total_duration_weeks']} weeks"
    )

    print(
        "================================================"
    )