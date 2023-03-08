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
	#express = Skill("EXPRESS")
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
	repair = Skill(
		"repair",
		T("Diagnòstic i reparació d'avaries", "Diagnóstico y reparación de averías", "Diagnosis and repair of faults", "Diagnose und Behebung von Störungen")
	)
	php = Skill("PHP")
	mysql = Skill("MySQL")
	youtubeApi = Skill("youtube-api", T("API de YouTube", "API de YouTube", "YouTube API", "YouTube-API"))
	codeigniter = Skill("CodeIgniter")
	grocerycrud = Skill("GroceryCRUD")
	bootstrap = Skill("Bootstrap")
	vuejs = Skill("VueJS")
	drupal = Skill("Drupal")
	remoteaccess = Skill("remote-access", T("Accés remot", "Acceso remoto", "remote access", "Fernzugriff"))
	dns = Skill("DNS")
	python = Skill("Python")
	plone = Skill("Plone CMS")
	googlemaps = Skill("Google Maps API")
	xml = Skill("XML")
	wordpress = Skill("WordPress")
	cron = Skill("Cron")
	pdf = Skill("PDF")
	kml = Skill("KML")
	snorby = Skill("Snorby")
	networkmonitoring = Skill("network-monitoring", T("supervisió de la xarxa", "supervisión de la red", "network monitoring", "Netzwerküberwachung"))
	computermaint = Skill("computer-maintenance", T("Manteniment d'ordenadors", "Mantenimiento de ordenadores", "Computer maintenance", "Computerwartung"))
	access = Skill("Access")
	analog = Skill("analog-electronics", T("Electrònica analògica", "Electrónica analógica", "Analog electronics", "Analoge Elektronik"))
	digital = Skill("digital-electronics", T("Electrònica digital", "Electrónica digital", "Digital electronics", "Digitale Elektronik"))
	component = Skill("component-selection", T("selecció de components", "selección de componentes", "component selection", "Komponentenauswahl"))
	pcb = Skill("pcb", T("disseny de circuits impresos", "diseño de circuitos impresos", "printed circuit design", "Leiterplattenentwurf"))
	proteus = Skill("Proteus")
	firmware = Skill("Firmware")
	tcpIp = Skill("TCP/IP")
	http = Skill("HTTP")
	design = Skill("design", T("Disseny", "Diseño", "Design", "Design"))
	apache = Skill("Apache")
	npm = Skill("NPM"),
	algorithms = Skill("algorithms", T("Algorismes", "Algoritmos", "Algorithms", "Algorithmen"))
	foto = Skill("foto", T("fotografia", "fotografía", "photography", "Fotografie"))
	simu = Skill("simulations", T("simulacions", "simulaciones", "simulations", "Simulationen"))
	compNum = Skill("complex", T("Nombres complexos", "Números complejos", "Complex numbers", "Komplexe Zahlen"))
	mandel = Skill("Mandelbrot")
	julia = Skill("julia-set", T("Conjunt Julia", "Conjunto Julia", "Julia Set", "Julia Set"))
	video = Skill("video", T("Edició de vídeos", "Edición de vídeos", "Video editing", "Videobearbeitung"))
	softwarePlan = Skill("software-planning", T("Planificació de software", "Planificación de software", "Software planning", "Softwareplanung"))
	database = Skill("database", T("Bases de dades", "Bases de datos", "Databases", "Datenbanken"))
	arduino = Skill("Arduino")
	raspberry = Skill("Raspberry Pi")
	protocols = Skill("protocols", T("Protocols de comunicació", "Protocolos de comunicación", "Protocols of communication", "Kommunikationsprotokolle"))
	design3d = Skill("3d-design", T("disseny 3D", "diseño 3D", "3D design", "3D-Design"))
	gsm = Skill("GSM/GPRS")
	mongodb = Skill("MongoDB")
	ssh = Skill("SSH")
	batteries = Skill("batteries", T("Bateries", "Baterías", "Batteries", "Batterien"))
	field = Skill("field-work", T("Treball de camp", "Trabajo de campo", "Field work", "Feldarbeit"))
	feedback = Skill("feedback", T("Bucle de realimentació", "Bucle de retroalimentación", "Feedback loop", "Rückkopplungsschleife"))
	translation = Skill("translation", T("Traducció", "Traducción", "Translation", "Übersetzung"))



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
	headerData = HeaderData(headers, [doctors, tractor])

	dsPlace = T("Tècnic Servei d'assistència tècnica", "Técnico Servicio de asistencia técnica", "Help Desk Technician", "Help Desk Techniker")
	dsWeb = Project(
		T("Revisió i migració web", "Revisión y migración web" , "Web review and migration", "Web-Überprüfung und -Migration"),
		None,
		T(
			"La meva funció era la de revisar la migració de la botiga en línia des d'una plataforma obsoleta a una nova plataforma. També revisar continguts del blog i informes de SEO.",
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
			"Resoldre els dubtes i les incidències que es poden trobar els clients amb els productes de l'empresa. Donar consells i indicacions a companys/es de l'empresa. Diagnosticar avaries i reparar equips. Implementar millores.",
			"Resolver las dudas y las incidencias que pueden encontrarse los clientes con los productos de la empresa. Dar consejos e indicaciones a compañeros/as de la empresa. Diagnosticar averías y reparar equipos. Implementar mejoras.",
			"Resolve doubts and incidents that customers may encounter with the company's products. Give advice and instructions to company colleagues. Diagnose faults and repair equipment. Implement improvements.",
			"Beheben von Zweifel und Vorfälle, die Kunden mit den Produkten des Unternehmens begegnen können. Kollegen im Unternehmen Ratschläge und Anweisungen Geben. Fehler diagnostizieren und Geräte reparieren. Verbesserungen implementieren."
		),
		SkillSet([customer, incident, logistic, diplomacy, document, team, warranty, en, de, linux, solar, wind, optim])
	)
	damiaSolar = Job(dsPlace, "Damia Solar", "2020/08", "2022/07", "La Pobla de Segur", [dsWeb, dsTesting, dsSAT])

	iCore9 = Project(
		"iCore9",
		T(
			"iCore9 es un paquet de llibreries de gestió i procés de dades BIM desenvolupat conjuntament amb Apogea consulting.",
			"iCore9 es un paquete de librerías de gestión y proceso de datos BIM desarrollado conjuntamente con Apogea consulting.",
			"iCore9 is a package of BIM data management and process libraries developed together with Apogea consulting.",
			"iCore9 ist ein Paket aus BIM-Datenmanagement und Prozessbibliotheken, das zusammen mit Apogea Consulting entwickelt wurde."
		),
		T(
			"Implementació d'un parser d'arxius IFC (similar a step), un parser d'arxius EXPRESS, una llibreria de geometria 3D, un tessel·lador, un processador/optimitzador geomètric, un visor 3D web, funcions de desat i exportació, un sistema de llicencies. Documentació de funcionalitats.",
			"Implementación de un parser de archivos IFC (similar a step), un parser de archivos EXPRESS, una librería de geometría 3D, un teselador, un procesador/optimizador geométrico, un visor 3D web, funciones de guardado y exportación, un sistema de licencias. Documentación de funcionalidades.",
			"Implementation of an IFC (similar to step) file parser, an EXPRESS file parser, a 3D geometry library, a tessellator, a geometric processor/optimizer, a 3D web viewer, save and export functions, a licensing system. Functionality documentation.",
			"Implementierung eines IFC-Dateiparsers (ähnlich zu step), eines EXPRESS-Dateiparser, einer 3D-Geometriebibliothek, eines Tessellators, eines geometrischen Prozessors/Optimierers, eines 3D-Web-Viewers, Speicher- und Exportfunktionen, eines Lizenzsystems. Dokumentation der Funktionalität."
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
			"Disseny i implementació del backend de la plataforma, la base de dades, els sistemes de seguretat, el xifrat de les dades d'usuari, un parser d'expressions matemàtiques, calculadora de costos. Implementació del frontend.",
			"Diseño e implementación del backend de la plataforma, base de datos, sistemas de seguridad, cifrado de los datos de usuario, un parser de expresiones matemáticas, calculadora de costes. Implementación del frontendo.",
			"Design and implementation of the platform backend, database, security systems, user data encryption, a mathematical expression parser, cost calculator. Implementation of the frontend.",
			"Design und Implementierung des Plattform-Backends, der Datenbank, der Sicherheitssysteme, der Benutzerdatenverschlüsselung, ein mathematischer Ausdrucksparser, des Kostenrechners. Implementierung des Frontends."
		),
		SkillSet([distributed, oop, cs, antlr, grammar, syntax, visualstudio, git, jenkins, sonarQube, ci, cd, sqlServer, entityFrCore, security, crypto, api, graphql, html, angular, ts, css, team, responsive, en])
	)

	oda = Project(
		"Open Design Alliance",
		T(
			"La llibreria de l'open design alliance, es coneguda per ser farragosa i complicada de fer servir. L'objectiu era d'aportar un conjunt de funcionalitats per facilitar la implantació de la llibreria.",
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
			"La api BIM-360 d'Autodesk ofereix una plataforma de gestió de documents relacionats amb l'arquitectura.",
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
			T("Reparació de dispositius electrònics", "Reparación de dispositivos electrónicos", "Repair of electronic devices", "Reparatur von elektronischen Geräten"),
			None,
			T(
				"Diagnosticar i reparar tota mena de components electrònics, des de radiadors elèctrics fins a centraletes de maquines industrials.",
				"Diagnosticar y reparar todo tipo de componentes electrónicos, desde radiadores eléctricos hasta centralitas de máquinas industriales.",
				"Diagnose and repair all kinds of electronic components, from electric radiators to industrial machine control units.",
				"Diagnose und reparatur alle Arten von elektronischen Komponenten, von elektrischen Heizkörpern bis hin zu Steuereinheiten für industrielle Maschinen."
			),
			SkillSet([repair])
		),
		Project(
			T("Trasllat de botiga", "Traslado de tienda", "Store move", "Betriebsumzug"),
			T(
				"A més a més del taller de reparació el nou local havia de comptar amb una botiga.",
				"Además del taller de reparación, el nuevo local debía contar con una tienda.",
				"In addition to the repair workshop, the new premises had to have a shop.",
				"Zusätzlich zur Reparaturwerkstatt sollte in den neuen Räumlichkeiten auch ein Laden vorhanden sein."
			),
			T(
				"Preparació de la botiga. Trasllat del mobiliari i les eines del taller.",
				"Preparación de la tienda. Traslado del mobiliario y herramientas del taller.",
				"Store preparation. Transfer of workshop furniture and tools.",
				"Shop-Vorbereitung. Transport von Möbeln und Werkzeug."
			),
			None
		)
	]
	becari = T("Becari", "Becario", "Intern", "Praktikant")
	becariAlcoletge = Job(
		becari,
		T("Taller de electrònica", "Taller de electrónica", "Electronics workshop", "Elektronik Werkstatt"),
		"2018/02", "2018/06", "Alcoletge", alcoletgeProjects
	)

	webDeveloper = T("Desenvolupador web", "Desarrollador web", "Web developer", "Web-Entwickler")

	tuteorica = Project(
		"Tuteorica",
		T(
			"Tuteorica es una plataforma en línia de curs teòric de permisos de conduir.",
			"Tuteorica es una plataforma online de curso teórico de permisos de conducir.",
			"Tuteorica is an online platform for theoretical driving license courses.",
			"Tuteorica ist eine Online-Plattform für theoretische Führerscheinkurse."
		),
		T(
			"Realitzar un informe de l'estat de la plataforma. Aportar propostes de millora.",
			"Realizar un informe del estado de la plataforma. Aportar propuestas de mejora.",
			"Create a platform status report. Provide improvement proposals.",
			"Erstellen Sie einen Plattformstatusbericht. Verbesserungsvorschläge einbringen."
		),
		SkillSet([html, css, php, mysql, js, youtubeApi, linux, optim])
	)

	webamida = T(
		"Crear la pagina web des de zero, completament a mida de les seves necessitats.",
		"Crear la pagina web desde cero, completamente a medida de sus necesidades.",
		"Create the website from scratch, completely tailored to his needs.",
		"Erstellung der Website von Grund auf neu, vollständig an seine Bedürfnisse angepasst."
	)

	emilio = Project(
		"Emilio Ferrer Fotos",
		T(
			"Emilio Ferrer es un reconegut fotògraf amb la necessitat d'exposar les seves obres a través d'una pàgina web.",
			"Emilio Ferrer es un reconocido fotógrafo con la necesidad de exponer sus obras a través de una página web.",
			"Emilio Ferrer is a renowned photographer with the need to exhibit his works through a website.",
			"Emilio Ferrer ist ein renommierter Fotograf, der seine Werke über eine Website ausstellen möchte."
		),
		webamida,
		SkillSet([html, css, php, mysql, js, codeigniter, grocerycrud, linux, bootstrap, responsive, en]),
		"https://www.emilioferrerfotos.com/ca/"
	)

	josepBP = Project(
		"Josep Ball i Papiol",
		T(
			"Josep Ball i Papiol es un reconegut psicòleg amb la necessitat d'anunciar els seus serveis a través d'una pàgina web.",
			"Josep Ball i Papiol es un reconocido psicólogo con la necesidad de anunciar sus servicios a través de una página web.",
			"Josep Ball i Papiol is a renowned psychologist with the need to advertise his services through a website.",
			"Josep Ball i Papiol ist ein renommierter Psychologe, der seine Dienste über eine Website bewerben möchte."
		),
		webamida,
		SkillSet([html, css, js, vuejs, php, mysql, linux, bootstrap, responsive])
	)

	otherWebsites = T("Altres webs", "Otras webs", "Other websites", "Andere Webseiten")

	gIother = Project(otherWebsites, None, webamida, SkillSet([html, css, php, mysql, js, codeigniter, grocerycrud, linux, bootstrap, responsive, en]))

	grupindex = Job(webDeveloper, "grupIndex", "2017/02", "2018/02", "Balaguer", [tuteorica, emilio, josepBP, gIother])

	inaem = Project(
		"Inaem",
		T(
			"L'Inaem es un catàleg en línia de cultura que ofereix una API per a accedir a les dades del catàleg.",
			"Inaem es un catálogo online de cultura que ofrece una API para acceder a los datos del catálogo.",
			"Inaem is an online culture catalog that offers an API to access catalog data.",
			"Inaem ist ein Online-Kulturkatalog, der eine API für den Zugriff auf Katalogdaten bietet."
		),
		T(
			"Implementar un client de la API.",
			"Implementar un cliente de la API.",
			"Implement an API client.",
			"Implementieren eines API-Client."
		),
		SkillSet([html, js, api, css])
	)

	tmi = Project(
		"TMIPal",
		T(
			"TMI es una empresa que fabrica maquinaria per al paletitzat de mercaderies.",
			"TMI es una empresa que fabrica maquinaria para el paletizado de mercancías.",
			"TMI is a company that manufactures machinery for the palletizing of goods.",
			"TMI ist ein Unternehmen, das Maschinen zum Palettieren von Waren herstellt."
		),
		T(
			"Realitzar tasques de manteniment de la web. Resoldre incidència en la xarxa del client.",
			"Realizar labores de mantenimiento de la web. Resolver incidencia en la red del cliente.",
			"Perform website maintenance tasks. Resolve incidents in the client's network.",
			"Durchführen von Webwartungsaufgaben. Störungsbeseitigung im Netzwerk des Kunden."
		),
		SkillSet([html, css, js, php, mysql, drupal, remoteaccess, dns])
	)

	semicOther = Project(
		otherWebsites, 
		T(
			"A SEMIC un gran volum dels clients son les administracions publiques com ajuntaments.",
			"En SEMIC un gran volumen de clientes son las administraciones públicas como ayuntamientos.",
			"At SEMIC, a large volume of customers are public administrations such as town councils.",
			"Ein großer Teil der Kunden von SEMIC sind öffentliche Verwaltungen wie Stadtverwaltungen."
		),
		T(
			"Realitzar tasques de manteniment de les pagines web fetes amb plone o drupal.",
			"Realizar tareas de mantenimiento de las paginas web hechas con plone o drupal.",
			"Carry out maintenance tasks for web pages made with plone or drupal.",
			"Durchführen von Webwartungsaufgaben für Webseiten, die mit Plone oder Drupal erstellt wurden."
		),
		SkillSet([html, css, js, python, plone, drupal, linux])
	)

	semic = Job(webDeveloper, "SEMIC", "2015/09", "2016/06", "Lleida", [inaem, tmi, semicOther])

	okhabitat = Project(
		"OkHabitat",
		T(
			"OkHabitat era una plataforma immobiliaria pensada per a anunciar immobles d'agents immobiliaris i de bancs.",
			"OkHabitat era una plataforma inmobiliaria pensada para anunciar inmuebles de agentes inmobiliarios y bancos.",
			"OkHabitat was a real estate platform designed to advertise properties from real estate agents and banks.",
			"OkHabitat war eine Immobilienplattform, die entwickelt wurde, um Immobilien von Immobilienmaklern und Banken zu bewerben."
		),
		T(
			"Realitzar tasques de manteniment i d'ampliació de la plataforma. Optimitzar consultes a la base de dades.",
			"Realizar tareas de mantenimiento y ampliación de la plataforma. Optimizar consultas en la base de datos.",
			"Carry out maintenance and expansion tasks of the platform. Optimize database queries.",
			"Wartungs- und Erweiterungsaufgaben der Plattform durchführen. Datenbankabfragen optimieren."
		),
		SkillSet([html, css, php, mysql, optim, team, bootstrap, responsive]),
		"https://web.archive.org/web/20150221231551/http://okhabitat.com:80/"
	)

	eixcomercial = Project(
		"Eix comercial Lleida",
		T(
			"L'Eix comercial es una associació de negocis de Lleida. El projecte consistia en crear una plataforma en línia per donar visibilitat als negocis en qüestió.",
			"Eix comercial es una asociación de negocios de Lleida. El proyecto consistía en crear una plataforma online para dar visibilidad a los negocios en cuestión.",
			"Eix comercial is a business association from Lleida. The project consisted of creating an online platform to give visibility to the businesses in question.",
			"Eix comercial ist ein Unternehmensverband aus Lleida. Das Projekt bestand darin, eine Online-Plattform zu schaffen, um die betreffenden Unternehmen sichtbar zu machen."
		),
		webamida,
		SkillSet([html, css, php, mysql, js, codeigniter, grocerycrud, googlemaps, bootstrap, responsive]),
		"https://web.archive.org/web/20150815021539/http://www.eixcomerciallleida.com/ca"
	)

	jqueralt = Project(
		"JQueralt",
		T(
			"JQueralt es una immobiliària de Lleida que precisava d'una pagina web.",
			"JQueralt es una inmobiliaria de Lleida que precisaba de una pagina web.",
			"JQueralt is a real estate company in Lleida that needed a website.",
			"JQueralt ist ein Immobilienunternehmen in Lleida, das eine Website brauchte."
		),
		webamida,
		SkillSet([html, css, php, mysql, js, codeigniter, grocerycrud, api, xml, bootstrap, responsive, optim]),
		"https://web.archive.org/web/20160112013443/http://www.jqueralt.com/"
	)

	oceanAlmond = Project(
		"OceanAlmond",
		T(
			"OceanAlmond es una empresa agrònoma especialitzada en el cultiu d'ametlles que precisava d'una pagina web.",
			"OceanAlmond es una empresa agrónoma especializada en el cultivo de almendras que precisaba de una pagina web.",
			"OceanAlmond is an agricultural company specialized in the cultivation of almonds that needed a website.",
			"OceanAlmond ist ein landwirtschaftliches Unternehmen, das sich auf den Anbau von Mandeln spezialisiert hat und eine Website benötigte."
		),
		webamida,
		SkillSet([html,css, php, mysql, js, codeigniter, grocerycrud, googlemaps, bootstrap, responsive])
	)

	lagraficaOthr = Project(otherWebsites,None,webamida,SkillSet([html,css,php,mysql,js,codeigniter,grocerycrud,bootstrap,responsive,wordpress,en,video]))

	lagrafica = Job(webDeveloper, "LaGrafica", "2014/06", "2015/07", "Lleida", [okhabitat, eixcomercial, jqueralt, oceanAlmond, lagraficaOthr])

	timebank = Project(
		T("Banc del temps", "Banco del tiempo", "Time bank", "Zeitbank"),
		T(
			"Un banc del temps es una forma de intercambiar feines entre els membres d'una comunitat sense que s'hi involucrin els diners. En canvi es comptabilitzen hores.",
			"Un banco del tiempo es una forma de intercambiar trabajos entre los miembros de una comunidad sin que se involucre el dinero. En cambio, se contabilizan horas.",
			"A time bank is a way of exchanging jobs between members of a community without money being involved. Instead, hours are counted.",
			"Eine Zeitbank ist eine Möglichkeit, Jobs zwischen Mitgliedern einer Gemeinschaft auszutauschen, ohne dass Geld im Spiel ist. Stattdessen werden Stunden gezählt."
		),
		T(
			"Implementació d'una eina de gestió del membres i les hores  aportades per cadascun.",
			"Implementación de una herramienta de gestión de los miembros y las horas aportadas por cada uno.",
			"Implementation of a member management tool and the hours contributed by each.",
			"Implementierung eines Mitgliederverwaltungstools und der von jedem geleisteten Stunden."
		),
		SkillSet([html, php, mysql, codeigniter, grocerycrud])
	)

	camimages = Project(
		T("Ordenació imatges càmeres", "Ordenación imágenes cámaras", "Sorting camera images", "Sortieren von Kamerabildern"),
		T(
			"En compliment de la LOPD, les imatges gravades per les càmeres de vigilància s'han d'eliminar passat un període de temps determinat.",
			"En cumplimiento de la LOPD, las imágenes grabadas por las cámaras de vigilancia deben eliminarse pasado un período de tiempo determinado.",
			"In compliance with the LOPD, the images recorded by the surveillance cameras must be deleted after a certain period of time.",
			"Gemäß LOPD müssen die von den Überwachungskameras aufgenommenen Bilder nach einer bestimmten Zeit gelöscht werden."
		),
		T(
			"Implementar un script que s'executi de forma regular, que crei un directori per cada dia i que mogui les imatges al seu directori corresponent.",
			"Implementar un script que se ejecute de forma regular, que cree un directorio por cada día y que mueva las imágenes en su directorio correspondiente.",
			"Implement a script that runs regularly, creates a directory for each day and moves the images to their corresponding directory.",
			"Implementierung eines regelmäßig ausgeführten Skripts, das für jeden Tag ein Verzeichnis erstellt und die Bilder in das entsprechende Verzeichnis verschiebt."
		),
		SkillSet([linux, bash, cron, php])
	)

	smssending = Project(
		T("Enviament d'SMS", "Envío de SMS", "Sending SMS", "SMS senden"),
		T(
			"El poliesportiu de la ciutat demana que se li faci arribar als membres subscrits informació de forma diària per SMS.",
			"El polideportivo de la ciudad pide que se le haga llegar a los miembros suscritos información de forma diaria por SMS.",
			"The city's sports center requests that subscribed members receive information on a daily basis by SMS.",
			"Das Sportzentrum der Stadt fordert, dass abonnierte Mitglieder täglich Informationen per SMS erhalten."
		),
		T(
			"Implementar un script que obtingui la informació en qüestió i l'envii als destinataris subscrits.",
			"Implementar un script que obtenga la información en cuestión y lo envíe a los destinatarios suscritos.",
			"Implement a script that obtains the information in question and sends it to the subscribed recipients.",
			"Implementierung eines Skripts, das die betreffenden Informationen erhält und an die abonnierten Empfänger sendet."
		),
		SkillSet([linux, bash, cron])
	)

	hiking = Project(
		T("Generació de fitxes de rutes", "Generación de fichas de rutas", "Generation of route files", "Generierung von Routendateien"),
		T(
			"L'oficina de turisme precisava un conjunt de fitxes descriptives per a varies rutes d'excursionisme.",
			"La oficina de turismo precisaba de un conjunto de fichas descriptivas para varias rutas de excursionismo.",
			"The tourism office required a set of descriptive cards for various hiking routes.",
			"Das Tourismusbüro verlangte einen Satz beschreibender Karten für verschiedene Wanderrouten."
		),
		T(
			"Implementar un script que obtingui les dades d'una API i generi els arxius PDF.",
			"Implementar un script que obtenga los datos de una API y genere los archivos PDF.",
			"Implement a script that obtains the data from an API and generates the PDF files.",
			"Implementierung eines Skripts, das die Daten von einer API bezieht und die PDF-Dateien generiert."
		),
		SkillSet([php, pdf, kml, api, xml])
	)

	ids = Project(
		"IDS",
		T(
			"Per tal de garantir la seguretat i el bon funcionament de la xarxa de l'ajuntament es va implantar un sistema de detecció d'intrusions.",
			"Para garantizar la seguridad y buen funcionamiento de la red del ayuntamiento se implantó un sistema de detección de intrusiones.",
			"In order to guarantee the security and proper functioning of the council's network, an intrusion detection system was implemented.",
			"Um die Sicherheit und das ordnungsgemäße Funktionieren des Gemeindenetzwerks zu gewährleisten, wurde ein Intrusion Detection System implementiert."
		),
		T(
			"Instalar i conectar un servidor dedicat, instal·lació del sistema operatiu i del programari necessari. Detectar vulnerabilitats en els equips de la xarxa i resoldre-les.",
			"Instalar y conectar un servidor dedicado, instalación del sistema operativo y del software necesario. Detectar vulnerabilidades en los equipos de la red y resolverlas.",
			"Install and connect a dedicated server, installation of the operating system and the necessary software. Detect vulnerabilities in network equipment and resolve them.",
			"Installation und Anschluss eines dedizierten Servers, Installation des Betriebssystems und der notwendigen Software. Erkennung von Schwachstellen in Netzwerkgeräten und deren Behebung."
		),
		SkillSet([snorby, linux, security, networkmonitoring, incident, computermaint])
	)

	ajLaseu = Job(
		becari,
		T("Ajuntament de La Seu d'Urgell", "Ayuntamiento de La Seu d'Urgell", "City Council of La Seu d'Urgell", "Rathaus von La Seu d'Urgell"),
		"2012", "2013", "La Seu d'Urgell", [timebank, camimages, smssending, hiking, ids]
	)

	telecentrePallars = Job(
		becari,
		T("Telecentre del Pallars Sobirà", "Telecentro del Pallars Sobirà", "Pallars Sobirà telecentre", "Telezentrum Pallars Sobirà"),
		"2009", "2010", "Sort",
		None,
		SkillSet([html, css, drupal, access, computermaint])
	)

	jobs = [damiaSolar, handle, becariAlcoletge, grupindex, semic, lagrafica, ajLaseu, telecentrePallars]

	udl = Training(
		T(
			"Grau en Enginyeria Electrònica Industrial i Automàtica",
			"Grado en Ingeniería Electrónica Industrial y Automática",
			"Degree in Industrial and Automatic Electronic Engineering",
			"Studium der Industrie- und Automatisierungstechnik"
		),
		"2015",
		T("(en curs)", "(en curso)", "(in progress)", "(im Gange)"),
		T(
			"Escola Politècnica Superior – Universitat de Lleida",
			"Escuela Politécnica Superior - Universidad de Lleida",
			"Higher Polytechnic School – University of Lleida",
			"Höhere Polytechnische Schule – Universität Lleida"
		),
		"Lleida"
	)

	pick2light = Project(
		T(
			"Disseny i desenvolupament prototip – Pick to light",
			"Diseño y desarrollo prototipo – Pick to light",
			"Prototype design and development – Pick to light",
			"Prototypendesign und -entwicklung – Pick to light"
		),
		None,
		T(
			"Disseny i construcció d'un guia visual per a empleats de magatzem d'una empresa de logística amb connexió a la xarxa de l'empresa.",
			"Diseño y construcción de un guía visual para empleados de almacén de una empresa de logística con conexión a la red de la empresa.",
			"Design and construction of a visual guide for warehouse employees of a logistics company connected to the company's network.",
			"Design und Aufbau eines visuellen Leitfadens für Lagermitarbeiter eines Logistikunternehmens, das an das Netzwerk des Unternehmens angeschlossen ist."
		),
		SkillSet([analog, digital, component, schema, pcb, proteus, firmware, cpp, tcpIp, http, html, css, team]),
		None, "2014", "2015"
	)

	sensors = Skill("sensors", T("Sensors", "Sensores", "Sensors", "Sensoren"))
	robolot = Event(
		T(
			"Concursant – Competició de robots rastrejadors – Robolot",
			"Concursante – Competición de robots rastreadores – Robolot",
			"Contestant – Crawler Robot Competition – Robolot",
			"Kandidat – Crawler-Roboter-Wettbewerb – Robolot"
		),
		T(
			"Els concursants havíem de presentar un robot que fos capaç de seguir una línia pintada al ring.",
			"Los concursantes debíamos presentar un robot que fuera capaz de seguir una línea pintada en el ring.",
			"We contestants had to present a robot that was able to follow a line painted in the ring.",
			"Wir Teilnehmer mussten einen Roboter präsentieren, der einer in den Ring gemalten Linie folgen konnte."
		),
		SkillSet([analog, digital, component, schema, pcb, proteus, firmware, cpp, sensors, team, batteries]),
		None, "2014/04/26", "Olot"
	)

	caparrella = Training(
		T(
			"CFGS – Manteniment Electrònic",
			"CFGS – Mantenimiento Electrónico",
			"Higher Level Training Curse – Electronic Maintenance",
			"Fachabitur – Elektronische Wartung"
		),
		"2013", "2015", "IES la Caparrella", "Lleida", [pick2light, robolot]
	)

	aversicuela = Event(
		T(
			"Concursant – Jornada de petits i joves emprenedors",
			"Concursante – Jornada de pequeños y jóvenes emprendedores",
			"Contestant – Day of small and young entrepreneurs",
			"Kandidat – Tag der Klein- und Jungunternehmer"
		),
		T(
			"L'objectiu de la jornada era el de donar una oportunitat als alumnes de diferents instituts de presentar els seus respectius projectes emprenedors.",
			"El objetivo de la jornada era dar una oportunidad a los alumnos de diferentes institutos de presentar sus respectivos proyectos emprendedores.",
			"The aim of the day was to give students from different institutes an opportunity to present their respective entrepreneurial projects.",
			"Ziel des Tages war es, Studierenden verschiedener Institute die Möglichkeit zu geben, ihre jeweiligen unternehmerischen Projekte vorzustellen."
		),
		SkillSet([php, html, css, mysql, security, design, team]),
		None, "2012/05/17", "La Seu d'Urgell",
		Header(
			T("Projecte presentat", "Proyecto presentado", "Project presented", "Vorgestelltes Projekt"),
			T(
				"A ver si cuela (aversicuela.com) es el projecte que varem presentar en el nostre equip. Es tracta d'una plataforma social en línia per compartir contingut d'humor. La plataforma va estar en producció, funcionant i amb usuaris reals entre el 2012/04/01 i el 2013/02/21.",
				"A ver si cuela (aversicuela.com) es el proyecto que presentamos en nuestro equipo. Se trata de una plataforma social online para compartir contenido de humor. La plataforma estuvo en producción, funcionando y con usuarios reales entre el 2012/04/01 y el 2013/02/21.",
				"A ver si cuela (aversicuela.com) is the project that we presented in our team. It is an online social platform for sharing humorous content. The platform was in production, working and with real users between 2012/04/01 and 2013/02/21.",
				"A ver si cuela (aversicuela.com) ist das Projekt, das wir in unserem Team vorgestellt haben. Es ist eine soziale Online-Plattform zum Teilen von humorvollen Inhalten. Die Plattform war zwischen dem 2012/04/01 und dem 2013/02/21 in Betrieb und mit echten Benutzern."
			)
		)
	)

	programameName = T(
		"Concursant – Competició de programació – ProgramaMe",
		"Concursante – Competición de programación – ProgramaMe",
		"Contestant – Programming competition – ProgramaMe",
		"Teilnehmer – Programmierwettbewerb – ProgramaMe"
	)
	programameDesc = T(
		"Els concursants havien de resoldre problemes matemàtics amb l'ajuda de lògica i codi.",
		"Los concursantes debían resolver problemas matemáticos con ayuda de lógica y código.",
		"Contestants had to solve math problems with the help of logic and code.",
		"Die Teilnehmer mussten mathematische Probleme mit Hilfe von Logik und Code lösen."
	)

	programame3 = Event(programameName, programameDesc, SkillSet([cpp, team]), None, "2013/03/14", "IES Baix Camp, Reus")
	programame2 = Event(programameName, programameDesc, SkillSet([cpp, team]), None, "2012/06/05", "IES Antonio de Nebrija, Móstoles")
	programame1 = Event(
		programameName, programameDesc, SkillSet([cpp, team]), None, "2012/03/27", "IES Baix Camp, Reus",
		T("Varem obtenir el 2n premi.", "Obtuvimos el 2º premio.", "We won the 2nd prize.", "Wir hatten den 2en Preis gewonnen.")
	)

	# TODO: Add linux classroom
	# name, description, tasks, skills, url = None, startDate = None, endDate = None
	linuxClassroom = Project(
		T("Aula Linux", "Aula Linux", "Linux classroom", "Linux-Klassenzimmer"),
		T(
			"Implementació d'una aula d'informatica de baix cost que aprofiti el maquinari antic o de gama baixa i un o varis servidors que asumeixin la carrega de treball.",
			"Implementación de un aula de informática de bajo coste que aproveche el hardware antiguo o de gama baja y uno o varios servidores que asuman la carga de trabajo.",
			"Implementation of a low-cost IT classroom that takes advantage of old or low-end hardware and one or more servers that take on the workload.",
			"Implementierung eines kostengünstigen IT-Klassenzimmers, das alte oder Low-End-Hardware und einen oder mehrere Server nutzt, die die Arbeitslast übernehmen."
		),
		T(
			"Dissenyar la topologia de la xarxa. Cercar solucions de software disponibles. Instal·lar i configurar Linux Terminal Server Project. Cercar ordinadors de baix cost que facin de client.",
			"Diseñar la topología de la red. Buscar soluciones de software disponibles. Instalar y configurar Linux Terminal Server Project. Buscar ordenadores de bajo coste que hagan de cliente.",
			"Design the topology of the network. Search for available software solutions. Install and configure Linux Terminal Server Project. Look for low-cost computers that act as clients.",
			"Entwurf der Netzwerktopologie. Suche von verfügbaren Software-Lösungen. Installation und Konfiguration des Linux Terminal Server Project. Suche von kostengünstigen Computern, um als Client zu fungieren."
		),
		SkillSet([linux, apache, php, mysql, codeigniter, team, component]),
		startDate = "2013"
	)

	joanBrudieu = Training(
		T(
			"CFGS – Administració de Sistemes Informàtics en Xarxa",
			"CFGS – Administración de Sistemas Informáticos en Red",
			"Higher Level Training Curse – Computer Network Systems Administration",
			"Fachabitur – Verwaltung von Netzwerkcomputersystemen"
		),
		"2011", "2013", "IES Joan Brudieu", "La Seu d'Urgell", [programame3, linuxClassroom, programame2, aversicuela, programame1]
	)

	catskills = Event(
		T(
			"Concursant – Competició de disseny de pagines web – CatSkills",
			"Concursante – Competición de diseño de paginas web – CatSkills",
			"Contestant – Web page design competition – CatSkills",
			"Kandidat – Webseiten-Designwettbewerb – CatSkills"
		),
		T(
			"Els concursants havien de crear un lloc web d'una empresa immobiliària.",
			"Los concursantes debían crear un sitio web de una empresa inmobiliaria.",
			"Contestants had to create a website for a real estate company.",
			"Die Teilnehmer mussten eine Website für ein Immobilienunternehmen erstellen."
		),
		SkillSet([html, css, php, mysql]), None, "2009/01/28", "IES Esteve Terradas i Illa, Cornellà de Llobregat"
	)

	hugRoger = Training(
		T(
			"CFGM – Explotació de Sistemes Informàtics",
			"CFGM – Explotación de Sistemas Informáticos",
			"Intermediate Level Training Curse – Use of Computer Systems",
			"Fachabitur – Nutzung von Computersystemen"
		),
		"2007", "2009", "IES Hug Roger III", "Sort", [catskills]
	)

	eso = Training(
		T("Educació Secundària Obligatòria", "Educación Secundaria Obligatoria", "High school", "Weiterführende Schule"),
		"2003", "2007", "IES de Tremp", "Tremp", []
	)

	trainings = [udl, caparrella, joanBrudieu, hugRoger, eso]

	freelance = Project(
		T("Consultor tecnològic freelance", "Consultor tecnológico freelance", "Freelance technology consultant", "Freiberuflicher Technologieberater"),
		None,
		[
		T(
			"Implementació d'un client API REST per a pantalles informatives d'estacions d'esquí. HTML, JavaScript, JSON, jQuery, CSS.",
			"Implementación de un cliente API REST para pantallas informativas de estaciones de esquí. HTML, JavaScript, JSON, jQuery, CSS.",
			"Implementation of a REST API client for ski resort information screens. HTML, JavaScript, JSON, jQuery, CSS.",
			"Implementierung eines REST-API-Clients für Skigebiets-Informationsbildschirme. HTML, JavaScript, JSON, jQuery, CSS."
		),
		T(
			"Manteniment de instal·lació fotovoltaica aïllada. Manteniment de bateries estacionaries i inversor, energia solar.",
			"Mantenimiento de instalación fotovoltaica aislada. Mantenimiento de baterías estacionarias e inversor, energía solar.",
			"Maintenance of isolated photovoltaic installation. Maintenance of stationary batteries and inverter, solar energy.",
			"Wartung einer isolierten Photovoltaikanlage. Wartung von stationären Batterien und Wechselrichter, Solarenergie."
		),
		T(
			"Manteniment de instal·lació fotovoltaica aïllada. Substitució de regulador, inversor i proteccions, energia solar.",
			"Mantenimiento de instalación fotovoltaica aislada. Sustitución de regulador, inversor y protecciones, energía solar.",
			"Maintenance of isolated photovoltaic installation. Replacement of regulator, inverter and protections, solar energy.",
			"Wartung einer isolierten Photovoltaikanlage. Austausch von Laderegler, Wechselrichter und Schutzvorrichtungen, Solarenergie."
		),
		T(
			"Implementació del frontend d'una botiga en línia de productes d'hostaleria a l'engròs. HTML, CSS, PHP, MYSQL, JavaScript, SOAP, XML.",
			"Implementación del frontendo de una tienda online de productos de hostelería al por mayor. HTML, CSS, PHP, MYSQL, JavaScript, SOAP, XML.",
			"Implementation of the frontend of an online store of wholesale hospitality products. HTML, CSS, PHP, MYSQL, JavaScript, SOAP, XML.",
			"Implementierung des Frontends eines Online-Shops für Großhandelsprodukte für das Gastgewerbe. HTML, CSS, PHP, MYSQL, JavaScript, SOAP, XML."
		),
		T(
			"Creació de pagina web d'una casa rural. HTML, PHP, CSS,  JavaScript, MySQL, Photoshop.",
			"Creación de pagina web de una casa rural. HTML, PHP, CSS, JavaScript, MySQL, Photoshop.",
			"Creation of a rural house website. HTML, PHP, CSS, JavaScript, MySQL, Photoshop.",
			"Erstellung einer Landhaus-Website. HTML, PHP, CSS, JavaScript, MySQL, Photoshop."
		),
		T(
			"Altres. Recomanacions tècniques varies.",
			"Otros. Recomendaciones técnicas varias.",
			"Others. Various technical recommendations.",
			"Andere. Verschiedene technische Empfehlungen."
		)
		],
		None, None, "2007", "2023"
	)

	thisresume = Project(
		T("Aquest currículum", "Este currículum", "This resume", "Dieser Lebenslauf"),
		T(
			"Com que mantenir 4 versions diferents d'aquest document em semblava un treball molt tediós he decidit generar aquest document amb codi. Les dades del meu currículum son exportades a un document markdown i posteriorment mitjançant pandoc aquest es transforma a PDF.",
			"Puesto que mantener 4 versiones distintas de este documento me parecía un trabajo muy tedioso he decidido generar este documento con código. Los datos de mi currículum son exportados a un documento markdown y posteriormente mediante pandoc éste se transforma a PDF.",
			"Since maintaining 4 different versions of this document seemed like a very tedious task I decided to generate this document with code. The data of my resume is exported to a markdown document and subsequently using pandoc it is transformed into a PDF.",
			"Da die Pflege von 4 verschiedenen Versionen dieses Dokuments eine sehr mühsame Aufgabe zu sein schien, entschied ich mich, dieses Dokument mit Code zu generieren. Die Daten meines Lebenslaufs werden in ein Markdown-Dokument exportiert und anschließend mit pandoc in ein PDF umgewandelt."
		),
		skills = SkillSet([python, git, linux, bash, es, ca, en, de, translation]),
		startDate = "2023/03/02", endDate = "2023/03/08"
	)

	multiIsochrone = Project(
		"Multi-Isochrone",
		T(
			"La funció d'aquesta eina es la de generar corbes isòcrones en escenari de múltiples destinacions recurrents.",
			"La función de esta herramienta es la de generar curvas isócronas en escenario de múltiples destinos recurrentes.",
			"The function of this tool is to generate isochronous curves in the scenario of multiple recurring destinations.",
			"Die Funktion dieses Tools besteht darin, im Szenario mehrerer wiederkehrender Ziele isochrone Kurven zu erzeugen."
		),
		None,
		SkillSet([html, css, ts, git, googlemaps, npm, algorithms, optim]),
		None, "2023/02", "2023/03"
	)

	loom = Project(
		T(
			"Creació d'un teler artesanal de 4 lliços, mida sobretaula",
			"Creación de un telar artesanal de 4 lizos, tamaño sobremesa",
			"Creation of an artisan loom of 4 looms, tabletop size",
			"Herstellung eines handwerklichen Webrahmen mit 4 schäfte"
		),
		url = "https://youtu.be/rWfuz8Ocmzg", startDate = "2022/09", endDate = "2022/11"
	)


	youtube = Project(
		T(
			"Projecte artístic – Fractals & More – disponible a YouTube",
			"Proyecto artístico – Fractals & More – disponible en YouTube",
			"Art project – Fractals & More – available on YouTube",
			"Kunstprojekt – Fractals & More – verfügbar auf YouTube"
		),
		T(
			"L'art generatiu sempre m’ha apassionat. Des de que vaig descobrir que aquest tipus d’art està a l’abast de tothom que tingui 4 nocions de programació m’he anat endinsant cada vegada més en aquest mon.",
			"El arte generativo siempre me ha apasionado. Desde que descubrí que este tipo de arte está al alcance de todo el mundo que tenga 4 nociones de programación me he ido adentrando cada vez más en este mundo.",
			"I have always been passionate about generative art. Since I discovered that this type of art is within the reach of everyone who has 4 notions of programming, I have been getting deeper and deeper into this world.",
			"Generative Kunst hat mich schon immer begeistert. Seit ich entdeckt habe, dass diese Art von Kunst für jeden erreichbar ist, der 4 Vorstellungen von Programmierung hat, bin ich immer tiefer in diese Welt eingedrungen."
		),
		None,
		SkillSet([php, python, cpp, json, git, foto, simu, compNum, mandel, julia, algebra, algorithms, optim, bash, video, en]),
		"https://www.youtube.com/channel/UCNtWQJFXRJU-9qtVpBPASxQ", "2014", "2022"
	)

	rgb = Event(
		T(
			"Membre de Jurat – Robots Great Battle RGB Zaragoza",
			"Miembro de Jurado – Robots Great Battle RGB Zaragoza",
			"Jury member – Robots Great Battle RGB Zaragoza",
			"Jurymitglied – Robots Great Battle RGB Zaragoza"
		),
		T(
			"Competició de robots de lluita RGB Zaragoza.",
			"Competición de robots de lucha RGB Zaragoza.",
			"Competition of RGB Zaragoza fighting robots.",
			"Wettbewerb der Kampfroboter RGB Zaragoza."
		),
		None, "https://rgb.codelearn.es", None, "Zaragoza",
		HeaderData(
			[
			Header(T("Primera edició", "Primera edición", "First edition", "Erstausgabe"), "2021/07/31"),
			Header(T("Segona edició","Segunda edición","Second edition","Zweite Auflage"), "2022/07/30")
			],
			[]
		)
	)

	newak = Project(
		T("Soci i desenvolupador – Newak", "Socio y desarrollador – Newak", "Partner and developer – Newak", "Partner und Entwickler – Newak"),
		T(
			"Degut al contracte de confidencialitat que vaig signar no hi han detalls.",
			"Debido al contrato de confidencialidad que firmé no hay detalles.",
			"Due to the confidentiality agreement I signed there are no details.",
			"Aufgrund der von mir unterzeichneten Vertraulichkeitsvereinbarung gibt es keine Details."
		),
		skills = SkillSet([
			python, cpp, api, git, digital, analog, pcb, component, team, softwarePlan, database, kicad, arduino, raspberry, protocols, design3d, document, tcpIp, gsm, http, html, css, mysql, mongodb, firmware, js, linux, bash, ssh, en, blender
		]),
		startDate = "2016",
		endDate = "2021"
	)

	battery = Project(
		T(
			"Disseny i desenvolupament prototip – Anàlisis de bateries",
			"Diseño y desarrollo prototipo – Análisis de baterías",
			"Prototype design and development – Battery analyses",
			"Prototypendesign und -entwicklung – Batterieanalysen"
		),
		T(
			"La funció del prototip es la de mesurar el voltatge de múltiples bateries estacionaries i mostrar els respectius voltatges en una pantalla LCD. La missió del projecte es desenvolupar una eina que pugui detectar de forma precoç anomalies en bateries individuals del banc.",
			"La función del prototipo es medir el voltaje de múltiples baterías estacionarias y mostrar los respectivos voltajes en una pantalla LCD. La misión del proyecto es desarrollar una herramienta que pueda detectar de forma precoz anomalías en baterías individuales del banco.",
			"The function of the prototype is to measure the voltage of multiple stationary batteries and display the respective voltages on an LCD screen. The mission of the project is to develop a tool that can early detect anomalies in individual batteries in the bank.",
			"Die Funktion des Prototyps besteht darin, die Spannung mehrerer stationärer Batterien zu messen und die jeweiligen Spannungen auf einem LCD-Bildschirm anzuzeigen. Die Mission des Projekts ist die Entwicklung eines Werkzeugs, das Anomalien in einzelnen Batterien in der Bank frühzeitig erkennen kann."
		),
		skills = SkillSet([analog, digital, component, schema, pcb, kicad, git, firmware, cpp, batteries, solar]),
		startDate = "2020/04",
		endDate = "2020/06"
	)

	pump = Project(
		T(
			"Disseny de firmware – Controlador de bombeig solar",
			"Diseño de firmware – Controlador de bombeo solar",
			"Firmware Design – Solar Pump Controller",
			"Firmware-Design – Solarpumpen-Controller"
		),
		T(
			"Partint d’una instal·lació de bombeig solar directe controlada per un variador de freqüència i un microcontrolador, era necessari reescriure el firmware per complert ja que la implementació del proveïdor no complia amb les expectatives del client. El projecte ha durat varis anys ja que durant la meva formació he anat adquirint nous coneixements útils per millorar el rendiment del firmware.",
			"Partiendo de una instalación de bombeo solar directo controlada por un variador de frecuencia y un microcontrolador, era necesario reescribir el firmware por completo puesto que la implementación del proveedor no cumplía con las expectativas del cliente. El proyecto ha durado varios años, ya que durante mi formación he ido adquiriendo nuevos conocimientos útiles para mejorar el rendimiento del firmware.",
			"Starting from a direct solar pumping installation controlled by a frequency inverter and a microcontroller, it was necessary to completely rewrite the firmware as the supplier's implementation did not meet the client's expectations. The project has lasted several years as during my training I have been acquiring new useful knowledge to improve the performance of the firmware.",
			"Ausgehend von einer direkten Solarpumpanlage, die von einem Frequenzumrichter und einem Mikrocontroller gesteuert wird, war es notwendig, die Firmware komplett neu zu schreiben, da die Implementierung des Lieferanten nicht den Erwartungen des Kunden entsprach. Das Projekt hat mehrere Jahre gedauert, da ich während meiner Ausbildung neues nützliches Wissen erworben habe, um die Leistung der Firmware zu verbessern."
		),
		skills = SkillSet([analog, digital, git, firmware, cpp, sensors, field, feedback, solar]),
		startDate = "2019/06",
		endDate = "2021/10"
	)

	threeDprinter = Project(
		T("Curs d'impressores 3D", "Curso de impresoras 3D", "3D printer course", "3D-Drucker Kurs"),
		T(
			"Juntament amb 2 altres professors varem impartir un curs pràctic per crear, configurar i fer servir una impressora 3D.",
			"Junto con otros 2 profesores impartimos un curso práctico para crear, configurar y utilizar una impresora 3D.",
			"Together with 2 other teachers we taught a practical course to create, configure and use a 3D printer.",
			"Zusammen mit 2 anderen Lehrern haben wir einen praktischen Kurs zum Erstellen, Konfigurieren und Verwenden eines 3D-Druckers durchgeführt."
		),
		skills = SkillSet([digital, analog, firmware, design3d, team]),
		startDate = "2015/09",
		endDate = "2015/11"
	)

	lanParty = Event(
		T("Col·laborador – Lan Party Soses", "Colaborador - Lan Party Soses", "Collaborator – Lan Party Soses", "Mitarbeiter – Lan Party Soses"),
		T(
			"Com a col·laborador de la lan party he donat una classe practica d’introducció als microcontroladors i circuits de desenvolupament Arduino i Raspberry Pi.",
			"Como colaborador de la lan party he dado una clase práctica de introducción a los microcontroladores y circuitos de desarrollo Arduino y Raspberry Pi.",
			"As a collaborator of the lan party I gave a practical introduction class to Arduino and Raspberry Pi microcontrollers and development circuits.",
			"Als Mitarbeiter der LAN-Party habe ich einen praktischen Einführungskurs zu Arduino- und Raspberry Pi-Mikrocontrollern und Entwicklungsschaltungen gegeben."
		),
		None, None, date = "2014/05/31", location = "Soses"
	)

	projects = [freelance, thisresume, multiIsochrone, loom, youtube, rgb, newak, battery, pump, threeDprinter, lanParty]

	resume = Resume(name, headerData, jobs, trainings, projects)

	return resume

