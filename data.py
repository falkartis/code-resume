from myTypes import *


def GetResume():

	T = Translation


	name = "Falk Artis Bay"
	drivingLicense = T("Permís de conduir", "Permiso de conducir", "Driving license", "Führerschein")
	myDLicense = T("B, vehicle propi.", "B, vehículo propio.", "B, own vehicle.", "B, eigenes fahzeug.")

	languages = T("Idiomes","Idiomas","Languages","Sprachen")
	ca = Language("ca", T("Català", "Catalán", "Catalan", "Katalanisch"))
	es = Language("es", T("Castellà", "Castellano", "Spanish", "Spanisch"))
	en = Language("en", T("Anglès", "Inglés", "English", "Englisch"))
	de = Language("de", T("Alemany", "Alemán", "German", "Deutsch"))
	myLangs = SkillSet([ca, es, en, de])
	seo = Skill("SEO")
	presta = Skill("Prestashop")
	cletu = Skill("Cletu")
	linux = Skill("Linux")
	electr = Skill("electr", T("Electricitat", "Electricidad", "Electricity", "Elektrizität"))
	schema = Skill("schema", T("Esquemes elèctrics", "Esquemas eléctricos", "Electrical schematics", "Schaltpläne"))
	kicad = Skill("KiCad")
	team = Skill("team", T("Treball en equip", "Trabajo en equipo", "Teamwork", "Teamarbeit"))
	git = Skill("Git")
	solar = Skill("solar", T("energia solar", "energía solar", "solar energy", "Solarenergie"))
	wind = Skill("wind", T("energia eòlica", "energía eólica", "wind energy", "Windenergie"))
	customer = Skill("customer", T("Comunicació amb clients", "Comunicación con clientes", "Customer Communication", "Kundenkommunikation"))
	incident = Skill("incident", T("Gestió d'incidències", "Gestión de incidencias", "Incident Management", "Incident Management"))
	logistic = Skill("logistic", T("Logística", "Logística", "Logistics", "Logistik"))
	diplomacy = Skill("diplomacy", T("Diplomàcia", "Diplomacia", "Diplomacy", "Diplomatie"))
	document = Skill("document", T("Documentació", "Documentación", "Documentation", "Dokumentation"))
	warranty = Skill("warranty", T("Gestió de garanties", "Gestión de garantías", "Warranty Management", "Garantiemanagement"))
	optim = Skill("optim", T("Optimització de processos", "Optimización de procesos", "Process Optimization", "Prozessoptimierung"))
	oop = Skill("oop",T("Programació orientada a objectes","Programación orientada a objetos","Object Oriented Programming","Objektorientierte Programmierung"))
	cs = Skill("C#")
	dotnet = Skill("dotnet", ".Net (Framework, Core, Standard)")
	antlr = Skill("ANTLR")
	grammar = Skill("grammar", T("Gramàtica", "Gramática", "Grammar", "Grammatik"))
	syntax = Skill("syntax", T("Sintaxis", "Sintaxis", "Syntax", "Syntax"))
	visualstudio = Skill("Visual studio")
	jenkins = Skill("Jenkins")
	bash = Skill("Bash")
	sonarQube = Skill("Sonar Qube")
	ci = Skill("ci", T("Integració continua", "Integración continua", "Continuous Integration", "Continuous Integration"))
	cd = Skill("cd", T("Entrega continua", "Entrega continua", "Continuous Delivery", "Continuous Delivery"))
	ifc = Skill("IFC")
	geo3d = Skill("3D", T("geometria 3D", "geometría 3D", "3D Geometry", "3D-Geometrie"))
	algebra = Skill("linear-algebra", T("Àlgebra lineal", "Álgebra lineal", "Linear Algebra", "Lineare Algebra"))
	sqlite = Skill("SqLite")
	litedb = Skill("LiteDB")
	json = Skill("JSON")
	blender = Skill("Blender")
	unity = Skill("Unity 3D")
	aspnet = Skill("ASP.NET")
	html = Skill("HTML")
	js = Skill("JavaScript")
	webservice = Skill("WebService")
	api = Skill("API")
	doxygen = Skill("Doxygen")
	entityFrame = Skill("Entity Framework")
	distributed = Skill("distributed-systems", T("Sistemes distribuïts", "Sistemas distribuidos", "Distributed Systems", "Verteilte Systeme"))
	sqlServer = Skill("SQL Server")
	entityFrCore = Skill("Entity Framework Core")
	security = Skill("security", T("Seguretat", "Seguridad", "Security", "Sicherheit"))
	crypto = Skill("crypto", T("Criptografia", "Criptografía", "Cryptography", "Kryptografie"))
	graphql = Skill("GraphQL")
	angular = Skill("Angular")
	ts = Skill("TypeScript")
	css = Skill("CSS")
	responsive = Skill("Responsive")
	cpp = Skill("C/C++")




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
		"Si el cos humà canvies al ritme que ho fa la tecnologia, els metges també es passarien el dia fent consultes a internet.",
		"Si el cuerpo humano cambiara al ritmo que lo hace la tecnología, los médicos también se pasarían el día haciendo consultas a internet.",
		"If the human body changed at the rate that technology does, doctors would also spend the entire day making queries on internet.",
		"Wenn sich der menschliche Körper so schnell verändern würde wie die Technologie, würden Ärzte auch den ganzen Tag mit Internet verbringen."
	)
	tractor = T(
		"Amb un cotxe de carreres no pots llaurar el camp, amb un tractor si.",
		"Con un coche de carreras no puedes labrar el campo, con un tractor sí.",
		"With a racing car you can't plow the field, with a tractor you can.",
		"Mit einem Rennwagen kann man das Feld nicht pflügen, mit einem Traktor schon."
	)
	quotes = [doctors, tractor]
	headerData = HeaderData(headers, quotes)

	dsPlace = T("Tècnic Servei d'assistència tècnica", "Técnico Servicio de asistencia técnica", "Help Desk Technician", "Help Desk Techniker")
	dsWeb = Project(
		T("Revisió i migració web", "Revisión y migración web" , "Web review and migration", "Web-Überprüfung und -Migration"),
		None,
		T(
			"La meva funció era la de revisar la migració de la botiga en línia des d’una plataforma obsoleta a una nova plataforma. També revisar continguts del blog i informes de SEO.",
			"Mi función era la de revisar la migración de la tienda online desde una plataforma obsoleta a una nueva plataforma. También revisar contenidos del blog e informes de SEO.",
			"My role was to review the migration of the online store from an outdated platform to a new platform. Also to review blog content and SEO reports.",
			"Meine Rolle bestand darin, die Migration des Online-Shops von einer veralteten Plattform auf eine neue Plattform zu überprüfen. Auch Blog-Inhalte und SEO-Berichte zu überprüfen."),
		SkillSet([seo, presta, cletu, linux])
	)
	dsTesting = Project(
		T("Banc de proves", "Banco de pruebas", "Test bank", "Prüfstand"),
		None,
		T(
			"Planificar la instal·lació de panells fotovoltaics, dissenyar un quadre elèctric, posar a prova equips, implementar millores.",
			"Planificar la instalación de paneles fotovoltaicos, diseñar un cuadro eléctrico, poner a prueba equipos, implementar mejoras.",
			"Plan the installation of photovoltaic panels, design an electrical panel, test equipment, implement improvements.",
			"Die Installation von Photovoltaikmodulen planen, entwurf eines elektrisches Panel, Geräte testen, Verbesserungen implementieren."
		),
		SkillSet([electr, schema, kicad, team, git, linux, solar, wind])
	)
	dsSAT = Project(
		T("Servei d'assistència tècnica", "Servicio de asistencia técnica", "Help Desk", "Help Desk"),
		None,
		T(
			"Resoldre els dubtes i les incidències que es poden trobar els clients amb els productes de l’empresa. Donar consells i indicacions a companys/es de l’empresa. Diagnosticar avaries i reparar equips. Implementar millores.",
			"Resolver las dudas y las incidencias que pueden encontrarse los clientes con los productos de la empresa. Dar consejos e indicaciones a compañeros/as de la empresa. Diagnosticar averías y reparar equipos. Implementar mejoras.",
			"Resolve doubts and incidents that customers may encounter with the company's products. Give advice and instructions to company colleagues. Diagnose faults and repair equipment. Implement improvements.",
			"Beheben von Zweifel und Vorfälle, die Kunden mit den Produkten des Unternehmens begegnen können. Kollegen im Unternehmen Ratschläge und Anweisungen Geben. Fehler diagnostizieren und Geräte reparieren. Verbesserungen implementieren."
		),
		SkillSet([customer, incident, logistic, diplomacy, document, team, warranty, en, de, linux, solar, wind, optim])
	)
	dsProjects = [dsWeb, dsTesting, dsSAT]
	damiaSolar = Job(dsPlace, "Damia Solar", "2020/08", "2022/07", "La Pobla de Segur", dsProjects)


	iCore9 = Project(
		"iCore9",
		T(
			"iCore9 es un paquet de llibreries de gestió i procés de dades BIM desenvolupat conjuntament amb Apogea consulting.",
			"iCore9 es un paquete de librerías de gestión y proceso de datos BIM desarrollado conjuntamente con Apogea consulting.",
			"iCore9 is a package of BIM data management and process libraries developed together with Apogea consulting.",
			"iCore9 ist ein Paket aus BIM-Datenmanagement und Prozessbibliotheken, das zusammen mit Apogea Consulting entwickelt wurde."
		),
		T(
			"Implementació d’un parser d’arxius IFC (similar a step), una llibreria de geometria 3D, un tessel·lador, un processador/optimitzador geomètric, un visor 3D web, funcions de desat i exportació, un sistema de llicencies. Documentació de funcionalitats.",
			"Implementación de un parser de archivos IFC (similar a step), una librería de geometría 3D, un teselador, un procesador/optimizador geométrico, un visor 3D web, funciones de guardado y exportación, un sistema de licencias. Documentación de funcionalidades.",
			"Implementation of an IFC (similar to step) file parser, a 3D geometry library, a tessellator, a geometric processor/optimizer, a 3D web viewer, save and export functions, a licensing system. Functionality documentation.",
			"Implementierung eines IFC-Dateiparsers (ähnlich zu step), einer 3D-Geometriebibliothek, eines Tessellators, eines geometrischen Prozessors/Optimierers, eines 3D-Web-Viewers, Speicher- und Exportfunktionen, eines Lizenzsystems. Dokumentation der Funktionalität."
		),
		SkillSet([oop, cs, dotnet, antlr, grammar, syntax, visualstudio, git, jenkins, linux, bash, sonarQube, ci, cd, ifc, geo3d, algebra, sqlite, litedb, json, blender, unity, aspnet, html, js, webservice, api, team, doxygen, entityFrame, en, optim])
	)

	ndbim = Project(
		"NdBim",
		T(
			"ndBim es una plataforma en línia de treball col·laboratiu especialitzat en totes les fases de una obra.",
			"ndBim es una plataforma online de trabajo colaborativo especializado en todas las fases de una obra.",
			"ndBim is an online platform for collaborative work specialized in all phases of construction.",
			"ndBim ist eine kollaborative Online-Arbeitsplattform, die auf alle Bauphasen spezialisiert ist"
		),
		T(
			"Disseny i implementació del backend de la plataforma, la base de dades, els sistemes de seguretat, el xifrat de les dades d’usuari, calculadora de costos. Implementació del frontend.",
			"Diseño e implementación del backend de la plataforma, base de datos, sistemas de seguridad, cifrado de los datos de usuario, calculadora de costes. Implementación del frontendo.",
			"Design and implementation of the platform backend, database, security systems, user data encryption, cost calculator. Implementation of the frontend.",
			"Design und Implementierung des Plattform-Backends, der Datenbank, der Sicherheitssysteme, der Benutzerdatenverschlüsselung, des Kostenrechners. Implementierung des Frontends."
		),
		SkillSet([distributed, oop, cs, antlr, grammar, syntax, visualstudio, git, jenkins, sonarQube, ci, cd, sqlServer, entityFrCore, security, crypto, api, graphql, html, angular, ts, css, team, responsive, en])
	)

	oda = Project(
		"Open Design Alliance",
		T(
			"La llibreria de l’open design alliance, es coneguda per ser farragosa i complicada de fer servir. L’objectiu era d’aportar un conjunt de funcionalitats per facilitar la implantació de la llibreria.",
			"La librería del open design aliance, es conocida por ser engorrosas y complicada de utilizar. El objetivo era aportar un conjunto de funcionalidades para facilitar la implantación de la librería.",
			"The open design alliance library is known to be cumbersome and complicated to use. The goal was to provide a set of functionalities to facilitate the implementation of the library.",
			"Die Open Design Alliance Funktionenbibliothek ist bekanntermaßen umständlich und kompliziert zu bedienen. Das Ziel war es, eine Reihe von Funktionalitäten bereitzustellen, um die Implementierung der Bibliothek zu erleichtern."
		),
		T(
			"Implementar un conjunt de funcionalitats embolcall per a accedir a les funcions pròpies de la ODA.",
			"Implementar un conjunto de funcionalidades envoltura para acceder a las funciones propias de la ODA.",
			"Implement a set of wrapper functions to access the ODA's own functions.",
			"Implementierung von eine Reihe von Wrapper-Funktionen, um auf die eigenen Funktionen des ODA zuzugreifen."
		),
		SkillSet([oop, cpp, visualstudio, git, jenkins, ci, cd, api, team])
	)

	bim360 = Project(
		T("Client API BIM-360", "Cliente API BIM-360", "BIM-360 API Client", "BIM-360-API-Client"),
		T(
			"La api BIM-360 d’Autodesk ofereix una plataforma de gestió de documents relacionats amb l’arquitectura.",
			"La apio BIM-360 de Autodesk ofrece una plataforma de gestión de documentos relacionados con la arquitectura.",
			"Autodesk's BIM-360 API provides an architecture-related document management platform.",
			"Die BIM-360-API von Autodesk bietet eine architekturbezogene Dokumentenverwaltungsplattform."
		),
		T(
			"Dissenyar i implementar un client de la API.",
			"Diseñar e implementar un cliente de la API.",
			"Design and implement an API client.",
			"Entwurf und implementierung von einen API-Client."
		),
		SkillSet([oop, cs, visualstudio, git, linux, bash, api, json])
	)

	hscProjects = [iCore9, ndbim, oda, bim360]
	handle = Job(T("Programador", "Programador", "Programmer", "Programmierer"),"Handle Software Company", "2018/06", "2020/03", "Lleida", hscProjects)



	alcoletgeProjects = [
		Project(
		),
		Project(
		)
	]
	becariAlcoletge = Job(
		T("Becari", "Becario", "Intern", "Praktikant"),
		T("Taller de electrònica", "Taller de electrónica", "Electronics workshop", "Elektronik Werkstatt"),
		"2018/02", "2018/06", "Alcoletge", alcoletgeProjects
	)



	jobs = [damiaSolar, handle, becariAlcoletge]
	trainings = []
	projects = []

	resume = Resume(name, headerData, jobs, trainings, projects)

	return resume

