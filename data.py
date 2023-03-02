import types

def GetResume():
	name = "Falk Artis Bay"
	headerData = ""	#TODO: implement this
	jobs = []
	trainings = []
	projects = []
	return Resume(name, headerData, jobs, trainings, projects)

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
