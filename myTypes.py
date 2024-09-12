import os.path
import collections.abc

class IndexEntry:
	NextEntryNumber = 1
	def __init__(self):
		self.EntryNumber = IndexEntry.NextEntryNumber
		IndexEntry.NextEntryNumber = IndexEntry.NextEntryNumber + 1

	def IndexAnchor(self):
		return F"<a class=\"internAnchor\" name=\"ien{self.EntryNumber}\"></a>"

	def BodyAnchor(self):
		return F"<a class=\"internAnchor\" name=\"ben{self.EntryNumber}\"></a>"

	def IndexLink(self):
		return F" <a class=\"internLink\" href=\"#ien{self.EntryNumber}\">#</a>"
		
	def BodyLink(self):
		return F" <a class=\"internLink\" href=\"#ben{self.EntryNumber}\">#</a>"

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

		iconpath = F"img/skill_{self.Tag}.svg"
		if os.path.exists(iconpath):
			ctx.AddSkill(self.Tag, self)
			return ctx.Image(iconpath, self.Name)
		else:
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
	def __init__(self, name, description = None, tasks = None, skills = None, url = None, startDate = None, endDate = None):
		Activity.__init__(self, name, description, skills, url, endDate)
		self.Tasks = tasks
		self.StartDate = startDate

	def Render(self, ctx):

		txt = ""
		txt += ctx.Header(self.Name)
		txt += ctx.TableHead(" ", " ")

		if self.StartDate is not None and self.Date is not None:
			txt += ctx.TableRow(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.Date))
		elif self.StartDate is not None:
			txt += ctx.TableRow(ctx.Translations["date"], self.StartDate)
		elif self.Date is not None:
			txt += ctx.TableRow(ctx.Translations["date"], self.Date)

		if self.Description is not None:
			txt += ctx.TableRow(ctx.Translations["description"], self.Description)

		if self.Tasks is not None:
			if isinstance(self.Tasks, collections.abc.Sequence):
				txt += ctx.KeyAndValueP(ctx.Translations["tasks"], "")
				txt += ctx.StartList()
				for task in self.Tasks:
					txt += ctx.ListItem(task)
				txt += ctx.EndList()

			else:
				txt += ctx.TableRow(ctx.Translations["tasks"], self.Tasks)

		if self.Skills is not None:
			txt += ctx.TableRow(ctx.Translations["skills"], self.Skills)

		if self.Url is not None:
			txt += ctx.TableRow(ctx.Translations["link"], ctx.Link(self.Url, self.Url))

		return txt

class Event(Activity):
	def __init__(self, name, description, skills, url = None, date = None, location = None, extraData = None):
		Activity.__init__(self, name, description, skills, url, date)
		self.Location = location
		self.ExtraData = extraData
	
	def Render(self, ctx):
		txt = ""
		txt += ctx.Header(self.Name)
		txt += ctx.TableHead(" ", " ")

		if self.Date is not None:
			txt += ctx.TableRow(ctx.Translations["date"], ctx.Render(self.Date))

		if self.Location is not None:
			txt += ctx.TableRow(ctx.Translations["location"], self.Location)

		if self.Description is not None:
			txt += ctx.TableRow(ctx.Translations["event-description"], self.Description)

		if self.Skills is not None:
			txt += ctx.TableRow(ctx.Translations["skills"], self.Skills)

		if self.Url is not None:
			txt += ctx.TableRow(ctx.Translations["link"], ctx.Link(self.Url, self.Url))

		if self.ExtraData is not None:
			txt += ctx.Render(self.ExtraData)

		return txt

class Job(IndexEntry):
	def __init__(self, place, company, startDate, endDate, location, projects, skills = None):
		IndexEntry.__init__(self)
		self.Place = place
		self.Company = company
		self.StartDate = startDate
		self.EndDate = endDate
		self.Location = location
		self.Projects = projects
		self.Skills = skills

	def Render(self, ctx):
		txt = ""

		txt += ctx.Header(self.IndexAnchor(), self.Place, " – ", self.Company, self.BodyLink())

		txt += ctx.TableHead(" ", " ")
		txt += ctx.TableRow(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.EndDate))
		txt += ctx.TableRow(ctx.Translations["location"], self.Location)

		if self.Skills is not None:
			txt += ctx.TableRow(ctx.Translations["skills"], self.Skills)
		
		return txt

	def RenderProjects(self, ctx):
		txt = ""

		if self.Projects is not None:

			txt += ctx.Header(self.BodyAnchor(), self.Company, self.IndexLink())

			ctx.IncHeadLevel()
			for project in self.Projects:
				txt += ctx.Render(project)
			ctx.DecHeadLevel()
		
		return txt

