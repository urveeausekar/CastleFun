from audioop import ratecv
from crypt import methods
from glob import glob
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect

app = Flask(__name__)

castles = {
	"1" : {
		"id": "1",
		"title": "Corvin Castle",
		"name" : "corvin",
		"image": "https://upload.wikimedia.org/wikipedia/commons/3/38/Hunedoara_castle.jpg",
		"year": "1446",
		"country": "Romania",
		"summary": "Corvin Castle, also known as Hunyadi Castle or Hunedoara Castle, is a Gothic-Renaissance castle in Hunedoara, Romania. It is a very beautiful castle that was used as the residence of the ruling family of the area. it was the place where Vlad the Impaler (popularly known as the real-life Dracula), was held prisoner by John Hunyadi, Hungary's military leader and regent during the King's minority. the castle was used as the 'Carta Monastary' in the horror movie 'The Nun'.",
		"genres": ["Romania", "gothic", "renaissance", "15th century"],
		"pop" : ["Vlad the Impaler", "The Nun", "Dracula"],
		"rating" : "8.9/10",
		"time" : "Tues to Sun : 8:00 - 19:00, Monday closed",
		"text" : "Visit the beautiful castle where 'The Nun' was filmed! Perfect for horror and history fans!"
	},
	"2" : {
		"id": "2",
		"title": "The Castle Orava",
		"name" : "orava",
		"image": "https://upload.wikimedia.org/wikipedia/commons/3/35/Orava_Castle_01.jpg",
		"year": "1267",
		"country": "Slovakia",
		"summary": "Orava Castle is a castle situated on a high rock above Orava river in the village of Oravský Podzámok, Slovakia. It is considered to be one of the most beautiful castles in Slovakia. The castle was built in the Kingdom of Hungary in the thirteenth century. The original design was in Romanesque and Gothic style; it was later reconstructed as a Renaissance and Neo-Gothic structure, hugging the shape of the 520-metre spur on which it perches. Many scenes of the 1922 film Nosferatu were filmed here, the castle representing Count Orlok's Transylvanian castle. In their 2020 TV adaptation of Bram Stoker's novel Dracula, Mark Gatiss and Steven Moffat also used Orava as their Castle Dracula. It was also used by the Polish video game company CD Projekt as inspiration for the fictional Kaer Morhen, fortress for the witchers of the Wolf School in Andrzej Sapkowski's The Witcher book series.",
		"genres": ["Slovakia", "gothic", "renaissance", "13th century"],
		"pop" : ["Dracula", "The Witcher : Kaer Morhen"],
		"rating" : "9.7/10",
		"time" : "Tues to Sun : 7:30 - 18:00, Monday closed",
		"text" : "Tour the majestic castle that was the inspiration for the Wolf Witcher School in the Witcher games, Kaer Morhen! For fans of the Witcher games, and everyone else who likes scenic beauty!"
	},
	"3" : {
		"id": "3",
		"title": "Neuschwanstein Castle",
		"name" : "neuschwanstein",
		"image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Castle_Neuschwanstein.jpg",
		"year": "1869",
		"country": "Germany",
		"summary": "Neuschwanstein Castle is a 19th-century historicist palace on a rugged hill above the village of Hohenschwangau near Füssen in southwest Bavaria, Germany. The palace was commissioned by King Ludwig II of Bavaria as a retreat and in honour of Richard Wagner. A popular tourist destination, the palace has appeared prominently in several movies. It served as the inspiration for Disneyland's Sleeping Beauty Castle.",
		"genres": ["Germany", "romanesque", "gothic", "byzantine", "19th century"],
		"pop" : ["Sleeping Beauty Castle", "Chitty Chitty Bang Bang"],
		"rating" : "8.3/10",
		"time" : "All week : 7:00 - 19:00",
		"text" : "Come see the real Sleeping Beauty Castle!"
	},
	"4" : {
		"id": "4",
		"title": "The Alcazar of Segovia",
		"name" : "alcazar",
		"image": "https://upload.wikimedia.org/wikipedia/commons/5/50/ALCAZAR_DE_SEGOVIA_2.jpg",
		"year": "1120",
		"country": "Spain",
		"summary": "The Alcázar of Segovia (literally 'Segovia Fortress') is a medieval castle located in the city of Segovia, Castile and León, Spain. The fortress is a World Heritage Site by UNESCO. Rising out on a rocky crag above the confluence of two rivers near the Guadarrama mountains, it is one of the most distinctive castle-palaces in Spain by virtue of its shape. The alcázar was originally built to serve as a fortress but has served as a royal palace, a state prison, a Royal Artillery College, and a military academy since then. The castle also served as the French home of Sir Lancelot du Lac, Joyous Gard, in the 1967 musical film Camelot. The castle's silhouette and overall appearance also inspired the castle in Disney's 1937 animated classic, Snow White and the Seven Dwarves.",
		"genres": ["Spain", "medieval", "12th century"],
		"pop" : ["Joyous Gard", "Snow White Castle", "Sir Lancelot du Lac"],
		"rating" : "7.0/10",
		"time" : "Wed to Mon : 6:00 - 19:00, Tuesday closed",
		"text" : "Visit the real-life castle from Disney's Snow White!"
	},
	"5" : {
		"id": "5",
		"title": "The Castle Bran",
		"name" : "bran",
		"image": "https://upload.wikimedia.org/wikipedia/commons/1/17/Castelul_Bran2.jpg",
		"year": "1377",
		"country": "Romania",
		"summary": "Bran Castle (Romanian: Castelul Bran; German: Schloss Bran; Hungarian: Törcsvári kastély) is a castle in Bran, 25 kilometres (16 mi) southwest of Brașov. It is a national monument and landmark in Transylvania. The fortress is on the Transylvanian side of the historical border with Wallachia, on road DN73. Commonly known outside Transylvania as Dracula's Castle, it is often referred to as the home of the title character in Bram Stoker's Dracula. There is no evidence that Stoker knew anything about this castle, which has only tangential associations with Vlad the Impaler, voivode of Wallachia, the putative inspiration for Dracula. Stoker's description of Dracula's crumbling fictional castle also bears no resemblance to Bran Castle.",
		"genres": ["Romania", "medieval", "Transylvania", "14th century"],
		"pop" : ["Dracula", "haunted"],
		"rating" : "8.4/10",
		"time" : "Tues to Sun : 6:30 - 19:30, Monday closed",
		"text" : "Experience the dramatic architecture of Dracula's castle!"
	},
	"6" : {
		"id": "6",
		"title": "Castle Poenari",
		"name" : "poenari",
		"image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Cetatea_Poenari_1.jpg",
		"year": "1250",
		"country": "Romania",
		"summary": "Poenari Castle, also known as Poenari Citadel (Cetatea Poenari in Romanian), is a ruined castle in Romania which was a home of Vlad the Impaler. The citadel is situated high atop a mountain and accessed by climbing 1,480 concrete stairs. A modern rendering of Poenari Castle was featured in the 2013 BBC Worldwide/Starz television series Da Vinci's Demons in the episode titled 'The Devil' in which Leonardo da Vinci travels to Poenari Castle in Wallachia to meet with Vlad III. In the 2020 documentary 'Romania: Seeking Dracula's Castle', the presenters declare that Poenari deserves the title 'Dracula's Castle' as it has the 'heart' of Vlad III.",
		"genres": ["Romania", "medieval", "ruined", "13th century"],
		"pop" : ["Dracula", "The Real Dracula's Castle", "haunted"],
		"rating" : "6.7/10",
		"time" : "Tues to Sun : 8:00 - 18:00, Monday closed",
		"text" : "Visit the real, 100 percent authentic citadel where Vlad III lived!"
	},
	"7" : {
		"id": "7",
		"title": "Edinburgh Castle",
		"name" : "edinburgh",
		"image": "https://upload.wikimedia.org/wikipedia/commons/2/26/Edinburgh_Castle_from_the_North.JPG",
		"year": "1050",
		"country": "Great Britain",
		"summary": "Edinburgh Castle is a historic castle in Edinburgh, Scotland. It stands on Castle Rock, which has been occupied by humans since at least the Iron Age, although the nature of the early settlement is unclear. Research undertaken in 2014 identified 26 sieges in its 1,100-year history, giving it a claim to having been 'the most besieged place in Great Britain and one of the most attacked in the world'. This beautiful castle has become a recognisable symbol of Edinburgh, and of Scotland. It is believed the castle is also haunted by a drummer who only appears when the castle is about to be attacked.",
		"genres": ["Scotland", "Great Britain", "11th century"],
		"pop" : ["Most besieged in Great Britain", "Occupied Since the Iron Age", "haunted"],
		"rating" : "7.9/10",
		"time" : "All week : 7:00 - 19:30",
		"text" : "Tour the most besieged castle in Great Britain! (Yes it's still standing!)"
	},
	"8" : {
		"id": "8",
		"title": "Stirling Castle",
		"name" : "stirling",
		"image": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Stirling_Castle_(6056086215).jpg",
		"year": "1110",
		"country": "Great Britain",
		"summary": "Stirling Castle, located in Stirling, is one of the largest and most important castles in Scotland, both historically and architecturally. Its strategic location has made it an important fortification in the region from the earliest times. The castle is open to the public year-round and is a popular place for tourists. Due to its similar appearance to Colditz Castle in Saxony, Germany, it was used to film the exterior shots for the 1970s TV series Colditz, a drama about the many attempts of Allied POWs to escape from the castle during its use as a military prison in the Second World War. There are reported sightings of a green lady who is said to be the ghost of one of Mary Queen of Scots servants.",
		"genres": ["Scotland", "Great Britain", "medieval", "12th century"],
		"pop" : ["Believed haunted", "Colditz"],
		"rating" : "7.2/10",
		"time" : "All week : 7:00 - 19:00",
		"text" : "Visit the 'most haunted' castle in Scotland! (Tell us if you see anything:))"
	},
	"9" : {
		"id": "9",
		"title": "Houska Castle",
		"name" : "houska",
		"image": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Hrad_Houska.JPG",
		"year": "1260",
		"country": "Czech Republic",
		"summary": "Houska Castle is an early Gothic castle, 47 kilometres north of Prague, in the Czech Republic. It is one of the best preserved castles of the period. Some notable features of the castle include a predominantly Gothic chapel, green chamber with late-Gothic paintings, and a knight's drawing room. The castle was built in an area of forests, swamps and mountains with no external fortifications, no source of water except for a cistern to collect rainwater, no kitchen, far from any trade routes, and with no occupants at its time of completion. Folklore considers this castle to cover one of the gateways to Hell, built to prevent demons (trapped in lower levels) from reaching the rest of the world. During World War II, the Wehrmacht occupied the castle until 1945. The Nazis were said to have conducted experiments into the occult there. This folklore was also the basis for the Doctor Who graphic novel Herald of Madness (2019), which is set at Houska Castle and was first published in Doctor Who Magazine 535-539",
		"genres": ["Czech Republic", "early gothic", "renaissance", "13th century"],
		"pop" : ["haunted", "Doctor Who", "gateway to hell"],
		"rating" : "6.9/10",
		"time" : "Tues to Sun : 8:30 - 17:30, Monday closed",
		"text" : "Come and see the castle famous as the gateway to hell!"
	},
	"10" : {
		"id": "10",
		"title": "Highclere Castle",
		"name" : "highclere",
		"image": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Highclere_Castle.jpg",
		"year": "1679",
		"country": "Great Britain",
		"summary": "Highclere Castle is a Grade I listed country house in England. The architecture style is Jacobethan. Highclere Castle has been used as a filming location for several films and television series, including 1990s comedy series Jeeves and Wooster and Marple. It is famous as the main location for the ITV historical drama series Downton Abbey. The castle became home to Egyptian artefacts after the 5th Earl, an enthusiastic amateur Egyptologist, sponsored the excavation of nobles' tombs in Deir el-Bahari (Thebes) in 1907, and employed archaeologist Howard Carter in the search for the tomb of Tutankhamun. The house, Egyptian exhibition, and gardens are open to the public for self-guided tours during the summer months and at other times during the rest of the year",
		"genres": ["Great Britain", "England", "Jacobethan", "17th century"],
		"pop" : ["Jeeves and Wooster", "Downton Abbey", "Egyptian artefacts", "Tutankhamun"],
		"rating" : "8.5/10",
		"time" : "All week : 7:30 - 19:00",
		"text" : "Like Downton Abbey? Visit the real thing!"
	}
}

