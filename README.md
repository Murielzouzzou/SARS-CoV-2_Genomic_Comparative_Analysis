# SARS-CoV-2_Genomic_Comparative_Analysis
Analyse comparative génomique d’un isolat français du SARS-CoV-2 avec la souche de référence Wuhan-Hu-1.


🎯 Objectif du projet

Ce projet consiste en une analyse comparative de séquences génomiques virales réalisée à partir :

d’un isolat français du SARS-CoV-2 (MT470152.1)

de la séquence de référence Wuhan-Hu-1 (NC_045512.2)

L’objectif est d’identifier les variations nucléotidiques apparues lors de la propagation du virus et de quantifier la similarité génomique entre les deux souches.

🧠 Démarche personnelle

Ce projet s’inscrit dans une démarche personnelle d’exploration en bioinformatique.
Animée par une forte curiosité scientifique et un intérêt marqué pour l’analyse des données biologiques, j’ai souhaité approfondir de manière autonome les méthodes de comparaison génomique appliquées à un cas réel.

Il constitue une première approche concrète des outils et raisonnements mobilisés en bioinformatique comparative.

📚 Sources des données

Les séquences utilisées sont publiques et ont été téléchargées depuis :

NCBI GenBank (référence Wuhan-Hu-1, NC_045512.2)

ENA / EMBL-EBI (isolat français MT470152.1)

🛠 Méthodologie

L’analyse a été réalisée en Python et comprend :

Lecture et parsing de fichiers FASTA

Calcul de la longueur génomique

Analyse de la composition nucléotidique (A, T, C, G)

Calcul du pourcentage GC

Comparaison position par position des deux génomes

Détection des substitutions nucléotidiques

Classification des mutations (transitions / transversions)

📊 Résultats principaux

Longueur du génome : 29 903 bases

GC content : 37,96 %

Nombre de différences observées : 6 substitutions

Similarité globale : 99,9799 %

🧬 Mutations identifiées
Position	Wuhan	France	Type
2480	A	G	Transition
2558	C	T	Transition
11083	G	T	Transversion
14805	C	T	Transition
24095	G	T	Transversion
26144	G	T	Transversion
🔬 Interprétation

Les différences observées reflètent l’évolution naturelle du virus au cours de sa propagation mondiale.

Les virus à ARN présentent des mutations ponctuelles lors de leur réplication. Les six substitutions identifiées représentent une divergence de seulement 0,02 %, cohérente avec la dynamique mutationnelle attendue pour le SARS-CoV-2 en 2020.

💻 Compétences mobilisées

Manipulation de données génomiques

Traitement de fichiers biologiques (FASTA)

Analyse comparative de séquences

Détection et interprétation de mutations

Programmation Python appliquée à la bioinformatique

Interprétation biologique des résultats

🚀 Perspectives d’approfondissement

Analyse phylogénétique sur plusieurs isolats

Étude des régions codantes affectées

Traduction des séquences pour analyser l’impact protéique des mutations

Visualisation graphique des variations génomiques
