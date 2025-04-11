import tkinter as tk

current_scene = 'forest'
image_files = {'forest': 'images/forest.png', 'castle': 'images/castle.png'}

def help_command():
    display_scene("You can type 'look' to look around, 'go east' to go to the castle, and 'go west' to go back to the forest.")

def help_game():
    display_scene("Game help: Usually, I can understand one or two words. A verb and an object perahps.")

def display_scene(description):
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, description)
    update_image()

def update_image():
    global current_scene
    image_file = image_files.get(current_scene)
    if image_file:
        image = tk.PhotoImage(file=image_file)
        canvas.create_image(150, 150, anchor=tk.CENTER, image=image) # Center the image at 150, 150
        canvas.image = image  # Keep a reference to the image to prevent garbage collection

def process_input(event):
    global current_scene
    command = input_entry.get().strip().lower()
    input_entry.delete(0, tk.END)
    
    if current_scene == 'forest':
        if command == 'look':
            display_scene("You see tall trees and hear the chirping of birds.")
        elif command == 'repeat':
            command = 'look'
            display_scene('The birds are chirping. I just told you that. The trees are still trees')

        elif command == 'help':
            help_game()
        elif command == 'go east':
            current_scene = 'castle'
            display_scene("You walk towards the castle.")
        else:
            display_scene("I don't understand that command.")

    elif current_scene == 'castle':
        if command == 'look':
            display_scene("You stand before the grand castle gates.")
        elif command == 'go west':
            current_scene = 'forest'
            display_scene("You return to the forest.")
        else:
            display_scene("I don't understand that command.")
    else:
        display_scene("Oops! Something went wrong.")

root = tk.Tk()
root.title("King's Quest")

output_text = tk.Text(root, wrap=tk.WORD, height=5, width=50)
output_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

canvas = tk.Canvas(root, height=200, width=400)
canvas.grid(row=1, column=0, padx=10, pady=10)

input_label = tk.Label(root, text="> ")
input_label.grid(row=2, column=0, padx=10, sticky="w")

input_entry = tk.Entry(root)
input_entry.grid(row=2, column=0, padx=25, pady=10, sticky="ew")
input_entry.bind("<Return>", process_input)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

display_scene("Welcome to King's Quest! You are in the forest.")

root.mainloop()