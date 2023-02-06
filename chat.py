from tkinter import *
import customtkinter
import openai
import os
import pickle

root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x600")
# root.iconbitmap("ai_lt.ico")

# Set colors scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Submit to ChatGPT
def speak():
	if chat_entry.get():
		
		# Define the filename
		filename  = "api_key"

		try:
			if os.path.isfile(filename):

				# Open the file
				input_file = open(filename, "rb")

				# Load the data from the file into a variable
				var = pickle.load(input_file)

				# Query ChatGPT
				# Define API to ChatGPT
				openai.api_key = var

				# Create an instance
				openai.Model.list()

				#Define the query / response
				response = openai.Completion.create(
					model = "text-davinci-003", 
					prompt = chat_entry.get(), 
					temperature = 0,
					max_tokens = 60,
					top_p = 1.0, 
					frequency_penalty = 0.0,
					presence_penalty = 0.0)

				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")
				

			else:
				# Create the file
				input_file = open(filename, "wb")
				# Close the file
				input_file.close()
				# Display Error Message
				my_text.insert(END, "\n\n You need an API Key to converse with ChatGPT!!! Get one here:\n https://beta.openai.com/account/api-keys")


		except Exception as e:
			my_text.insert(END, "\n\n An error encountered!!\n\n{e}")
	else:
		my_text.insert(END, "\n\nHey! You forgot to type!!!")

# Clear the screen
def clear():
	
	# Clear the main textbox 
	my_text.delete(1.0, END)

	# Clear the query entry box
	chat_entry.delete(0, END)

# API Connection
def key():

	# Define the filename
	filename  = "api_key"

	try:
		if os.path.isfile(filename):

			# Open the file
			input_file = open(filename, "rb")

			# Load the data from the file into a variable
			var = pickle.load(input_file)

			# Output to entry box
			api_entry.insert(END, var)

		else:
			# Create the file
			input_file = open(filename, "wb")
			# Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, "\n\n An error encountered!!\n\n{e}")

	# Resize App Larger
	root.geometry("600x750")
	# Reshow API
	api_frame.pack(pady = 30)

    	
# Save API Key
def save_key():
	 # Define our filename
	 filename = "api_key"

	 try:
	 	# Open file
		 output_file = open(filename, 'wb')

		 # Add data to the file 
		 pickle.dump(api_entry.get(), output_file)

		 # Delete Entry Box
		 api_entry.delete(0, END)

		 # Hide the API Frame
		 api_frame.pack_forget()
		 # Resize App Smaller
		 root.geometry("600x600")
		 
	 except Exception as e:
	 	my_text.insert(END, "\n\n An error encountered!!\n\n{e}")
		
		

# Create text frame
text_frame  = customtkinter.CTkFrame(root)
text_frame.pack(pady = 20)

# Add text widget to get ChatGPT responses
my_text = Text(text_frame, bg = "#343638", width = 65, bd = 1, fg = "#d6d6d6", relief = "flat", wrap = WORD, selectbackground = "#1f538d")
my_text.grid(row = 0, column = 0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame, command = my_text.yview)
text_scroll.grid(row = 0, column = 1, sticky = "ns")

# Adding the scrollbar to textbox
my_text.configure(yscrollcommand = text_scroll.set)

# Entry Widget 
chat_entry = customtkinter.CTkEntry(root, placeholder_text = "Type something to ChatGPT...", width = 535, height = 50, border_width = 2)
chat_entry.pack(pady = 10)

# Creat button frame
button_frame = customtkinter.CTkFrame(root, fg_color = "#242424")
button_frame.pack(pady = 10)

# Creating Buttons
# Submit Button
submit_button  = customtkinter.CTkButton(button_frame, text = "Speak to ChatGPT", command = speak)
submit_button.grid(row = 0, column = 0, padx = 25)

# Clear Button
clear_button  = customtkinter.CTkButton(button_frame, text = "Clear Response", command = clear)
clear_button.grid(row = 0, column = 1, padx = 35)

# API Button
api_button  = customtkinter.CTkButton(button_frame, text = "Update API Key", command = key)
api_button.grid(row = 0, column = 2, padx = 25)

# API key Frame
api_frame = customtkinter.CTkFrame(root, border_width = 1)
api_frame.pack(pady = 30)

# API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame, placeholder_text = "Enter your API Key", width = 350, height = 50, border_width = 1)
api_entry.grid(row = 0, column = 0, padx = 20, pady = 20)

# Add API Button
api_save_button = customtkinter.CTkButton(api_frame, text = "Save Key", command = save_key)
api_save_button.grid(row = 0, column = 1, padx = 10)

root.mainloop()