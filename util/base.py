from dndnetwork import DungeonMasterServer, PlayerClient
from llm_utils import TemplateChat
from llm_utils import roll_d20
import re


class DungeonMaster:
    def __init__(self):
        self.game_log = ['START']
        self.server = DungeonMasterServer(self.game_log, self.dm_turn_hook)
        self.chat = TemplateChat.from_file(
            'templates\dm_chat.json', 
            sign='d20_tool_use',
            function_call_processor=self.process_tool_calls
        )
        self.start = True

    def start_server(self):
        self.server.start_server()

    def dm_turn_hook(self):
        dm_message = ''
        # Do DM things here. You can use self.game_log to access the game log
        if self.start:
            dm_message = self.chat.start_chat()
            self.start = False
        else: 
            dm_message = self.chat.send('\n'.join(self.game_log))

        # Return a message to send to the players for this turn
        return dm_message 
    
    def process_tool_calls(self, response):                                             # can handle any tool call
        content = response['message']['content']
        match = re.search(r"\[ROLL:D20:(.*?)\]", content)                               # handle specifically d20 rolls
        if match:
            reason = match.group(1).strip()
            result = roll_d20(reason)                                                   # roll a d20 using the roll_d20 function in llm_utils
            roll_message = f"(A d20 was rolled for {reason}: **{result['roll']}**)"     # send a message back to the model indicating what the d20 was rolled ffor
            self.chat.messages.append({"role": "system", "content": roll_message})
        return response


class Player:
    def __init__(self, name):
        self.name = name
        self.client = PlayerClient(self.name)

    def connect(self):
        self.client.connect()

    def unjoin(self):
        self.client.unjoin()

    def take_turn(self, message):
        self.client.send_message(message)