def GetExtraTranslations():
	T = Translation

	translations = {}
	translations["jobsTitle"] = T("EXPERIÈNCIA PROFESSIONAL", "EXPERIENCIA PROFESIONAL", "PROFESSIONAL EXPERIENCE", "BERUFLICHE ERFAHRUNGEN")
	translations["trainTitle"] = T("FORMACIÓ ACADÈMICA", "FORMACIÓN ACADÉMICA", "ACADEMIC TRAINING", "AUSBILDUNG")
	translations["projectsTitle"] = T("PROJECTES PERSONALS", "PROYECTOS PERSONALES", "PERSONAL PROJECTS", "PERSÖNLICHE PROJEKTE")
	translations["interval"] = T("Interval", "Intervalo", "Interval", "Intervall")
	translations["location"] = T("Localitat", "Localidad", "Location", "Ortschaft")
	translations["description"] = T("Descripció del projecte", "Descripción del proyecto", "Project description", "Beschreibung des Projekts")
	translations["tasks"] = T("Tasques realitzades", "Tareas realizadas", "Tasks performed", "Ausgeführte Aufgaben")
	translations["skills"] = T("Eines i coneixements", "Herramientas y conocimientos", "Skills and tools", "Fähigkeiten und Werkzeuge")
	return translations

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
