def recommend_movies(user_input: str) -> str:
    """
    Takes the user's input (string) and returns a recommendation (string)
    based on rule-based keyword checks.
    """

    # Normalize input to lowercase so checks are case-insensitive
    text = user_input.lower()

    # Rule 1 – Action Movies
    if any(word in text for word in ["action", "fight", "superhero"]):
        return "You might like: John Wick, Mad Max: Fury Road, or The Dark Knight."

    # Rule 2 – Comedy Movies
    elif any(word in text for word in ["comedy", "funny", "laugh"]):
        return "You might like: Superbad, 21 Jump Street, or The Hangover."

    # Rule 3 – Horror Movies
    elif any(word in text for word in ["horror", "scary", "thriller"]):
        return "You might like: The Conjuring, Get Out, or A Quiet Place."

    # Rule 4 – Romance Movies
    elif any(word in text for word in ["romance", "love", "relationship"]):
        return "You might like: La La Land, The Notebook, or Crazy Rich Asians."

    # Fallback Rule – No Match
    else:
        return ("I’m not sure what genre that is. "
                "Try words like action, comedy, horror, or romance.")


def main():
    print("Welcome to the Movie Recommendation System!")
    print("What kind of movie are you in the mood for?")
    print("(For example: action, comedy, horror, romance, sci-fi)")

    # Get input from the user
    user_input = input("Your answer: ")

    # Get recommendation based on rules
    recommendation = recommend_movies(user_input)

    # Output result
    print(recommendation)


if __name__ == "__main__":
    main()
