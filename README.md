How to use:
=====================

To retrieve the results, copy the places_tweets.sh and finalproject.py files into a personal directory on karora (I named this directory researchmethods/).
To make sure it will run, run the following commands:

$ chmod a+x places_tweets.sh
$ chmod a+x finalproject.py

To run the place_tweets script, you can use either of the following commands:

$ ./places_tweets.sh
$ nohup ./places_tweets.sh

The second command writes the output of the terminal to an extra file called nohup.out, 
which ensures that the command will keep running after the terminal is closed.
This may be useful because the script has to go over a large dataset so it may take some time, 
and may otherwise stop running if the terminal is accidentally closed or if the user loses connection.

The dataset used is the following:

/net/corpora/twitter2/Tweets/ (on karora)

This script only needs the data from march to may (so directories 03, 04 and 05) of 2021.

The results are stored in the following file:

place_tweets_2021.txt

This file should look similar to this:

Amsterdam, The Netherlands, The Netherlands	Late beslissing, maar wel volkomen terecht natuurlijk. Vitesse was solide georganiseerd, maar creëerde zowat niks. Heerlijk voor Neres. Prachtig. #Ajax #ajavit #KNVBbeker
Haarlem, Nederland, Nederland	@JaapFriso Kuipers ziet toch geen herhaling? Lomp was het zeker.
's-Hertogenbosch, Nederland, Nederland	Zag ik nou Ten Hag de scheids een volle hand geven? 😅🤣 #VITAJA
Goes, Nederland, Nederland	@MauriceBernard Wedstrijd van ontzettend matig niveau. Konden passes over 5 meter nog niet naar elkaar spelen in het laatste kwartier.
Bunschoten, Nederland, Nederland	Dit is de mooiste club#Ajaxamsterdam ❌❌❌
Rijswijk, Nederland, Nederland	En dat dan "Mijn club" door de Kuip schalt!! 🤘🤘🤘🤘 #ajavit
The Hague, The Netherlands, The Netherlands	Beste @gosharingoff, een #go scooter stond in de weg op 18 april om 18:58 ter hoogte van Loosduinsekade 226 Den Haag. @RvanAsten waarom negeert u het? #FelyxChallenge https://t.co/d8kwYNrrLr


After retrieving this data, the script of finalproject.py can be used. 
To run the script, use the following command:

$ Python3 finalproject.py

The output of this file will not be stored in a serperate file, 
but can be read directly from the terminal window.

