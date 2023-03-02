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
	def __init__(self, tag, name):
		self.Tag = tag
		self.Name = name

class Language(Skill):
	def __init__(self):
		super(Language, self).__init__()
		

class Project:
	def __init__(self, name, description, tasks, skills):
		self.Name = name
		self.Description = description
		self.Tasks = tasks
		self.Skills = skills

class Job:
	def __init__(self, place, company, startDate, endDate, location, projects):
		self.Place = place
		self.Company = company
		self.StartDate = startDate
		self.EndDate = endDate
		self.Location = location
		self.Projects = projects
						

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
		self.Key.Render(ctx)
		self.Value.Render(ctx)


class HeaderData:
	def __init__(self, headers, quotes):
		self.Headers = headers
		self.Quotes = quotes

	def Render(self, ctx):
		for header in self.Headers:
			header.Render(ctx)
		for quote in self.Quotes:
			quote.Render(ctx)

class Resume:
	def __init__(self, name, headerData, jobs, trainings, projects):
		self.Name = name
		self.HeaderData = headerData
		self.Jobs = jobs
		self.Trainings = trainings
		self.Projects = projects
	
	def Render(self, ctx):
		ctx.Add(self.Name)
		self.HeaderData.Render(ctx)

		# TODO: push section
		# TODO: add title
		# TODO: pop section

		for job in self.Jobs:
			job.Render(ctx)
		for training in self.Trainings:
			training.Render(ctx)
		for project in self.Projects:
			project.Render(ctx)


def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
