import tkinter as tk


class MainWindow:
	def __init__(self, root):
		self.root = root
		self.root.title("CBSE Database Manager")
		self.root.geometry("700x400")
	
	def __str__(self) -> str:
		return "Window of geometry 700x400"
	
	def __repr__(self) -> str:
		return ""

def main() -> None:
	root= tk.Tk()
	app = MainWindow(root)
	root.mainloop()



if __name__ == "__main__":
	print( f"Currently running {__file__.split( '\\' )[-1]} script." )
	main()
	

	
	"""super().__init__()
	window = tk.Tk()
	window.mainloop()"""

"""def main(self) -> None:
	..."""
"""def main() -> None:
	window = tk.Tk()

	# Settings
	window.title("CBSE Database Manager")
	window.geometry("700x400")

	# Icon
	# icon: tk.PhotoImage = tk.PhotoImage("icon.png")
	# window.wm_iconphoto(icon)

	# Starting the window
	window.mainloop()"""
