import sys

from data import GetResume, GetExtraTranslations


class RenderContext:
	def __init__(self, lang, translations):
		self.Lang = lang
		self.Translations = translations
		self.Text = ""
		self.HeadLevel = 1


	def RenderArg(self, arg):
		txt = ""
		if callable(getattr(arg, 'Render', None)):
			tmp = arg.Render(self)
			if tmp is None:
				raise NotImplementedError(F"Render didn't return anything, not correctly implemented {arg}")
			else:
				txt += tmp
		else:
			if type(arg) is tuple:
				txt += self.RenderThem(arg)
			else:
				txt += arg
		return txt

	def RenderThem(self, args):
		txt = ""
		for arg in args:
			txt += self.RenderArg(arg)
		return txt


	def Render(self, *args):
		return self.RenderThem(args)


	def IncHeadLevel(self):
		self.HeadLevel += 1
	def DecHeadLevel(self):
		if self.HeadLevel > 1:
			self.HeadLevel -= 1

	def StartHeader(self):
		return F"\n\n" + "#" * self.HeadLevel + " "

	def EndHeader(self):
		return "\n"

	def Header(self, *args):
		txt = ""
		txt += self.StartHeader()
		txt += self.RenderThem(args)
		txt += self.EndHeader()
		return txt

	def StartItalic(self):
		return "*"
	def EndItalic(self):
		return "*"
	def Italic(self, *args):
		txt = ""
		txt += self.StartItalic()
		txt += self.RenderThem(args)
		txt += self.EndItalic()
		return txt

	def StartBold(self):
		return "**"
	def EndBold(self):
		return "**"
	def Bold(self, *args):
		txt = ""
		txt += self.StartBold()
		txt += self.RenderThem(args)
		txt += self.EndBold()
		return txt

	def StartParagraph(self):
		return "\n\n"
	def EndParagraph(self):
		return "\n"
	def Paragraph(self, *args):
		txt = ""
		txt += self.StartParagraph()
		txt += self.RenderThem(args)
		txt += self.EndParagraph()
		return txt

	def NewLine(self):
		# To create a line break or new line, end a line with two or more spaces, and then type return.
		return "  \n"

	def KeyAndValueNl(self, key, value):
		txt = ""
		txt += self.Bold(key, ":")
		txt += self.Render(" ", value)
		txt += self.NewLine()
		return txt

	def KeyAndValueP(self, key, value):
		txt = ""
		txt += self.StartParagraph()
		txt += self.Bold(key, ":")
		txt += self.Render(" ", value)
		txt += self.EndParagraph()
		return txt

	def Link(self, text, url, title = None):
		if title is None:
			return F"[{text}]({url})"
		else:
			return F"[{text}]({url} \"{title}\")"



def main(argv):

	resume = GetResume()
	extraTranslations = GetExtraTranslations()

	ctx = RenderContext(argv[0], extraTranslations)

	txt = resume.Render(ctx)

	print(txt)

	pass

if __name__ == "__main__":
	main(sys.argv[1:])
