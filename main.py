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
#    Also the result of the questions that the student already tried. self.dominated_topics
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
