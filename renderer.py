import sys

from data import GetResume


class RenderContext:
	def __init__(self, lang):
		self.Lang = lang
		self.Text = ""
		self.HeadLevel = 1

	def Add(self, text):
		self.Text += text

	def IncHeadLevel(self):
		self.HeadLevel += 1
	def DecHeadLevel(self):
		if self.HeadLevel > 1:
			self.HeadLevel -= 1

	def StartHeader(self):
		tmp = "#" * self.HeadLevel + " "
		self.Text += F"\n\n{tmp}"
	def EndHeader(self):
		self.Text += "\n"
	def AddHeader(self, text):
		tmp = "#" * self.HeadLevel + " " + text
		self.Text += F"\n{tmp}\n"

	def StartItalic(self):
		self.Text += "*"
	def EndItalic(self):
		self.Text += "*"
	def AddItalic(self, text):
		self.StartItalic()
		self.Add(text)
		self.EndItalic()

	def StartBold(self):
		self.Text += "**"
	def EndBold(self):
		self.Text += "**"
	def AddBold(self, text):
		self.StartBold()
		self.Add(text)
		self.EndBold()

	def AddNl(self, text):
		# To create a line break or new line, end a line with two or more spaces, and then type return.
		self.Text += F"{text}  \n"

	def StartParagraph(self):
		self.Text += "\n\n"
	def EndParagraph(self):
		self.Text += "\n"
	def AddParagraph(self, text):
		self.Text += F"\n\n{text}\n"

	def Print(self):
		print(F"{self.Text}")

def main(argv):
	resume = GetResume()

	ctx = RenderContext(argv[0])

	resume.Render(ctx)

	ctx.Print()

	pass

if __name__ == "__main__":
	main(sys.argv[1:])