# most_popular = [
# 	{
# 		"id": "1",
# 		"title": "Corvin Castle",
# 		"name" : "corvin",
# 		"image": "https://upload.wikimedia.org/wikipedia/commons/3/38/Hunedoara_castle.jpg",
# 		"year": "1446",
# 		"country": "Romania",
# 		"summary": "Corvin Castle, also known as Hunyadi Castle or Hunedoara Castle, is a Gothic-Renaissance castle in Hunedoara, Romania. It is a very beautiful castle that was used as the residence of the ruling family of the area. it was the place where Vlad the Impaler (popularly known as the real-life Dracula), was held prisoner by John Hunyadi, Hungary's military leader and regent during the King's minority. the castle was used as the 'Carta Monastary' in the horror movie 'The Nun'.",
# 		"genres": ["Romania", "gothic", "renaissance", "15th century"],
# 		"pop" : ["Vlad the Impaler", "The Nun", "Dracula"],
# 		"rating" : "8.9/10",
# 		"time" : "Tues to Sun : 8:00 - 19:00, Monday closed"
# 	},
# 	{
# 		"id": "2",
# 		"title": "The Castle Orava",
# 		"name" : "orava",
# 		"image": "https://upload.wikimedia.org/wikipedia/commons/3/35/Orava_Castle_01.jpg",
# 		"year": "1267",
# 		"country": "Slovakia",
# 		"summary": "Orava Castle is a castle situated on a high rock above Orava river in the village of Oravský Podzámok, Slovakia. It is considered to be one of the most beautiful castles in Slovakia. The castle was built in the Kingdom of Hungary in the thirteenth century. The original design was in Romanesque and Gothic style; it was later reconstructed as a Renaissance and Neo-Gothic structure, hugging the shape of the 520-metre spur on which it perches. Many scenes of the 1922 film Nosferatu were filmed here, the castle representing Count Orlok's Transylvanian castle. In their 2020 TV adaptation of Bram Stoker's novel Dracula, Mark Gatiss and Steven Moffat also used Orava as their Castle Dracula. It was also used by the Polish video game company CD Projekt as inspiration for the fictional Kaer Morhen, fortress for the witchers of the Wolf School in Andrzej Sapkowski's The Witcher book series.",
# 		"genres": ["Slovakia", "gothic", "renaissance", "13th century"],
# 		"pop" : ["Dracula", "The Witcher : Kaer Morhen"],
# 		"rating" : "9.7/10",
# 		"time" : "Tues to Sun : 7:30 - 18:00, Monday closed"
# 	},
# 	{
# 		"id": "3",
# 		"title": "Neuschwanstein Castle",
# 		"name" : "neuschwanstein",
# 		"image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Castle_Neuschwanstein.jpg",
# 		"year": "1869",
# 		"country": "Germany",
# 		"summary": "Neuschwanstein Castle is a 19th-century historicist palace on a rugged hill above the village of Hohenschwangau near Füssen in southwest Bavaria, Germany. The palace was commissioned by King Ludwig II of Bavaria as a retreat and in honour of Richard Wagner. A popular tourist destination, the palace has appeared prominently in several movies. It served as the inspiration for Disneyland's Sleeping Beauty Castle.",
# 		"genres": ["Germany", "romanesque", "gothic", "byzantine", "19th century"],
# 		"pop" : ["Sleeping Beauty Castle", "Chitty Chitty Bang Bang"],
# 		"rating" : "8.3/10",
# 		"time" : "All week : 7:00 - 19:00"
# 	}
# ]

