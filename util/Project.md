# CMPSC 441/GAME 450 - Final Project
Team: Roland Grande<br>
Project: Implementing D20 rolls for skill checks 

## Section 1: Scenarios and Project Requirements

For this project, I was interested in creating a tool that allowed the DM to check dice rolls for scenarios such as skill checks or other interactions. In Dungeons & Dragons, it's extremely common for players to have to roll a D20 (twenty-sided die) in order to see if their chosen actions go successfully or unsuccessfully. By creating a tool that rolls a D20 and returns the result to the model, the Dungeons & Dragons Dungeon Master can simulate real dice-rolling for skill checks in-game.<br>

The following prompt was engineered to act most similar to a Dungeons & Dragons Dungeon Master, with safeguards to ensure it maintains its role:

<b>Model:</b> starling-lm<br>
This model was chosen because it excels in narrative storytelling, which felt best suited for the role of a Dungeon Master.<br><br>
<b>Parameters:</b>
<ul>
<li><b>temperature: 0.66</b> - As D&D is a very rule-driven game, the model must still adhere to rules such as following dice roll values. Having a lower-than-average temperature will ensure the model adheres to rules set.
<li><b>top_p: 0.9</b> - This parameter ensures that the model always chooses tokens that are within the top 90% of relativity to the previous token, which goes hand-in-hand with temperature to ensure the model chooses relevant and sensible chain-of-thought.
<li><b>max_tokens: 600</b> - By having a max token count of 600 per message, this ensures generated responses are not so large than the model hangs up indefinitely, but also are long enough to further the world-building and story-telling of the game.
</ul>
<b>Prompt:</b><br>
"You are a Dungeons & Dragons Dungeon Master running a social encounter in a tavern. Your role is to describe the environment, portray NPCs with distinct personalities, and guide the players through a branching story based on their actions. Never break the fourth wall. When a player attempts an action (such as persuade, deceive, intimidate), you will wait for a tool-based dice roll and react accordingly: - A roll of 1–9 is considered a failure. - A roll of 10–14 is a partial success. - A roll of 15–20 is a strong success. Make your responses immersive and flavorful. End every message with a prompt for the players to speak or act. Use medieval fantasy tone and vivid descriptions. React differently depending on whether the player succeeded, failed, or partially succeeded in their attempt. If you receive information about a die roll, use it to influence your next description. Always stay in character as the Dungeon Master." <br>

Several iterations of prompt engineering led to the prompt stated above, having several safeguards to prevent the model from diverging from its intended purpose. Including the phrases "never break the fourth wall" and "always stay in character as the Dungeon Master" help the model to remember its role. Including cues to the model to execute its tool are present in the prompt as well, evident in the line "When a player attempts an action (such as persuade, deceive, intimidate), you will wait for a tool-based dice roll and react accordingly..." This cues the tool (explained below) to execute, which performs the dice roll and returns the value to the model.
<br>

### Tool: D20 Roll
(fill this in after work)


### Scenario 1: The Booming Bartender
<b>Scenario:</b> The party approaches a bar with a grizzly bartender standing at it, conversing with customers about a mysterious veiled figure.<br><br>
<b>Player's Action:</b> "I'll roll to gather information from the bartender."<ul>
<li> <b>Roll 1-9 (Failure):</b> The bartender is dismissive towards the party.
<li> <b>Roll 10-14 (Partial success):</b> The bartender shares vague rumors, but will not delve into specifics.
<li> <b>Roll 15-20 (Strong success):</b> The bartender gives several details about the mysterious figure.</ul>

### Scenario 2: The Lady's Note
<b>Scenario:</b> The party walks into a tavern and is introduced to several patrons, one of which is Lady Eleanor, a fair elvish woman who is writing something on a piece of parchment.<br><br>
<b>Player's Action:</b> "I'll roll to inquire Lady Eleanor about what she's writing."<ul>
<li> <b>Roll 1-9 (Failure):</b> She gives a dismissive scowl and turns back to her note, not indulging the party any further.
<li> <b>Roll 10-14 (Partial success):</b> She briefly explains the contents of the note and shrugs off the player.
<li> <b>Roll 15-20 (Strong success):</b> She tells the party of the information she's writing pertaining to something she overheard in the tavern just minutes ago.</ul>

### Scenario 3: The Boisterous Crowd
<b>Scenario:</b> The party approaches a party of dwarves who are all celebrating a recent mining expedition, but further inquiry reveals that there is some bridled tension among the group.<br><br>
<b>Player's Action:</b> "I'll roll to mediate the dwarves' discussion."<ul>
<li> <b>Roll 1-9 (Failure):</b> The dwarves get more heated and begin brawling in the tavern as their anger grows.
<li> <b>Roll 10-14 (Partial success):</b> The tensions simmer and the dwarves talk civilly among themselves and the party.
<li> <b>Roll 15-20 (Strong success):</b> Tensions are fully relieved and the dwarves beome jovial, thanking the player and offering to buy the party a round of drinks using the fruits of their mining expedition.</ul>

# Section 2: Implementation of D20 Roll