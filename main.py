import math
pi = math.pi
num_wraps = 2

from tkinter import *
CREAM = "#Fbf9f3"

#window config
window=Tk()
window.title("Christmas Lights Calculator")
window.config(bg=CREAM, padx=20, pady=20)

#canvas config

canvas=Canvas(width=500, height=500, bg=CREAM, highlightthickness=0)
canvas.grid(column=1, row=1)


#------Define the function buttons to put user inputs into equations---#

def desired_spacing_input():
    strand_spacing = float(desired_spacing_entry.get())
    return strand_spacing


def tree_height_input():
    max_height_feet = float(tree_height_entry.get())
    return max_height_feet

    
def tree_radius_input():
    base_radius = float(tree_diameter_entry.get())/2
    return base_radius



#-------each entry box needs a Label() widget & an Entry() widget

#------Widgets for Vertical Spacing------#

desired_spacing_label = Label(text="Desired Vertical Spacing")
desired_spacing_label.grid(column = 0, row=0)

desired_spacing_entry = Entry()
desired_spacing_entry.grid(column = 1, row=0)


#--------Widgets for Tree Height Info------#

tree_height_label = Label(text = "Tree Height (ft)")
tree_height_label.grid(column = 0, row=1)

tree_height_entry = Entry()
tree_height_entry.grid(column = 1, row=1)


#-------Widgets for Tree Diameter Entry--------#

tree_diameter_label = Label(text="Tree Diameter at Base (in)")
tree_diameter_label.grid(column = 0, row=2)

tree_diameter_entry = Entry()
tree_diameter_entry.grid(column = 1, row=2)
                          

def calculate_lights():
    global num_wraps
    #make the list assuming wrapping around the largest and smallest parts of the tree
  
    max_height_feet = tree_height_input()
    max_height_inches = max_height_feet*12
    base_radius = tree_radius_input()
    
    wrap_points = [1, max_height_inches]
    
    strand_spacing = desired_spacing_input()
    #to calculate number of wraps based on desired strand spacing
    num_wraps += (int((max_height_inches-1)/strand_spacing))

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

#----Button to Run calculation------#

calculate_button = Button(text="Calculate", command=calculate_lights)
                          
calculate_button.grid(column=0, row=3)



window.mainloop()
