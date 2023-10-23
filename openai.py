import openai
import os 
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

# creating chatgpt_response function, which calls the "text-davinci-003" API from ChatGPT #
def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        # temperature controls randomness of response, and max_tokens limits the response so it is not so long #
        prompt=prompt,
        temperature=1,
        max_tokens=100
    )
    response_dict = response.get("choices")
    # uses OpenAI API's response dictionary, and uses one choice, which is a response. Then, return prompt_response #
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
