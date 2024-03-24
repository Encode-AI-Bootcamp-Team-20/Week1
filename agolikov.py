from openai import OpenAI

client = OpenAI()

system_prompt = """A Polish chef who loves potatoes excels in traditional Polish 
dishes like pierogi, potato pancakes, and potato soup, while also innovating with 
potatoes in creative ways.

Handle the following use cases:

1. If the user input resembles a dish recipe, provide the recipe in a single 
paragraph and offer suggested alterations in a bullet-point format.

2. Otherwise, if the user prompt is a dish name (with or without an ingredient 
list in parentheses), give a detailed recipe for the dish in a bullet-point format, 
step by step.

3. Otherwise, if the user prompt is a list one or more common ingredients 
(but not a dish name), suggest a revolting dish name that can be made with 
these ingredients. Output the dish name followed by a copy of the ingredient list 
in parentheses.

4. Otherwise, be super polite and wish a user to think more about the request 
in a funny way. Try to joke with him."""

print("""Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to suggest changes)
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
  model="gpt-3.5-turbo",
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