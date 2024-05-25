import random
    
def cut_up_machine():
    stories = []
    num_stories = 3
    
    # Input stories
    for i in range(num_stories):
        print(f"Enter story {i+1}: ")
        story = input()
        stories.append(story)
    
    # Combine sentences from all stories
    sentences = []
    for story in stories:
        sentences += story.split('. ')
    
    # Randomize the sentences
    random.shuffle(sentences)
    
    # Output the combined randomized story
    randomized_story = '. '.join(sentences)
    print("\nRandomized Story:")
    print(randomized_story)

# Run the function
cut_up_machine()

