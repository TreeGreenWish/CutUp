import random


#First Commit on Github

def cut_up_machine(*stories):
    sentences = []
    for story in stories:
        sentences += story.split('. ')
    random.shuffle(sentences)
    return '. '.join(sentences)

# Test the function
story1 = "Once upon a time, in a land far far away, there lived a beautiful princess."
story2 = "The prince was on a journey to find a potion that would make him immortal."
story3 = "They met and fell in love, but the wicked witch was determined to keep them apart."

print(cut_up_machine(story1, story2, story3))
