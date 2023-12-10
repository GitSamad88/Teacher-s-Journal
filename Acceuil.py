import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
import pathlib
import shutil

st.set_page_config(page_icon="notebook_with_decorative_cover:",
    page_title="Multipage App")

#logo_short_url = "https://lh3.googleusercontent.com/pw/ADCreHdOa7p9Daww_kxpctHG6JjyyuqMBPAp9JYJNRYhTjnWAuKNJk477fDhoM2Z724qRemehhezGNq6U0o4omKYE8MPKt9rz3qlnsFIopxmSq1Z3id-Ud709F56KxXW9b71Kb03C8VLO44mpNdC5DrTaR8mC0yIM6esYjyynEawBYtiVPyO8JlhZ10Lu-DX_df9mriuf5NJoyOxMpYzT28vctH8hSRoxRtVCN7wGqjxEiF1Q8bXT6fjQmJ_jp_ndnVJAttxyyb9_mD2bMjXf24xuybr-0AFsjkzZWl3qbVLoA9JjD07cGyi_VGSHp6hFfwBkxih7E9ew7DxvdTqtcqdBSBipUmyuVEh6S5aQQjNqbcCakWAj-jmmv-PSyK5jow-Tcjg0X75z68_pt0yZn6Hfj18e00_hboE9oZJ-bPxi2mBKu81mWrf0N7M6ThTdAYwTPzlFdWVVsWJ0J1AHRyYZSgLgB0SdhpIFkL4Da898-NVW02nRr5TcfK13YcuVfXdR5xmtCzSJfpmdj1rxWGmH39At9uSW8WRGKgEQvPAdhcs3fB8OhUj1j9X848zq34ccUmmlIHB1nXG400TeQezxkIoqZcKH_-liS4ocjds0CafsTeRn0_eZPZjol4IpmJSeh6N-J4VU_-hV35kTb5D4owMiJDsQAed7aBEx9__BKsvqalOOTiFA-dBe902Le_f1p0lIpdBxOCwO_FTKpM2KS3bQrsn0T5-21dc8xBBuo7Zdil_mEywhJ8uA4F1CebLFV00wiJlf04GcBJ2Ma8zhxhRgmsSx2hT2tBtegebOOlWUCrdMqFOEMsBxukD7WbizLOgI7IaJB_S8Dui_EA9sz1WOyllnmN6jx_OigAiysLkq4YZpdhZOARpdW_X-rTr7u8o=w100-h100-s-no-gm?authuser=0"
logo_icon = "notebook_with_decorative_cover:"
add_logo(logo_short_url,height=100)



link = "Made by [TAOUFIQ ABDESSAMAD](https://www.linkedin.com/in/abdessamad-taoufiq-082013209/)"
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


