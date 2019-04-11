from tkinter import *
from PIL import Image, ImageTk
import glob

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.instruction = Label(self, text = "Path to image:")
		self.instruction.grid(row = 0, column = 0, sticky = W)

		self.path = Entry(self)
		self.path.grid(row = 0, column = 1, sticky = W)

		self.submit_button = Button(self, text = "Submit", command = self.submit_touched)
		self.submit_button.grid(row = 1, column = 0, sticky = W)


	def submit_touched(self):
		content = self.path.get()

		self.image = ImageTk.PhotoImage(Image.open(content))
		self.imageLabel = Label(self, image = self.image).grid(row = 2, column = 0, columnspan = 2, sticky = W)

		self.image_to_text_title = Label(self, text = "Image to text result:")
		self.image_to_text_title.grid(row = 3, column = 0, sticky = W)

		self.image_to_text = Text(self, width = 35, height = 5, wrap = WORD)
		self.image_to_text.grid(row = 4, column = 0, columnspan = 2, sticky = W)
		
		self.word_embedding_title = Label(self, text = "Word embedding result:")
		self.word_embedding_title.grid(row = 5, column = 0, sticky = W)

		self.word_embedding = Text(self, width = 35, height = 5, wrap = WORD)
		self.word_embedding.grid(row = 6, column = 0, columnspan = 2, sticky = W)

		
		self.image_to_text_run(self.image)
		self.word_embedding_run()


	def image_to_text_run(self, image):
		self.image_to_text.insert(0.0, "image_to_text")

	def word_embedding_run(self):
		self.word_embedding.insert(0.0, "word_embedding")



root = Tk()
root.title("Image to text to word embedding")
root.geometry("800x600")
app = Application(root)

root.mainloop()