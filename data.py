from myTypes import *


def GetResume():

	T = Translation


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
	languages = Translation("Idiomes","Idiomas","Languages","Sprachen")
	# Català, castellà, anglés, alemany
	# Catalán, castellano, inglés, alemán
	# Catalan, Spanish, English, German
	# Katalanisch, Spanisch, Englisch, Deutsch
	ca = Language("ca", T("Català", "Catalán", "Catalan", "Katalanisch"))
	es = Language("es", T("Castellà", "Castellano", "Spanish", "Spanisch"))
	en = Language("en", T("Angés", "Inglés", "English", "Englisch"))
	de = Language("de", T("Alemany", "Alemán", "German", "Deutsch"))
	myLangs = SkillSet([ca, es, en, de])
	headers = [
		Header(drivingLicense, myDLicense),
		Header(languages, myLangs)
	]
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
