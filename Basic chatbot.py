def chatbot():
    """A simple rule-based chatbot for the CodeAlpha internship task."""

    # A dictionary to store keyword-response pairs.
    # The keys are lowercase to handle case-insensitive user input.
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }

    print("Welcome! I'm a simple rule-based chatbot.")
    print("You can say 'hello', 'how are you', or 'bye' to me.")
    print("Type 'bye' to exit the chat.\n")

    # Start an infinite loop to keep the conversation going.
    while True:
        try:
            # Get user input and convert it to lowercase for easy matching.
            user_input = input("You: ").lower()

            # Check if the user wants to exit the chat.
            if user_input == "bye":
                print("Bot:", responses[user_input])
                break

            # Find a matching response in the dictionary.
            # Using get() with a default value prevents key errors.
            bot_response = responses.get(user_input, "Sorry, I don't understand that.")

            # Print the bot's response.
            print("Bot:", bot_response)

        except (IOError, EOFError) as e:
            print(f"An error occurred: {e}. Exiting the chatbot.")
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
