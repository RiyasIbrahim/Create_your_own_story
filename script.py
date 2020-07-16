######
# TREENODE CLASS
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choice = []

######

######
# VARIABLES FOR TREE
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...
""")
######

######
# TESTING AREA
print("\nOnce upon a time")
print(story_root.story_piece)

######
