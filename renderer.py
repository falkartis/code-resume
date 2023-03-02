import sys

from data import GetResume


class RenderContext:
	def __init__(self, lang):
		self.Lang = lang
		self.Text = ""

	def Add(self, text):
		self.Text += F"\n{text}"

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
