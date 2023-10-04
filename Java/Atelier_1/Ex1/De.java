package Ateliers_de_programmation.Java.Atelier_1.Ex1;

import java.util.Random;

public class De {
    // Nom du dé
    private String nom;

    // Nombre de faces du dé
    int nbrFaces;

    // Nombre de dés crées
    static int nbrDe = 0;

    // Générateur de nombres aléatoires
    private static Random r = new Random();

    // METHODES

    // Méthode pour afficher le nombre de faces du dé
    public int getNbFaces() {
        return this.nbrFaces;
    }

    // Méthode pour changer le nombre de faces du dé
    public void setNbFaces(int nbFaces) {
        nbrFaces = nbFaces;
        System.out.println("Le nombre de faces du dé " + this.getNom() + " a été modifié à " + nbrFaces);
    }

    // Méthode pour récupérer le nom d'un dé
    public String getNom() {
        return this.nom;
    }

    public int getNbrDe() {
        return De.nbrDe;
    }

    // Méthode pour lancer un dé
    public int lancer() {
        // Génère un nombre aléatoire entre 1 et le nombre de faces du dé (la valeur du
        // dé max est exclue, donc le +1 sera le dé max)
        int nbAleatoire = r.nextInt(this.nbrFaces) + 1;
        return nbAleatoire;
    }

    // Surcharge de lancer pour pouvoir lancer plusieurs dés a la suite et récupérer
    // le meilleur lancer
    public int lancer(int nbr) {
        int meilleurLancer = 0;
        for (int i = 0; i < nbr; i++) {
            int nbAleatoire = r.nextInt(this.nbrFaces) + 1;
            if (nbAleatoire > meilleurLancer) {
                meilleurLancer = nbAleatoire;
            }
        }
        return meilleurLancer;

    }

    // CONSTRUCTEURS

    // Constructeur par défaut
    public De(String nom, int nbFaces) {
        nbrDe += 1;
        if (nom == null)
            this.nom = "De n°" + nbrDe;
        else
            this.nom = nom;
        if (nbFaces > 3 && nbFaces < 120) {
            this.nbrFaces = nbFaces;
        } else {
            System.out.println(
                    "Création de " + nom + " impossible : le nombre de faces du dé doit être compris entre 3 et 120");
        }
    }

    // Constructeur de dé sans paramètres
    public De() {
        this(null, 6);
    }

    // Constructeur de dé avec le nombre de faces en paramètre
    public De(int nbFaces) {
        this(null, nbFaces);
    }

    // Constructeur de dé avec un nom en paramètre
    public De(String nom) {
        this(nom, 6);
    }

    // Redéfinition de toString
    public String toString() {
        return "Le dé " + this.getNom() + " a " + this.getNbFaces() + " faces.";
    }

    // Redéfinition de equals, qui compare le nombre de faces
    public boolean equals(Object o) {
        boolean result = false;
        if (o != null && o instanceof De) {
            De de = (De) o;
            result = ((this.getNbFaces() == de.getNbFaces()) && (this.getNom().equals(de.getNom())));
        }
        return result;
    }
}