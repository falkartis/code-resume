from myTypes import *

def GetPrivateData():

	T = Translation

	phoneNumber = T("Nùmero de telèfon", "Número de teléfono", "Phone number", "Telefonnummer")
	emailAddress = T("Correu electrònic", "Correo electrónico", "Email", "Email")
	location = T("Localitat", "Localidad", "Location", "Ortschaft")

	data = [
		Header(phoneNumber, "replace this with your real phone number"),
		Header(emailAddress, "replace this with your real email address"),
		Header(location, "replace this with your rela location")
	]

	return data


def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
