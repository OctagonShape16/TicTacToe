import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.environ['OPENAI_API_KEY'])

def get_completion(messages):
    response = client.chat.completions.create(
    model="microsoft/phi-3-mini-4k-instruct",
    messages=messages,
    temperature=0,
    max_tokens=1024)
    return response.choices[0].message.content

delimiter = "####"
example = {"1":"2","2":"0","3":"1",
           "4":"0","5":"0","6":"2",
           "7":"0","8":"0","9":"1",
           "symbol":"1","moves":"[2, 4, 5, 7, 8]"}

system_message = f"""You are a TicTacToe bot. \
That means there will be a 3x3 grid as the playing board, \
so your and your opponents goal is to place 3 of your symbols \
in a row, column or diagonal. \
You will be provided with the playing board, all available moves \
and your own symbol (a blank tile is 0) in json format delimited by \
{delimiter} characters. \
i.e. {delimiter}{example}{delimiter}
Here is a list of instructions you must strictly follow \
and make sure to always finish all instructions before outputting something:
Step 1:
Look at all the available moves provided \
(do not play a move that is not in this list).
Step 2:
Calculate which of these moves is the best way for you to win \
and also stop your opponent from winning. \
To do that follow this checklist:
Is there a way to immediately win by placing 3 symbols in a row, column or diagonal? \
If so immediately do that.
Is there a way for your opponent to immediately win \
by placing 3 symbols in a row, column or diagonal? If so immediately block this tile.
Is there a way for you to create a fork now or in the future? \
If so try to follow that plan.
Is there a way for your opponent to fork you now or in the future? \
If so try to stop that plan.
If non of the named things are true just try to play logical moves, not loose and \
always be strategic by visualizing the board and thinking about the future.
Step 3:
Output the move you chose as just a singular digit with no other information \
(e.g your thought process or reasoning) not included."""

def create_message(user_message):
    messages =  [
      {'role':'system',
      'content': system_message},
      {'role':'user',
      'content': f"{delimiter}{example}{delimiter}"},
      {'role':'assistant',
      'content': "7"},
      {'role':'user',
      'content': f"{delimiter}{user_message}{delimiter}"}
    ]
    return messages
