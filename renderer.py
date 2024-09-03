import sys

from data import GetResume, GetExtraTranslations
from private_data import GetPrivateData

class RenderContext:
	def __init__(self, lang, gitStatus, translations):
		self.Lang = lang
		self.Translations = translations
		self.GitStatus = gitStatus
		self.Text = ""
		self.HeadLevel = 1
		self.Skills = {}

	def RenderGitStatus(self):
		return F"<p class=\"revision\"><span class=\"label\">Revision:</span> <span class=\"value\"span>{self.GitStatus}</span></p>"

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
			elif type(arg) is list:
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
		return "\n\n"

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


	def EndList(self):
		return "\n\n"
	def StartList(self):
		return "\n\n"
	def ListItem(self, *args):
		txt = ""
		txt += " + "
		txt += self.RenderThem(args)
		txt += "\n"
		return txt

	def Image(self, url, title = None):
		if title is None:
			title = " "
		else:
			title = self.Render(title)
		return F"![{title}]({url} \"{title}\")"

	def TableHead(self, *args):
		txt = ""
		txt += "|"
		count = 0
		for arg in args:
			txt += " "
			txt += self.Render(arg)
			txt += " |"
			count += 1
		txt += "\n"
		txt += "|"
		for i in range(count):
			txt += " --- |"
		txt += "\n"
		return txt

	def TableRow(self, *args):
		txt = ""
		txt += "|"
		for arg in args:
			txt += " "
			txt += self.Render(arg)
			txt += " |"
		txt += "\n"
		return txt

	def AddSkill(self, tag, skill):
		self.Skills[tag] = skill

	def RenderSkills(self):
		txt = ""
		first = True
		for tag in self.Skills:
			if first:
				first = False
			else:
				txt += ", "
			skill = self.Skills[tag]
			txt += self.Render(skill)
			txt += ": "
			txt += self.Render(skill.Name)
		return txt

def main(argv):

	privateData = GetPrivateData()
	resume = GetResume(privateData)
	extraTranslations = GetExtraTranslations()

	ctx = RenderContext(argv[0], argv[1], extraTranslations)

	txt = resume.Render(ctx)

	print(txt)

if __name__ == "__main__":

	main(sys.argv[1:])
