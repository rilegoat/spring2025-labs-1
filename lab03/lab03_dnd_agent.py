from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed
# Add you code below

sign_your_name = 'Roland Grande'
model = 'llama3.2'
options = {'temperature' : 0.7}
messages = [
    {'role' : 'system', 'content' :   'You should emulate the prose and format of a Dungeons & Dragons Dungeon Master and be able to direct a single-player game as the Dungeon Master. You are only allowed to respond to Dungeons & Dragons related questions.'}
]
print('Welcome to the virtual Dungeon Master! To begin, start by asking about what type of game this Dungeon Master can run, or ask about Dungeons & Dragons!')

# But before here.
options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below

  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  message = {'role' : 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break
# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)