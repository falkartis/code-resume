class Translation:
	def __init__(self, ca, es, en, de):
		self.Ca = ca
		self.Es = es
		self.En = en
		self.De = de

	def Render(self, ctx):
		match ctx.Lang:
			case "ca":
				ctx.Add(self.Ca)
			case "es":
				ctx.Add(self.Es)
			case "en":
				ctx.Add(self.En)
			case "de":
				ctx.Add(self.De)
			case _:
				print (F"Language {ctx.Lang} not implemented.")

class Skill:
	def __init__(self, tag, name = None):
		self.Tag = tag
		if name is None:
			self.Name = tag
		else:
			self.Name = name

	def Render(self, ctx):
		# TODO: detect string or class
		if callable(getattr(self.Name, 'Render', None)):
			self.Name.Render(ctx)
		else:
			ctx.Add(self.Name)

class Language(Skill):
	def __init__(self, tag, name):
		Skill.__init__(self, tag, name)
		
class SkillSet:
	def __init__(self, skills):
		self.Skills = skills

	def Render(self, ctx):
		first = True
		for skill in self.Skills:
			if first:
				first = False
			else:
				ctx.Add(", ")
			skill.Render(ctx)

class Project:
	def __init__(self, name, description, tasks, skills):
		self.Name = name
		self.Description = description
		self.Tasks = tasks
		self.Skills = skills

	def Render(self, ctx):
		ctx.StartHeader()
		self.Name.Render(ctx)
		ctx.EndHeader()

		if self.Description is not None:
			ctx.StartBold()
			ctx.Translations["description"].Render(ctx)
			ctx.Add(": ")
			ctx.EndBold()
			self.Description.Render(ctx)
			ctx.AddNl("")

		if self.Tasks is not None:
			ctx.StartBold()
			ctx.Translations["tasks"].Render(ctx)
			ctx.Add(": ")
			ctx.EndBold()
			self.Tasks.Render(ctx)
			ctx.AddNl("")

		if self.Skills is not None:
			ctx.StartBold()
			ctx.Translations["skills"].Render(ctx)
			ctx.Add(": ")
			ctx.EndBold()
			self.Skills.Render(ctx)
			ctx.AddNl("")

class Job:
	def __init__(self, place, company, startDate, endDate, location, projects):
		self.Place = place
		self.Company = company
		self.StartDate = startDate
		self.EndDate = endDate
		self.Location = location
		self.Projects = projects
	def Render(self, ctx):
		ctx.StartHeader()
		self.Place.Render(ctx)
		ctx.Add(" – ")
		ctx.Add(self.Company)
		ctx.EndHeader()

		ctx.StartBold()
		ctx.Translations["interval"].Render(ctx)
		ctx.Add(":")
		ctx.EndBold()
		ctx.AddNl(F" {self.StartDate} – {self.EndDate}")

		ctx.StartBold()
		ctx.Translations["location"].Render(ctx)
		ctx.Add(":")
		ctx.EndBold()
		ctx.AddNl(F" {self.Location}")

		ctx.IncHeadLevel()
		for project in self.Projects:
			project.Render(ctx)
		ctx.DecHeadLevel()

class Training:
	def __init__(self, name, startDate, endDate, school, location, projects):
		self.Name = name
		self.StartDate = startDate
		self.EndDate = endDate
		self.School = school
		self.Location = location
		self.Projects = projects

class Header:
	def __init__(self, key, value):
		self.Key = key
		self.Value = value

	def Render(self, ctx):
		ctx.StartBold()
		self.Key.Render(ctx)
		ctx.Add(":")
		ctx.EndBold()
		ctx.Add(" ")
		self.Value.Render(ctx)
		ctx.AddNl("")


class HeaderData:
	def __init__(self, headers, quotes):
		self.Headers = headers
		self.Quotes = quotes

	def Render(self, ctx):
		for header in self.Headers:
			header.Render(ctx)
		for quote in self.Quotes:
			ctx.StartParagraph()
			ctx.Add("> ")
			ctx.StartItalic()
			quote.Render(ctx)
			ctx.EndItalic()
			ctx.EndParagraph()

class Resume:
	def __init__(self, name, headerData, jobs, trainings, projects):
		self.Name = name
		self.HeaderData = headerData
		self.Jobs = jobs
		self.Trainings = trainings
		self.Projects = projects
	
	def Render(self, ctx):

		ctx.AddHeader(self.Name)
		self.HeaderData.Render(ctx)

		ctx.StartHeader()
		ctx.Translations["jobsTitle"].Render(ctx)
		ctx.EndHeader()
		ctx.IncHeadLevel()
		for job in self.Jobs:
			job.Render(ctx)
		ctx.DecHeadLevel()

		ctx.StartHeader()
		ctx.Translations["trainTitle"].Render(ctx)
		ctx.EndHeader()
		ctx.IncHeadLevel()
		for training in self.Trainings:
			training.Render(ctx)
		ctx.DecHeadLevel()

		ctx.StartHeader()
		ctx.Translations["projectsTitle"].Render(ctx)
		ctx.EndHeader()
		ctx.IncHeadLevel()
		for project in self.Projects:
			project.Render(ctx)
		ctx.DecHeadLevel()


def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
