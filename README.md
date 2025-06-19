# Grand-Oral_M2-IET

Cette expérimentation s'inscrit dans le cadre d'un travail de fin d'études présenté pendant le Master 2 "Intelligence économique et territoriale" (UFR Ingémédia, Université de Toulon). 
**Objectif** : mesurer puis analyser la polarité et la subjectivité des commentaires d'une pétition en ligne. 

Pour executer le code, respectez dans l'ordre chacune des étapes : 
- Lancer le script "Collecte.py" en remplaçant l'API sur la ligne "URL". Un fichier en sortie "pickle" est ainsi créé ;
- Lancer le script "Traite.py" en important le fichier .pkl, un second fichier au format .txt est écrit, avec les données traitées ;
- Lancer le script "AnalyseSP.py". Cette étape permet la création de 4 nouveaux fichiers en mesurant la polarité (+/-) et la subjectivité/objectivité) du fichier .pkl

Une fois les fichiers créés, vous pouvez les importer dans le logiciel IRaMuTeQ : http://www.iramuteq.org/ pour réaliser les différentes analyses. 

/!\ Attention, l'API du site change.org ne fonctionne plus depuis. 

# Pour nous citer...

Galliano, C. (2023). Le "Grand Oral" : une épreuve pédagogique de mise en situation au service des étudiants de master. Les Cahiers de la SFSIC, 18, pp.41-55. https://hal.science/hal-04146258v1
