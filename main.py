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
		self.topics = {
			"variable": {"explanation": "A variable stores a value."},
			"list": {"explanation": "A list stores an ordered collection of values."},
			"dictionary": {"explanation": "A dictionary stores values using keys."},
			"function": {"explanation": "A function is reusable code that performs a task."},
			"class": {"explanation": "A class is a blueprint for creating objects."},
			"git": {"explanation": "Git tracks changes to files over time."},
		}

	def explain_concept(self, normalized_message):
		for topic, info in self.topics.items():
			if topic in normalized_message:
				return info["explanation"]

		available_topics = ", ".join(self.topics)
		return f"That topic is not available yet. I can explain: {available_topics}."

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
		else:
			response = "I don't know how to answer that yet."

		self.history.append(("tutor", response))
		return response
