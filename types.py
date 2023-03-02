class Translation:
	def __init__(self, ca, es, en, de):
		self.Ca = ca
		self.Es = es
		self.En = en
		self.De = de

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

class HeaderData:
	def __init__(self, headers, quotes):
		self.Headers = headers
		self.Quotes = quotes

class Resume:
	def __init__(self, name, headerData, jobs, trainings, projects):
		self.Name = name
		self.HeaderData = headerData
		self.Jobs = jobs
		self.Trainings = trainings
		self.Projects = projects
		


def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
