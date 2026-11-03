"""Treasure Island Quiz - a small terminal quiz game (Maths and Science)."""

# Each question: prompt text + list of accepted answers.
# Answers are normalised (lower-case, no spaces, no "*", no trailing "+c", no "%"),
# so "Sin(x) cos(x)", "2*sin(x)*cos(x)" etc. all match.
MATHS = [
    ("What is the square root of 49?", ["7"]),
    (
        "A stock first falls 90%, then falls another 80% of its new value. "
        "What is the total percentage fall?",
        ["98"],
    ),
    ("What is the integral of sin(x)?", ["-cos(x)", "-cosx"]),
    ("What is the derivative of ln(x)?", ["1/x", "x^-1"]),
    (
        "What is sin(2x)?",
        ["2sin(x)cos(x)", "2sinxcosx", "2cos(x)sin(x)", "2cosxsinx"],
    ),
    ("What is 3!?", ["6"]),
    ("What is the sum of the cubes of 12 and 1?", ["1729"]),
    (
        "What is the integral of ln(x)?",
        ["xln(x)-x", "xlnx-x", "x(ln(x)-1)", "x(lnx-1)", "(ln(x)-1)x"],
    ),
]

SCIENCE = [
    ("What is the SI unit of electric current?", ["ampere", "amp", "a"]),
    ("Which lens is used to correct myopia?", ["concavelens", "concave", "diverginglens"]),
    (
        "What is the splitting of white light into its constituent colours called?",
        ["dispersion"],
    ),
    (
        "Which device converts electrical energy into mechanical energy?",
        ["electricmotor", "motor"],
    ),
    ("What is the SI unit of electrical resistance?", ["ohm"]),
    (
        "Which gas is released at the cathode during the electrolysis of water?",
        ["hydrogen", "h2"],
    ),
    (
        "What is the phenomenon responsible for the blue colour of the sky?",
        ["scattering", "rayleighscattering", "scatteringoflight"],
    ),
    (
        "Which part of the human eye controls the amount of light entering it?",
        ["pupil", "iris"],
    ),
]

SUBJECTS = {"1": ("Maths", MATHS), "2": ("Science", SCIENCE)}


def normalize(text: str) -> str:
    """Make free-text answers comparable."""
    text = text.lower().replace(" ", "").replace("*", "").replace("%", "")
    if text.endswith("+c"):
        text = text[:-2]
    return text


def is_correct(user_answer: str, accepted: list[str]) -> bool:
    return normalize(user_answer) in {normalize(a) for a in accepted}


def grade(score: int, total: int) -> str:
    ratio = score / total
    if ratio >= 0.75:
        return "Excellent!"
    if ratio >= 0.5:
        return "Good"
    return "Try again!"


def choose_subject() -> tuple[str, list]:
    while True:
        choice = input("1. Maths\n2. Science\nChoose a subject: ").strip()
        if choice in SUBJECTS:
            return SUBJECTS[choice]
        print("Please enter 1 or 2.")


def run_quiz(questions: list) -> int:
    score = 0
    for number, (prompt, accepted) in enumerate(questions, start=1):
        print(f"\n{number}. {prompt}")
        answer = input("Your answer: ")
        if is_correct(answer, accepted):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer was: {accepted[0]}")
    return score


def main() -> None:
    name = input("Your name: ").strip() or "Player"
    print("\n===== TREASURE ISLAND =====")

    while True:
        input("Press Enter to start: ")
        subject, questions = choose_subject()
        score = run_quiz(questions)

        print("\n** GAME END **")
        print(f"{name}, your {subject} score: {score}/{len(questions)} - {grade(score, len(questions))}")

        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()