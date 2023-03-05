class Translation:
	def __init__(self, ca, es, en, de):
		self.Ca = ca
		self.Es = es
		self.En = en
		self.De = de

	def Render(self, ctx):
		match ctx.Lang:
			case "ca":
				return ctx.Render(self.Ca)
			case "es":
				return ctx.Render(self.Es)
			case "en":
				return ctx.Render(self.En)
			case "de":
				return ctx.Render(self.De)
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
		return ctx.Render(self.Name)

class Language(Skill):
	def __init__(self, tag, name):
		Skill.__init__(self, tag, name)
		
class SkillSet:
	def __init__(self, skills):
		self.Skills = skills

	def Render(self, ctx):
		txt = ""
		first = True
		for skill in self.Skills:
			if first:
				first = False
			else:
				txt += ctx.Render(", ")
			txt += ctx.Render(skill)
		return txt

class Activity:
	def __init__(self, name, description, skills, url, date):
		self.Name = name
		self.Description = description
		self.Skills = skills
		self.Date = date
		self.Url = url

class Project(Activity):
	def __init__(self, name, description, tasks, skills, url = None, startDate = None, endDate = None):
		Activity.__init__(self, name, description, skills, url, endDate)
		self.Tasks = tasks
		self.StartDate = startDate

	def Render(self, ctx):

		txt = ""
		txt += ctx.Header(self.Name)

		if self.StartDate is not None and self.Date is not None:
			txt += ctx.KeyAndValueNl(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.Date))
		elif self.StartDate is not None:
			txt += ctx.KeyAndValueNl(ctx.Translations["date"], ctx.Render(self.StartDate))
		elif self.Date is not None:
			txt += ctx.KeyAndValueNl(ctx.Translations["date"], ctx.Render(self.Date))

		if self.Description is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["description"], self.Description)

		if self.Tasks is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["tasks"], self.Tasks)

		if self.Skills is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["skills"], self.Skills)

		if self.Url is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["link"], ctx.Link(self.Url, self.Url))

		return txt

class Event(Activity):
	def __init__(self, name, description, skills, url, date, location):
		Activity.__init__(self, name, description, skills, url, date)
		self.Location = location
	
	def Render(self, ctx):
		txt = ""
		txt += ctx.Header(self.Name)

		if self.Location is not None:
			txt += ctx.KeyAndValueNl(ctx.Translations["location"], self.Location)
			
		if self.Date is not None:
			txt += ctx.KeyAndValueNl(ctx.Translations["date"], ctx.Render(self.Date))

		if self.Description is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["event-description"], self.Description)

		if self.Skills is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["skills"], self.Skills)

		if self.Url is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["link"], ctx.Link(self.Url, self.Url))

		return txt


class Job:
	def __init__(self, place, company, startDate, endDate, location, projects, skills = None):
		self.Place = place
		self.Company = company
		self.StartDate = startDate
		self.EndDate = endDate
		self.Location = location
		self.Projects = projects
		self.Skills = skills

	def Render(self, ctx):
		txt = ""

		txt += ctx.Header(self.Place, " – ", self.Company)
		txt += ctx.KeyAndValueNl(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.EndDate))
		txt += ctx.KeyAndValueNl(ctx.Translations["location"], self.Location)

		if self.Skills is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["skills"], self.Skills)

		if self.Projects is not None:
			ctx.IncHeadLevel()
			for project in self.Projects:
				txt += ctx.Render(project)
			ctx.DecHeadLevel()
		
		return txt

class Training:
	def __init__(self, name, startDate, endDate, school, location, projects = None, skills = None):
		self.Name = name
		self.StartDate = startDate
		self.EndDate = endDate
		self.School = school
		self.Location = location
		self.Projects = projects
		self.Skills = skills

	def Render(self, ctx):
		txt = ""
		txt += ctx.Header(self.Name)
		txt += ctx.KeyAndValueNl(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.EndDate))
		txt += ctx.KeyAndValueNl(ctx.Translations["school"], self.School)
		txt += ctx.KeyAndValueNl(ctx.Translations["location"], self.Location)

		if self.Skills is not None:
			txt += ctx.KeyAndValueP(ctx.Translations["skills"], self.Skills)

		if self.Projects is not None:
			ctx.IncHeadLevel()
			for project in self.Projects:
				txt += ctx.Render(project)
			ctx.DecHeadLevel()
		
		return txt


class Header:
	def __init__(self, key, value):
		self.Key = key
		self.Value = value

	def Render(self, ctx):
		return ctx.KeyAndValueNl(self.Key, self.Value)


class HeaderData:
	def __init__(self, headers, quotes):
		self.Headers = headers
		self.Quotes = quotes

	def Render(self, ctx):
		txt = ""
		for header in self.Headers:
			txt += ctx.Render(header)
		for quote in self.Quotes:
			txt += ctx.Paragraph("> ", ctx.Italic(quote))
		return txt

class Resume:
	def __init__(self, name, headerData, jobs, trainings, projects):
		self.Name = name
		self.HeaderData = headerData
		self.Jobs = jobs
		self.Trainings = trainings
		self.Projects = projects
	
	def Render(self, ctx):

		txt = ""
		txt += ctx.Header(self.Name)
		txt += ctx.Render(self.HeaderData)
		txt += ctx.Header(ctx.Translations["jobsTitle"])

		ctx.IncHeadLevel()
		for job in self.Jobs:
			txt += ctx.Render(job)
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["trainTitle"])

		ctx.IncHeadLevel()
		for training in self.Trainings:
			txt += ctx.Render(training)
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["projectsTitle"])

		ctx.IncHeadLevel()
		for project in self.Projects:
			txt += ctx.Render(project)
		ctx.DecHeadLevel()
		return txt


def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
