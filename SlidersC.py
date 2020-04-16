# import usefull GUI tool
import tkinter as tk

# class contains lower and upper HSV sliders and few buttons that set colors for the mask

class Sliders():

	# constuctor
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Mask range setting")

		self.lowerHslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="lower H")
		self.lowerSslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="lower S")
		self.lowerVslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="lower V")
		self.upperHslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="upper H")
		self.upperSslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="upper S")
		self.upperVslide = tk.Scale(self.root, from_ = 0, to=255, resolution=1, orient=tk.HORIZONTAL, label="upper V")
		self.lowerHslide.pack()
		self.lowerSslide.pack()
		self.lowerVslide.pack()
		self.upperHslide.pack()
		self.upperSslide.pack()
		self.upperVslide.pack()

		self.RedButton = tk.Button(text="RED", command=self.set_red)
		self.GreenButton = tk.Button(text="GREEN", command=self.set_green)
		self.BlueButton = tk.Button(text="BLUE", command=self.set_blue)
		self.ArtLightSkinButton = tk.Button(text="ART LIGHT SKIN COLOR", command=self.set_skin_color_artlight)
		self.DayLightSkinButton = tk.Button(text="DAY LIGHT SKIN COLOR", command=self.set_skin_color_daylight)
		self.RedButton.pack()
		self.GreenButton.pack()
		self.BlueButton.pack()
		self.ArtLightSkinButton.pack()
		self.DayLightSkinButton.pack()

	def update_slider(self):
		self.root.update()
		return

	def get_lower_values(self):
		return self.lowerHslide.get(), self.lowerSslide.get(), self.lowerVslide.get()

	def get_upper_values(self):
		return self.upperHslide.get(), self.upperSslide.get(), self.upperVslide.get()

	def set_red(self):
		self.lowerHslide.set(170)
		self.lowerSslide.set(100)
		self.lowerVslide.set(0)
		self.upperHslide.set(180)
		self.upperSslide.set(255)
		self.upperVslide.set(255)
		return

	def set_green(self):
		self.lowerHslide.set(25)
		self.lowerSslide.set(52)
		self.lowerVslide.set(72)
		self.upperHslide.set(102)
		self.upperSslide.set(255)
		self.upperVslide.set(255)
		return

	def set_blue(self):
		self.lowerHslide.set(94)
		self.lowerSslide.set(80)
		self.lowerVslide.set(2)
		self.upperHslide.set(126)
		self.upperSslide.set(255)
		self.upperVslide.set(255)
		return

	#set skin color HSV parameters good for artificial light

	def set_skin_color_artlight(self):
		self.lowerHslide.set(0)
		self.lowerSslide.set(69)
		self.lowerVslide.set(38)
		self.upperHslide.set(191)
		self.upperSslide.set(180)
		self.upperVslide.set(90)
		return

	#set skin color HSV parameters good for day light

	def set_skin_color_daylight(self):
		self.lowerHslide.set(124)
		self.lowerSslide.set(34)
		self.lowerVslide.set(154)
		self.upperHslide.set(255)
		self.upperSslide.set(101)
		self.upperVslide.set(255)
		return
