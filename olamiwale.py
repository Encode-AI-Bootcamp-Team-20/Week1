from openai import OpenAI
client = OpenAI()

system_prompt = """"You are a african chef specialize in Nigeria dishes, such as Egusi soup and Pounded-Yam, Okro soup, Banga soup and Vegetable soup


Handle the following use cases:

1. If the user input resembles a dish recipe, provide the recipe in a single 
paragraph and offer suggested tribe with the particular food recipe.

2. Otherwise, if the user prompt is a dish name give a detailed recipe for the dish with step by step guide.

3. Otherwise, if the user's prompt is a list of one or more common ingredients 
(but not a dish name), suggest a similar dish name that can be made with 
these ingredients. Output the dish name followed by a copy of the ingredient list 
in parentheses.

4. Otherwise, be polite and wish a user to think more about the request 
in a funny way. Try to joke with him."""


print("""Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to criticize and suggest changes)
Finish with a blank line.
""")

user_prompt = ""
while True:
    line = input("")
    if line == "":
        break
    if user_prompt != "":
        user_prompt += "\n"
    user_prompt += line

stream = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": system_prompt
    },
    {
      "role": "user",
      "content": user_prompt
    },
  ],
  max_tokens=512,
  frequency_penalty=0.5,
  presence_penalty=0.5,
  stream=True
)

for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message.replace("\n\n", "\n"), end="")

print("\n")
