# TP site statique
Ce TP est un projet de classe qui nous a été proposé par notre professeur Mr.Poulailleau Vincent. Il a pour but de convertir des fichiers markdown ".md" en ".html". Pour pouvoir générer des sites statiques.

Sujet: https://github.com/vpoulailleau/site_statique

## Explication

Il faudra donc entrer obligatoirement un dossier d'entrée contenant les fichiers markdown que vous voulez convertir. Ce dossier peut également contenir d'autres fichiers, toute fois ils ne seront pas pris en compte par le programme. Le programme ne convertira que les fichiers markdown.
Il faut aussi entrer un dossier de sorti qui n'existe pas déjà le programme vous le créera. Dans ce nouveau dossier vous trouverez soit vos fichier markdown converti en fichier html(cas ou il n'y a pas de template sélectionné). Soit le contenu du dossier template ainsi que la conversion des fichiers markdown en html dans un seul fichier nommé "your_new_template.html" si l'option n n'a pas été utilisé.
 
Deux option sont possible :

 * -t Le choix du modèle de page internet. Qu'il vous faudra vous procurer sur internet, un exemple vous est donné dans se rappport (voir plus haut).Il faudra également rajouter `<REPLACE_ME>` dans le fichier index.html qui se trouve à la racine de votre dossier template. Vos fichier markdown converti se trouveront à cette place. 
 * -n Le nom de votre nouveau fichier html associé au template choisi.

## Argument:
 * -i : Sélection du dossier "d'entrée". Le dossier qui contient vos fichier markdown que vous souhaité convertir en html.
 * -o : Sélection du dossier de "sortie". Le dossier qui contiendra: 
    * Soit seulement les fichier markdown convertie en html.
    * Soit un seul fichier html contenant tous les fichiers d'entrées convertie avec le template. 
 * -t : Sélection du fichier contenant le model de la page internet dans votre dossier template. En générale ce fichier ce nomme : index.html.
 * -n : Vous permet de choisir le nom de votre nouveaux fichier html.
 * -h : Commande d'aide.