# ROUTES


# @app.route('/')
# def hello_world():
#    return render_template('welcome.html')

@app.route('/infinity')
def infinity():
	return render_template('log_sales.html', sales=sales, clients=clients)

@app.route('/')
def homepage():
	most_popular = [castles["1"], castles["2"], castles["3"]]
	return render_template('homepage.html', most_popular=most_popular)

# AJAX FUNCTIONS

@app.route('/view/<id>')
def view(id=None):
	#print(id)
	#print(type(id))
	data = castles[id]
	return render_template('view.html', data=data)

prev_results = []
prev_num_results = "0"
prev_query = ""

@app.route('/search', methods=['GET', 'POST'])
def search():
	global prev_results
	global prev_num_results
	global prev_query
	if request.method == 'POST':
		req = request.form
		if "query" in req:
			query = req["query"]
			#print(query)
			queryoriginal = query
			query = query.lower()
			num_results = 0

			if (query == "" or query.isspace() == True):
				#print("Found whitespace")
				return redirect(request.referrer)

			results = []
			for element in castles:
				#print(element)
				if query in castles[element]["title"].lower():
					results.append(castles[element])
					num_results = num_results + 1
				else:
					found = 0
					for popelement in castles[element]["pop"]:
						if query in popelement.lower():
							results.append(castles[element])
							num_results = num_results + 1
							found = 1
							break
					
					if found == 0:
						for genreelement in castles[element]["genres"]:
							if query in genreelement.lower():
								results.append(castles[element])
								num_results = num_results + 1
								break

					


			#print(results)
			#print(str(num_results))
			#print(query)
			prev_query = queryoriginal
			prev_num_results = str(num_results)
			prev_results = results
			return render_template('search.html', results=results, num_results=str(num_results), query=queryoriginal)
		else:
			return render_template('search.html', results=results, num_results=str(num_results), query=query)

	else:
		#print("________________________" + request.referrer)
		return render_template('search.html', results=prev_results, num_results=prev_num_results, query=prev_query)















@app.route('/save_sale', methods=['GET', 'POST'])
def save_sale():
	global sales
	global current_id
	json_data = request.get_json()
	
	# make new object
	new_id = current_id
	current_id = current_id + 1
	new_record = {
		"id": new_id,
		"salesperson": json_data["salesperson"],
		"client": json_data["client"],
		"reams": json_data["reams"]
	}
	# sales.append(new_record)
	sales.insert(0, new_record)

	# Update client list if necessary
	if json_data["client"] in clients:
		pass
	else:
		clients.append(json_data["client"])
	# Send back new data
	new_data = sales.copy()
	new_data.append(clients)

	return jsonify(sales=new_data)


@app.route('/delete_sale', methods=['GET', 'POST'])
def delete_sale():
	global sales
	global current_id
	id = request.get_json()

	# remove element from sales
	j = 0
	for element in sales:
		if id == element["id"]:
			break
		else:
			j = j + 1
	sales.pop(j)

	current_id = current_id - 1

	return jsonify(sales=sales)

if __name__ == '__main__':
   app.run(debug = True)