def GetExtraTranslations():
	T = Translation

	translations = {}
	translations["jobsTitle"] = T("EXPERIÈNCIA PROFESSIONAL", "EXPERIENCIA PROFESIONAL", "PROFESSIONAL EXPERIENCE", "BERUFLICHE ERFAHRUNGEN")
	translations["trainTitle"] = T("FORMACIÓ ACADÈMICA", "FORMACIÓN ACADÉMICA", "ACADEMIC TRAINING", "AUSBILDUNG")
	translations["projectsTitle"] = T("PROJECTES PERSONALS", "PROYECTOS PERSONALES", "PERSONAL PROJECTS", "PERSÖNLICHE PROJEKTE")
	#translations["interval"] = T("Interval", "Intervalo", "Interval", "Intervall")
	translations["interval"] = T("Període", "Periodo", "Period", "Zeitraum")
	translations["location"] = T("Localitat", "Localidad", "Location", "Ortschaft")
	translations["description"] = T("Descripció del projecte", "Descripción del proyecto", "Project description", "Beschreibung des Projekts")
	translations["tasks"] = T("Tasques realitzades", "Tareas realizadas", "Tasks performed", "Ausgeführte Aufgaben")
	translations["skills"] = T("Eines i coneixements", "Herramientas y conocimientos", "Skills and tools", "Fähigkeiten und Werkzeuge")
	translations["link"] = T("Enllaç", "Enlace", "Link", "Verknüpfung")
	translations["school"] = T("Centre", "Centro", "School", "Schule")
	translations["date"] = T("Data", "Fecha", "Date", "Datum")
	translations["event-description"] = T("Descripció de l'esdeveniment", "Descripción del evento", "Event description", "Beschreibung der Veranstaltung")
	return translations

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
