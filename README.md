# Christmas-lights-calculator
quick calculator based on user inputs to estimate length of lights (in feet)


I was trying to settle an argument with my spouse about how many feet of lights we needed for our new tree, and couldn't find a good calculator in the first 3 Google results I found, so I tried to figure out a way to make my own. This is the first project I'm posting here that's completely my own and not an exercise from the coding bootcamp I'm doing. 

My results track pretty well with [this calculator](https://www.omnicalculator.com/other/christmas-tree), considering how mine only uses really basic algebra and theirs uses some really lovely calculus. Mine seems to overestimate by about +1 rotations and about 10% the length of lights needed. For my fellow decorating afficionados out there, we know that adding the lights is the rate-limiting step, so I think it's always safer to overestimate! 

This is the most basic version of the calculator, that uses 3 user-given inputs to estimate the length: height of the tree, diameter at the base of the tree, and the desired vertical spacing between each strand of lights (which seems to be an industry-standard estimate of light density)?

The math is _really simple_, and assumes a few things so that I don't have to try to calculate the parameters of a conical helix, which is the right way to do it...
1. That each rotation exists in a single plane (and thus a constant circumference).
2. That the circumference of the tree is proportional to the height at a certain point along the tree.
3. That the "transitional length" as you move from one rotation to the next is equal to the number of inches of vertical spacing between each strand.

I'm trying to get more practice using git, so I'm posting the most basic iteration right now! Future versions will hopefully have a web-based user interface, and maybe even some kind of simulator (like the Omni Calculator version) to show what it will look like. 

Adding more sophisticated math is unlikely, but I do want to run some tests to get a more solid sense of what my margins of error are. 

Please enjoy!
