import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Multipage App")

link = "This app is made by [TAOUFIQ ABDESSAMAD](https://www.linkedin.com/in/abdessamad-taoufiq-082013209/)"
st.sidebar.markdown(link,unsafe_allow_html=True)

st.title("Le Cahier Journalier Educatif")
st.write("Bienvenue,"
         " Le Cahier Journalier Educatif est une application novatrice conçue spécialement pour simplifier la vie des enseignants du cycle primaire. "
         "Notre application vise à transformer l'expérience de la tenue de journal en une tâche simple, intuitive et efficace,"
         " offrant ainsi aux enseignants plus de temps pour se concentrer sur l'essentiel : l'éducation de leurs élèves")

col1,col2=st.columns([0.4,0.6])
col1.header("Fonctionnalités Clés :")
col2.image("https://almouggar.com/web/image/product.template/428319/image")
col1.write("1. ***Création Facile de Cahiers de Journal :*** "
         "Avec Journal Educatif, la création de cahiers de journal n'a jamais été aussi simple. "
         "Les enseignants peuvent rapidement enregistrer leurs observations,"
         " évaluations et notes sur chaque élève,"
         " le tout dans une interface conviviale.")

col1.write("2. ***Personnalisation Intuitive :*** "
         "Chaque enseignant a sa propre façon de documenter le progrès de ses élèves. Journal Educatif permet une personnalisation complète,"
         " offrant la flexibilité nécessaire pour s'adapter aux différents styles d'enseignement.")

col2.image("https://almouggar.com/web/image/product.template/524364/image")
col1.write("3. ***Suivi du Progrès Individualisé :*** "
         " Grâce à notre fonction de suivi du progrès,"
         " les enseignants peuvent aisément suivre l'évolution de chaque élève au fil du temps."
         " Ceci facilite l'identification des forces et des domaines à améliorer,"
         " favorisant ainsi une approche pédagogique plus ciblée.")

col1.write("4. ***Communication Efficace avec les Parents :*** " 
         "Journal Educatif simplifie la communication avec les parents en permettant le partage facile des progrès des élèves."
         " Les enseignants peuvent envoyer des mises à jour,"
         " des commentaires et des suggestions directement depuis l'application.")


col1.write("5. ***Sécurité des Données :*** "
         "Nous comprenons l'importance de la sécurité des données éducatives."
         " Journal Educatif assure une protection maximale des informations confidentielles,"
         " garantissant que seuls les enseignants et les parents autorisés ont accès aux données. ")


col1.subheader("Pourquoi Le Cahier  Journalier Educatif ?")

col1.write("Le Cahier Journalier Educatif a été créé avec la conviction que la gestion du suivi des élèves "
         "devrait être aussi enrichissante que l'enseignement lui-même."
         " Notre application vise à simplifier le processus de création de cahiers de journal tout en offrant"
         " des outils puissants pour améliorer la communication et l'efficacité pédagogique.")

col1.write("Téléchargez Le Cahier Journalier Educatif dès aujourd'hui et découvrez "
         "comment notre application peut transformer"
         " la façon dont les enseignants du cycle primaire gèrent leurs cahiers de journal, "
         "libérant ainsi du temps précieux pour se concentrer sur "
         "l'enseignement et l'épanouissement de leurs élèves.")

