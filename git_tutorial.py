"""Module for demonstrating basic Python functionality and Git tutorial examples."""

from typing import Final


# Constants at module level using snake_case
USER_NAME: Final[str] = "Peter"
USER_AGE: Final[int] = 20

def add_numbers(first_num: int, second_num: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        first_num: First number to add
        second_num: Second number to add

    Returns:
        int: The sum of the two input numbers
    """
    return first_num + second_num


def main() -> None:
    """Run the main program logic."""
    # Group related operations together
    print("Hello, World!")
    result = add_numbers(1, 2)
    print(f"Sum result: {result}")
    print(f"Name: {USER_NAME}, Age: {USER_AGE}")


if __name__ == "__main__":
    main()
