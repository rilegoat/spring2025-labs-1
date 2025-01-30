# Prompt Engineering Process

### Step 1
#### Intention
>What is the improvement that you intend to make?
Today, my intention was to initialize my LLM's code so that it would begin acting like a Dungeon Master. To do this, I set up a simple call-and-response between the user and the system. The system is initially instructed to act as a Dungeon Master, specializing in single-player oriented games. Initially I chose llama3.2 as my model because I wanted to test the capabilities of it before finding a less RAM-intensive model.

#### Action/Change
>Why do you think this action/change will improve the agent?
My initial settings feel like they will add enough constraints to shape the model into giving the responses I'm looking for while still allowing room for creativity. My temperature is initially set to 0.7, but I will experiment with making this value larger if I desire more creativity from the model. By having the model produce responses before the user, I'm able to get a user's input to gracefully exit the game, which also allows me to track my progress towards improving my model.

#### Result
>What was the result?
The result was promising, and the model did a good job at replicating the style of a Dungeon Master. It succinctly explained the premise and rules of Dungeons & Dragons, and it also fit itself into a personable and emotive expression which makes the user feel as if they're interacting with a real person.
On the other hand, responses take a very long time to generate---typically waiting close to a minute for responses, which would not be practical in a D&D setting. To attempt to solve this, I'm going to look into models that use less RAM and I'll be testing those models to see which of them seem to be better with narrative storytelling.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
I think this worked because of the constraints I added in the initial message---by telling the model to "emulate the prose and format of a Dungeons & Dragons Dungeon Master," it strongly filters and shapes the word choice and text formatting of my responses. This results in a much more authentic experience than if responses were formatted as simple paragraphs with less rigid structure.