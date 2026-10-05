# Python Tutor - Initial Design
#
# 1. Topics the tutor will explain:
#    Variables
#    List 
#    dictionary
#    function
#    class
#    git
#
# 2. What the tutor should remember:
#    The tutor should remember the whole conversation self.history
#    Also the result of the questions that the student already tried. self.mastered_topics
#   
#
# 3. What the tutor should respond when a topic is not available:
#    It should explain that the requested topic is not available
#    and show the topics it can currently explain.
#
# 4. How the tutor will determine whether an answer is correct:
#    Text answers will be normalized by removing extra spaces
#    and ignoring capitalization before comparing them with the
#    expected answer.
#    Numeric answers will be converted to numbers and compared
#    with the expected numeric value.
#

class PythonTutor:
	def __init__(self):
		self.history = []
		self.mastered_topics = {}
		self.topics = {
			"variable": {
				"explanation": "A variable stores a value.",
				"question": "What symbol is used to assign a value to a variable?",
				"answer": "=",
				"answer_type": "text",
			},
			"list": {
				"explanation": "A list stores an ordered collection of values.",
				"question": "What is the index of the first item in a Python list?",
				"answer": "0",
				"answer_type": "number",
			},
			"dictionary": {
				"explanation": "A dictionary stores values using keys.",
				"question": "What do dictionaries use to look up values?",
				"answer": "keys",
				"answer_type": "text",
			},
			"function": {
				"explanation": "A function is reusable code that performs a task.",
				"question": "What is a reusable block of code called?",
				"answer": "function",
				"answer_type": "text",
			},
			"class": {
				"explanation": "A class is a blueprint for creating objects.",
				"question": "What is a class a blueprint for creating?",
				"answer": "objects",
				"answer_type": "text",
			},
			"git": {
				"explanation": "Git tracks changes to files over time.",
				"question": "What does Git track over time?",
				"answer": "changes to files",
				"answer_type": "text",
			},
		}

	def explain_concept(self, normalized_message):
		for topic, info in self.topics.items():
			if topic in normalized_message:
				return info["explanation"]

		available_topics = ", ".join(self.topics)
		return f"That topic is not available yet. I can explain: {available_topics}."

	def ask_question(self, normalized_message):
		for topic, info in self.topics.items():
			if topic in normalized_message:
				student_answer = input(info["question"] + " ")

				if info["answer_type"] == "text":
					student_answer = " ".join(student_answer.lower().split())
					correct_answer = " ".join(info["answer"].lower().split())
				else:
					try:
						student_answer = int(student_answer)
					except ValueError:
						return "Please enter a number."
					correct_answer = int(info["answer"])

				is_correct = student_answer == correct_answer
				self.mastered_topics[topic] = is_correct
				return "Correct!" if is_correct else f"Incorrect. The correct answer was: {info['answer']}."

		available_topics = ", ".join(self.topics)
		return f"That topic is not available yet. I can quiz you on: {available_topics}."

	def show_progress(self):
		if not self.mastered_topics:
			return "You haven't attempted any topics yet."

		correct_topics = sum(self.mastered_topics.values())
		attempted_topics = len(self.mastered_topics)
		return f"You answered {correct_topics} out of {attempted_topics} attempted topics correctly."

	def show_history(self):
		for speaker, text in self.history:
			print(f"{speaker}: {text}")

	
	def respond(self, message):
		self.history.append(("student", message))
		normalized_message = message.strip().lower()
		message_words = normalized_message.split()

		if any(greeting in message_words for greeting in ("hello", "hi")):
			response = "Hello! What would you like to learn about Python?"
		elif any(command in message_words for command in ("bye", "exit")):
			response = "Goodbye! Happy learning."
		elif "explain" in normalized_message:
			response = self.explain_concept(normalized_message)
		elif "question" in message_words or "quiz" in message_words:
			response = self.ask_question(normalized_message)
		elif "progress" in message_words:
			response = self.show_progress()
		else:
			response = "I don't know how to answer that yet."

		self.history.append(("tutor", response))
		return response


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


def main():
    tutor = PythonTutor()
    start_conversation(tutor)


if __name__ == "__main__":
    main()