# static response 
# from ollama import chat
# prompt= input("Enter your prompt:")
# response = chat(
#     model='gemma4:31b-cloud',
#     messages=[{'role': 'user', 'content': prompt}],
# )
# print(response.message.content)
# python concepts
# wan to run logic 
# ollama server installed
# ollama model should be installed


# method to streaming response

from ollama import chat
prompt= input("Enter your prompt:")
response= chat(
    model='qwen-small:latest',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)
for chunk in response:
    print(chunk.message.content,end="",flush=True)