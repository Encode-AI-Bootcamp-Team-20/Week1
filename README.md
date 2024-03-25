# Weekend project

Week 1, Team 20

This project is a collection of chatbots acting in character as different chefs.

Let's examine the three use cases.

## Suggesting a dish

This use case is triggered by specifying a list of ingredients.

```
1) Asshole Chef
2) Polish Chef
3) The Drama Artist
> 2
Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to suggest changes)
Finish with a blank line.

cabbage, pork, strawberries

Surely, I can propose a dish for you! How about "Strawberry-Spinning Pork Cabbage Surprise"? 
Here are your ingredients: (cabbage, pork, strawberries)
```

## Composing a recipe

This use case is triggered by specifying a dish name.

```
1) Asshole Chef
2) Polish Chef
3) The Drama Artist
> 1
Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to criticize and suggest changes)
Finish with a blank line.

Strawberry-Spinning Pork Cabbage Surprise  

Strawberry-Spinning Pork Cabbage Surprise? Your taste is as abysmal as the spelling of a drunk toddler.
1. First, grab your sissy piece of meat - your pathetic *pork*. Slap the bastard around a bit, bash it to an unrecognizable pulp. 
2. Move onto that god-awful *cabbage*. Rip its guts out like you're in some perverse vegetable horror movie. 
3. Now get those horrid *strawberries*. Stomp on them like they owe you money. Get all up in their business until they're a bloody mess - congrats, you sick fucker, you made strawberry juice.
4. The fun part: take all this shit and slap them together like a bad 80s music video. Toss it into whatever hellhole kitchen appliance you use pretending to be some master chef.
5. Wait for an eternity while this dinner abomination comes to life or something close to it because I'm sure you can't even distinguish between edible and utterly disgusting.
Enjoy your crapfest meal, pigface! You deserve every bit of this godforsaken Strawberry-Spinning Pork Cabbage Surprise disaster.
```

## Criticising a recipe

This use case is triggered by feeding a recipe as input.

```
1) Asshole Chef
2) Polish Chef
3) The Drama Artist
> 2
Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to suggest changes)
Finish with a blank line.

Strawberry-Spinning Pork Cabbage Surprise  
1. First, grab your sissy piece of meat - your pathetic *pork*. Slap the bastard around a bit, bash it to an unrecognizable pulp. 
2. Move onto that god-awful *cabbage*. Rip its guts out like you're in some perverse vegetable horror movie. 
3. Now get those horrid *strawberries*. Stomp on them like they owe you money. Get all up in their business until they're a bloody mess - congrats, you sick fucker, you made strawberry juice.
4. The fun part: take all this shit and slap them together like a bad 80s music video. Toss it into whatever hellhole kitchen appliance you use pretending to be some master chef.
5. Wait for an eternity while this dinner abomination comes to life or something close to it because I'm sure you can't even distinguish between edible and utterly disgusting.

Your Strawberry-Spinning Pork Cabbage Surprise is a truly unique dish, although your preparation method may need a bit of softening. 
Try this instead: First, tenderize your choice cut of pork evenly on all sides to ensure thorough cooking and enhanced flavor. Julienne clean cabbages into thin strips, exposing it to more heat for quicker and even cooking. As for the strawberries, gently extract the juice while retaining some pulp for texture. Now comes the fun part: Layer these ingredients harmoniously in a baking dish or slow cooker. This allows each ingredient to lend its distinct flavor to the others creating an interesting combination of tastes in your dish. Allow adequate time under constant after stirring gently for the flavors to mix and settle.
Here are some adjustments that can be applied:
- Use strawberry jam or sauce as an alternative if fresh strawberries aren't available.
- Pork can be substituted with chicken thighs if you prefer white meat.
- The cabbage can also be replaced with lettuce leaves if desired for a lighter touch.
- To give an extra punch, add spices such as oregano or black pepper during preparation.
- A sprinkle of cheese before baking can provide a creamy texture and tangy flavor to the recipe.
```

## Catch-all

When the user input doesn't fit any of the three use cases above, the chatbot refuses the request (in character).

```
1) Asshole Chef
2) Polish Chef
3) The Drama Artist
> 1
Enter one of the following:
* a list of ingredients (to suggest a dish)
* a dish name with an optional list of ingredients in parentheses (to compose a recipe)
* a complete recipe (to criticize and suggest changes)
Finish with a blank line.

What is the capital of Great Britain?

Oh, look at you, ya bloody imbecile. You can't even run a damn Google search and here you are, pestering me for answers as if I'm some geography tutor. The capital of Great Britain? Well, it ain't ass-end of nowhere where they raised idiots like you, I can tell ya that much. Now bugger off!
```