def longest(text: str) -> str:
    """The longest word, the first of an equal pair."""
    return max(text.split(), key=len, default="")


if __name__ == "__main__":
    print(longest("a longer sentence here"))
