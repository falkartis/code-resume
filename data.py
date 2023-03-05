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
	computermaint = Skill("computer-maintenance", T("Manteniment d’ordenadors", "Mantenimiento de ordenadores", "Computer maintenance", "Computerwartung"))
	access = Skill("Access")




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
			"Implementació d'un parser d'arxius IFC (similar a step), una llibreria de geometria 3D, un tessel·lador, un processador/optimitzador geomètric, un visor 3D web, funcions de desat i exportació, un sistema de llicencies. Documentació de funcionalitats.",
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
			"Disseny i implementació del backend de la plataforma, la base de dades, els sistemes de seguretat, el xifrat de les dades d'usuari, calculadora de costos. Implementació del frontend.",
			"Diseño e implementación del backend de la plataforma, base de datos, sistemas de seguridad, cifrado de los datos de usuario, calculadora de costes. Implementación del frontendo.",
			"Design and implementation of the platform backend, database, security systems, user data encryption, cost calculator. Implementation of the frontend.",
			"Design und Implementierung des Plattform-Backends, der Datenbank, der Sicherheitssysteme, der Benutzerdatenverschlüsselung, des Kostenrechners. Implementierung des Frontends."
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

	gIProjects = [tuteorica, emilio, josepBP, gIother]
	grupindex = Job(webDeveloper, "grupIndex", "2017/02", "2018/02", "Balaguer", gIProjects)

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

	semicProjects = [inaem, tmi, semicOther]
	semic = Job(webDeveloper, "SEMIC", "2015/09", "2016/06", "Lleida", semicProjects)

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

	lagraficaOther = Project(otherWebsites,None,webamida,SkillSet([html,css,php,mysql,js,codeigniter,grocerycrud,bootstrap,responsive,wordpress,en]))

	lagraficaProjects = [okhabitat, eixcomercial, jqueralt, oceanAlmond, lagraficaOther]
	lagrafica = Job(webDeveloper, "LaGrafica", "2014/06", "2015/07", "Lleida", lagraficaProjects)

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

	laseuProjects = [timebank, camimages, smssending, hiking, ids]
	ajLaseu = Job(
		becari,
		T("Ajuntament de La Seu d'Urgell", "Ayuntamiento de La Seu d'Urgell", "City Council of La Seu d'Urgell", "Rathaus von La Seu d'Urgell"),
		"2012", "2013", "La Seu d'Urgell", laseuProjects
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

	caparrella = Training(
		T(
			"CFGS – Manteniment Electrònic",
			"CFGS – Mantenimiento Electrónico",
			"Higher Level Training Curse – Electronic Maintenance",
			"Fachabitur – Elektronische Wartung"
		),
		"2013", "2015", "IES la Caparrella", "Lleida",
		[]
	)


	trainings = [udl, caparrella]
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
	translations["link"] = T("Enllaç", "Enlace", "Link", "Verknüpfung")
	translations["school"] = T("Centre", "Centro", "School", "Schule")
	return translations

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