class Training(IndexEntry):
	def __init__(self, name, startDate, endDate, school, location, projects = None, skills = None):
		IndexEntry.__init__(self)
		self.Name = name
		self.StartDate = startDate
		self.EndDate = endDate
		self.School = school
		self.Location = location
		self.Projects = projects
		self.Skills = skills

	def Render(self, ctx):
		txt = ""
		txt += ctx.Header(self.IndexAnchor(), self.Name, self.BodyLink())
		txt += ctx.TableHead(" "," ")
		txt += ctx.TableRow(ctx.Translations["interval"], ctx.Render(self.StartDate, " – ", self.EndDate))
		txt += ctx.TableRow(ctx.Translations["school"], self.School)
		txt += ctx.TableRow(ctx.Translations["location"], self.Location)

		if self.Skills is not None:
			txt += ctx.TableRow(ctx.Translations["skills"], self.Skills)
		
		return txt

	def RenderProjects(self, ctx):
		txt = ""

		if self.Projects is not None:
			txt += ctx.Header(self.BodyAnchor(), self.Name, self.IndexLink())
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
		return ctx.TableRow(self.Key, self.Value)

class HeaderData:
	def __init__(self, headers, quotes):
		self.Headers = headers
		self.Quotes = quotes

	def Render(self, ctx):
		txt = ""
		txt += ctx.TableHead(" "," ")
		for header in self.Headers:
			txt += ctx.Render(header)
		
		txt += ctx.RenderGitStatus()
		
		for quote in self.Quotes:
			txt += ctx.Paragraph("> ", ctx.Italic(quote))
		return txt

class Resume:
	def __init__(self, name, headerData, jobs, trainings, projects, otherJobs, otherTrainings):
		self.Name = name
		self.HeaderData = headerData
		self.Jobs = jobs
		self.Trainings = trainings
		self.Projects = projects
		self.OtherJobs = otherJobs
		self.OtherTrainings = otherTrainings
	
	def Render(self, ctx):

		txt = ""

		txt += ctx.Header(self.Name)
		txt += ctx.Render(self.HeaderData)

		txt += ctx.Header(ctx.Translations["jobsTitle"])

		ctx.IncHeadLevel()
		ctx.IncHeadLevel()
		for job in self.Jobs:
			txt += ctx.Render(job)
		ctx.DecHeadLevel()
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["trainTitle"])

		ctx.IncHeadLevel()
		ctx.IncHeadLevel()
		for training in self.Trainings:
			txt += ctx.Render(training)
		ctx.DecHeadLevel()
		ctx.DecHeadLevel()

		# TODO: add here list of personal projects

		txt += ctx.Header(ctx.Translations["otherJobsTitle"])

		ctx.IncHeadLevel()
		ctx.IncHeadLevel()
		for job in self.OtherJobs:
			txt += ctx.Render(job)
		ctx.DecHeadLevel()
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["otherTrainTitle"])

		ctx.IncHeadLevel()
		ctx.IncHeadLevel()
		for training in self.OtherTrainings:
			txt += ctx.Render(training)
		ctx.DecHeadLevel()
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["annex"])

		txt += ctx.Header(ctx.Translations["workProjects"])

		ctx.IncHeadLevel()
		for job in self.Jobs:
			txt += job.RenderProjects(ctx)
		for job in self.OtherJobs:
			txt += job.RenderProjects(ctx)
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["academicProjects"])

		ctx.IncHeadLevel()
		for training in self.Trainings:
			txt += training.RenderProjects(ctx)
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["personalProjects"])

		ctx.IncHeadLevel()
		ctx.IncHeadLevel()
		for project in self.Projects:
			txt += ctx.Render(project)
		ctx.DecHeadLevel()
		ctx.DecHeadLevel()

		txt += ctx.Header(ctx.Translations["icons"])

		txt += ctx.RenderSkills()
		return txt



def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
