import server

def main():
    testcases = [
        "tm$$5",
        "actm$$Miss Jerry",
        "tmg$$Drama$$5",
        "abt$$02-29",
        "mvus$$5",
        "mvo$$5",
        "tmxc$$USA$$5",
        "lrm$$5",
        "awaxy$$"
    ]

    expected = [
        { 
            "Title": ["Suvarna Sundari", "Lejos de Casa pelicula Venezolana", "Jeeudo", "Ek", "Notuku Potu"],
            "Rating": ["9.90", "9.80", "9.80", "9.80", "9.80"],
            "Language": ["Telugu, Kannada", "Spanish", "English, Nepali", "Telugu", "Telugu"],
            "Duration": ["120", "87", "150", "129", "121"]
        },
        {
            "Actor Name": ["Blanche Bayliss", "William Courtenay", "Chauncey Depew"]
        },
        {
            "Name": ["Jeeudo", "Ek", "Lejos de Casa pelicula Venezolana", "Hopeful Notes", "Isha", "Jibon Theke Neya", "The Best Years", "Le ali della libertà", "Hababam Sinifi", "As I Am"],
            "Rating": ["9.80", "9.80", "9.80", "9.70", "9.50", "9.40", "9.40", "9.30", "9.30", "9.30"],
            "Language": ["English, Nepali", "Telugu", "Spanish", "English", "Malayalam", "Bengali", "English", "English", "Turkish", "English"],
            "Duration": ["150", "129", "87", "94", "118", "150", "96", "142", "87", "62"]
        },
        {
            "Name": ["Joss Ackland", "Dennis Farina", "Antonio Sabato Jr.", "Knut Agnred", "Domingo Ambriz", "Albert Augier", "Chester Barnett", "Eric Benz", "Aldo Berti", "Gérard Darmon", "Jimmy Dorsey", "Ken Foree", "Arthur Franz", "Yoshio Harada", "Harvey Jason", "Edward Jobson", "Shane Johnson", "Aleksandr Khochinsky", "Kosti Klemelä", "Ted Le Plat", "James Mitchell", "John Niland", "Ivan Petrov", "Dan Priest", "Alex Rocco", "Ja Rule", "Bjarke Smitt Vestermark", "Eric Stanley", "Vladimir Tikhonov", "René Verreth", "Richard Lewis Warren", "Saul Williams", "Erol Büyükburç", "Marek Richter", "Nejat Isler", "Arnaud Valois", "Peter Scanavino", "Jessie T. Usher", "Dallas Barnett", "Phil Haney", "James Cullen Bressack"]
        },
        {
            "Title": ["Il cavaliere oscuro", "Le ali della libertà", "Pulp Fiction", "Fight Club", "Forrest Gump"],
            "Votes": ["348363", "327264", "274101", "263329", "252635"],
            "Language": ["English, Mandarin", "English", "English, Spanish, French", "English", "English"],
            "Duration": ["152", "142", "154", "139", "142"]
        },
        {
            "Title": ["Le ali della libertà", "Il cavaliere oscuro", "Inception", "Fight Club", "Pulp Fiction"],
            "Votes": ["2278845", "2241615", "2002816", "1807440", "1780147"],
            "Language": ["English", "English, Mandarin", "English, Japanese, French", "English", "English, Spanish, French"],
            "Duration": ["142", "152", "148", "139", "154"]
        },
        {
            "Title": ["Hopeful Notes", "The Moving on Phase", "Love in Kilnerry", "Le ali della libertà", "As I Am"],
            "Rating": ["9.70", "9.50", "9.30", "9.30", "9.30"],
            "Language": ["English", "English", "English", "English", "English"],
            "Duration": ["94", "85", "100", "142", "62"]
        },
        {
            "Title": ["Prema Panjaram", "Holnap történt - A nagy bulvárfilm", "Seikai gûdo mooningu!!", "Ryûsei", "One Night: Choice of Evil"],
            "Rating": ["1.00", "1.00", "1.00", "1.00", "1.00"],
            "Language": ["Telugu", "Hungarian", "Japanese", "Japanese", "Min Nan, Mandarin"],
            "Duration": ["138", "82", "81", "78", "79"]
        },
        {

        }
    ]

    for i in range(len(testcases)):
        server.parseRequest(testcases[i])
        # assert server.parseRequest(testcases[i]) == expected[i]

if __name__ == "__main__":
	main()