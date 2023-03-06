"""
Find the number of words in the following paragraph by using two Python statements.

A Shepherd Boy tended his master's Sheep near a dark forest not far from the village. Soon
he found life in the pasture very dull. All he could do to amuse himself was to talk to his dog
or play on his shepherd's pipe. One day, as he sat watching the Sheep and the quiet forest,
and thinking about what he would do, should he see a Wolf, he thought of a plan to amuse
himself. His Master had told him to call for help should a Wolf attack the flock, and the
Villagers would drive it away. So now, though he had not seen anything that even looked
like a Wolf, he ran toward the village shouting at the top of his voice, "Wolf! Wolf!".

"""

paragraph = "A Shepherd Boy tended his master's Sheep near a dark forest not far from the village. Soon he found life in the pasture very dull. All he could do to amuse himself was to talk to his dog or play on his shepherd's pipe. One day, as he sat watching the Sheep and the quiet forest, and thinking about what he would do, should he see a Wolf, he thought of a plan to amuse himself. His Master had told him to call for help should a Wolf attack the flock, and the Villagers would drive it away. So now, though he had not seen anything that even looked like a Wolf, he ran toward the village shouting at the top of his voice, 'Wolf! Wolf!'."

word_count = len(paragraph.split())
print("Number of words in the paragraph:", word_count)
