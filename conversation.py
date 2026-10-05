def start_conversation(tutor):
    print("Welcome to the Python Tutor! Type 'exit' to end the conversation.\n")

    while True:
        message = input("You: ")
        response = tutor.respond(message)
        print(f"Python Tutor: {response}\n")

        if "exit" in message.lower() or "bye" in message.lower():
            break

    print("--- Conversation History ---")
    tutor.show_history()
