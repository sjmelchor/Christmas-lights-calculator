import math
pi = math.pi
num_wraps = 2

#this is the user's input part
max_height_feet = float(input("How tall is your tree (in feet?)\n"))
max_height_inches = max_height_feet*12
base_radius = float(input("What is the diameter of the base (in inches)\n"))/2
strand_spacing = float(input("How much vertical space between strands would you like (in inches)?\n"))

#make the list assuming wrapping around the largest and smallest parts of the tree
wrap_points = [1, max_height_inches]

#to calculate number of wraps based on desired strand spacing
num_wraps += (int((max_height_inches-1)/strand_spacing))
#print(f"num wraps = {num_wraps}")

#I can't figure out how to get this part to work in my for loop yet, so this just adds the first spacing to the min height to get the first middle wrap.
points = wrap_points[0] + strand_spacing
wrap_points.append(points)

#this will only kick in if there are more than 3 wraps, because the first two wraps are already accounted for in the list, and the third one is added right up there^
for n in range(num_wraps-3):
    points += strand_spacing
    wrap_points.append(points)

wrap_points = sorted(wrap_points)
print((wrap_points))

wrap_proportions = [round(item/max_height_inches, 2) for item in wrap_points]
#print(wrap_proportions)

furstrum_radii = [round(item*base_radius, 2) for item in wrap_proportions]
#print(furstrum_radii)

circumferences = [round(2*pi*item,2) for item in furstrum_radii]

#print(circumferences)

total_length_in_feet = round(((sum(circumferences)/12) + (strand_spacing*(num_wraps-1))/12), 2)

#print(total_length_in_feet)

print(f"For {num_wraps} wraps around a {max_height_feet} foot tall tree with {strand_spacing} inches of spacing, you will need at least {total_length_in_feet} feet of Christmas lights.")
