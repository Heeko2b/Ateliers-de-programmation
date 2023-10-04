package Ateliers_de_programmation.Java.Atelier_1.Ex1;

public class DeMemoire extends De {
    int memoire = 0;

    public DeMemoire(String nom, int nbFaces) {
        super(nom, nbFaces);
    }

    // Méthode de lancer de dé mémoire, si le résultat est égal au résultat
    // précédent, on relance le dé
    // A corriger
    public int lancer() {
        int resultat = 0;
        do {
            resultat = super.lancer();
        } while (resultat == memoire);
        memoire = resultat;
        return resultat;
    }
}
