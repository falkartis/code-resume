from myTypes import *


def GetResume():

	T = Translation


	name = "Falk Artis Bay"
	drivingLicense = T("Permís de conduir", "Permiso de conducir", "Driving license", "Führerschein")
	myDLicense = T("B, vehicle propi.", "B, vehículo propio.", "B, own vehicle.", "B, eigenes fahzeug.")

	languages = T("Idiomes","Idiomas","Languages","Sprachen")
	ca = Language("ca", T("Català", "Catalán", "Catalan", "Katalanisch"))
	es = Language("es", T("Castellà", "Castellano", "Spanish", "Spanisch"))
	en = Language("en", T("Angés", "Inglés", "English", "Englisch"))
	de = Language("de", T("Alemany", "Alemán", "German", "Deutsch"))
	myLangs = SkillSet([ca, es, en, de])

	others = T("Altres dades", "Otros datos", "Other information", "Sonstige angaben")
	myOthers = T(
		"Disponibilitat per desplaçar-me, canviar de residencia, fer torns rotatius, etc. segons retribució.",
		"Disponibilidad para desplazarme, cambiar de residencia, hacer turnos rotativos, etc. según retribución.",
		"Availability to move, change residence, rotate shifts, etc. according to remuneration.",
		"Bereitschaft für reisen, Wohnungswechsel, Schichtwechsel usw. nach Vergütung."
	)

	headers = [
		Header(drivingLicense, myDLicense),
		Header(languages, myLangs),
		Header(others, myOthers)
	]
	doctors = T(
		"Si el cos humà canvies al ritme que ho fa la tecnologia, els metges també es passarien el dia fent consultes a Google.",
		"Si el cuerpo humano cambiara al ritmo que lo hace la tecnología, los médicos también se pasarían el día haciendo consultas a Google.",
		"If the human body changed at the rate that technology does, doctors would also spend the entire day making queries on Google.",
		"Wenn sich der menschliche Körper so schnell verändern würde wie die Technologie, würden Ärzte auch den ganzen Tag mit Google verbringen."
	)
	quotes = [doctors]
	headerData = HeaderData(headers, quotes)

	dsPlace = T("Tècnic Servei d'assistència tècnica", "Técnico Servicio de asistencia técnica", "Help Desk Technician", "Help Desk Techniker")
	dsProjects = []
	damiaSolar = Job(dsPlace, "Damia Solar", "2020/08", "2022/07", "La Pobla de Segur", dsProjects)
	jobs = [damiaSolar]
	trainings = []
	projects = []

	translations = {}
	translations["jobsTitle"] = T("EXPERIÈNCIA PROFESSIONAL", "EXPERIENCIA PROFESIONAL", "PROFESSIONAL EXPERIENCE", "BERUFLICHE ERFAHRUNGEN")
	translations["trainTitle"] = T("FORMACIÓ ACADÈMICA", "FORMACIÓN ACADÉMICA", "ACADEMIC TRAINING", "AUSBILDUNG")
	translations["projectsTitle"] = T("PROJECTES PERSONALS", "PROYECTOS PERSONALES", "PERSONAL PROJECTS", "PERSÖNLICHE PROJEKTE")
	resume = Resume(name, headerData, jobs, trainings, projects, translations)

	return resume

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
