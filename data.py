from myTypes import *


def GetResume():
	name = "Falk Artis Bay"
	drivingLicense = Translation(
		"Permís de conduir",
		"Permiso de conducir",
		"Driving license",
		"Führerschein"
	)
	myDLicense = Translation(
		"B, vehicle propi.",
		"B, vehículo propio.",
		"B, own vehicle.",
		"B, eigenes fahzeug."
	)
	headers = [Header(drivingLicense, myDLicense)]
	doctors = Translation(
		"Si el cos humà canvies al ritme que ho fa la tecnologia, els metges també es passarien el dia fent consultes a Google",
		"Si el cuerpo humano cambiara al ritmo que lo hace la tecnología, los médicos también se pasarían el día haciendo consultas a Google",
		"If the human body changed at the rate that technology does, doctors would also spend the entire day making queries on Google",
		"Wenn sich der menschliche Körper so schnell verändern würde wie die Technologie, würden Ärzte auch den ganzen Tag mit Google verbringen"
	)
	quotes = [doctors]
	headerData = HeaderData(headers, quotes)
	jobs = []
	trainings = []
	projects = []
	return Resume(name, headerData, jobs, trainings, projects)

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
