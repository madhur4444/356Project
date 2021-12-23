from io import StringIO
import sys
import client

def main():
    testcases = [
        "am\nSpider-Man: No Way Home\n2021-12-16\n148\nUSA, India, Canada\nEnglish\nJon Watts\n\nMarvel Studios\nTom Holland, Zendaya, Benedict Cumberbatch, Jacob Batalon, Jon Favreau\nSpider-Man: No Way Home is a 2021 American superhero film based on the Marvel Comics character Spider-Man, co-produced by Columbia Pictures and Marvel Studios and distributed by Sony Pictures Releasing. It is the sequel to Spider-Man: Homecoming (2017) and Spider-Man: Far From Home (2019), and is the 27th film in the Marvel Cinematic Universe (MCU).\n$200,000,000\n$328,000,000\n$751,300,000\n1297\n327\n",
        "dm\n",
        "um\n",
        "tm\n5\n",
        "actm\nMiss Jerry\n",
        "tmg\nDrama\n5\n",
        "abt\n02-29\n",
        "mvus\n5\n",
        "mvo\n5\n",
        "tmxc\nUSA\n5\n",
        "lrm\n5\n",
        "awaxy\n1910\n1911\n",
        "mba\nAsta Nielsen\n",
        "mdd\nCharles L. Gaskill\n",
        "tmy\n2010\n5\n",
        "abmxy\nFollie di jazz\nCenerentola a Parigi\n"
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
            'Name': ['Lejos de Casa pelicula Venezolana', 'Ek', 'Jeeudo', 'Hopeful Notes', 'Isha'],
            'Rating': ['9.80', '9.80', '9.80', '9.70', '9.50'],
            'Language': ['Spanish', 'Telugu', 'English, Nepali', 'English', 'Malayalam'],
            'Duration': ['87', '129', '150', '94', '118']},
        {
            'Name': ['Joss Ackland', 'Dennis Farina', 'Antonio Sabato Jr.', 'Knut Agnred', 'Domingo Ambriz', 'Albert Augier', 'Chester Barnett', 'Eric Benz', 'Aldo Berti', 'Gérard Darmon', 'Jimmy Dorsey', 'Ken Foree', 'Arthur Franz', 'Yoshio Harada', 'Harvey Jason', 'Edward Jobson', 'Shane Johnson', 'Aleksandr Khochinsky', 'Kosti Klemelä', 'Ted Le Plat', 'James Mitchell', 'John Niland', 'Ivan Petrov', 'Dan Priest', 'Alex Rocco', 'Ja Rule', 'Bjarke Smitt Vestermark', 'Eric Stanley', 'Vladimir Tikhonov', 'René Verreth', 'Richard Lewis Warren', 'Saul Williams', 'Erol Büyükburç', 'Marek Richter', 'Nejat Isler', 'Arnaud Valois', 'Peter Scanavino', 'Jessie T. Usher', 'Dallas Barnett', 'Phil Haney', 'James Cullen Bressack']
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
            "Name": ["Asta Nielsen", "Emil Albes", "Hugo Flink", "Gunnar Helsengreen", "Valdemar Psilander", "Mary Hagen", "Giuseppe de Liguoro", "Salvatore Papa", "Arturo Pirovano", "Pier Delle Vigne", "Andrey Gromov", "Ivan Mozzhukhin", "N. Semyonov", "Olga Petrova-Zvantseva", "Lea Giunchi", "Augusto Mastripietri", "Polidor", "Natalino Guillaume", "Jovan Antonijevic-Djedo", "Teodora Arsenovic", "Mileva Bosnjakovic", "Dimitrije Ginic", "Vitomir Bogic"]
        },
        {
            "Title": ["Den sorte drøm", "Amleto", "La via senza gioia", "Fante-Anne"],
            "Language": ["", "German", "German", ""],
            "Duration": ["53", "131", "125", "93"]
        },
        {
            "Title": ["Cleopatra"],
            "Language": ["English"],
            "Duration": ["100"]
        },
        {
            "Title": ["Hopeful Notes", "Les Misérables in Concert: The 25th Anniversary", "Inception", "Doraleous and Associates", "Aaranya Kaandam"],
            "Rating": ["9.70", "8.80", "8.80", "8.60", "8.60"],
            "Language": ["English", "English", "English, Japanese, French", "English", "Tamil"],
            "Duration": ["94", "178", "148", "100", "126"]
        },
        {
            "Name": ["Fred Astaire"]
        }
    ]

    for i in range(len(testcases)):
        sys.stdin = StringIO(testcases[i])
        assert client.main() == expected[i]

if __name__ == "__main__":
	main()