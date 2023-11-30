import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

buffer = BytesIO()


def emplois_df(emplois):
    emplois["Jour"] = jours
    emplois["Matière"] = matieres
    emplois["Durèe"] = dures
    emplois["Niveau"] = niveaux
    emplois["Sèance"] = seances
    emplois.dropna(inplace=True)
    emplois.index=range(emplois.shape[0])
    #st.table(emplois)
    csv_file = emplois.to_csv(index=False)
    st.download_button(
        label="Télèchargez votre emplois",
        data=csv_file,
        file_name=f"emplois_{emplois['Niveau'].unique()[0]}_{emplois['Niveau'].unique()[1]}.csv",
        key="download_button"
    )


if "emplois" not in st.session_state:
    st.session_state["emplois"] = pd.DataFrame(columns=["Jour", "Matière","Sèance", "Durèe","Niveau"])

emplois = pd.DataFrame(columns=["Jour", "Matière","Sèance", "Durèe","Niveau"])
st.title("Emplois Du Temps")
form = st.form(key="key1")

creat_or_import = form.selectbox("choisissez une option: ", ["Créer un nouveau emplois", "Importer votre emplois"],
                                 # max_selections=1,
                                 index=None, key="crorimpo",
                                 placeholder="Choose an option")  # default="Crèer un nouveau emplois")
form.form_submit_button("Confirmez votre choix")

if creat_or_import == None:
    st.warning("svp, choisissez une option!")
elif (creat_or_import == "Créer un nouveau emplois"):

    jours, matieres, dures, niveaux,seances = [], [], [], [],[]

    level1_courses = ["",'Maths', 'Eveil Scientifique', 'Act. Orales', 'Oral ', 'Lecture',
                      'Graphisme', 'Ecriture / Copie', 'Comptine/ Chant', 'Projet de classe']
    level2_courses = ["",'Maths', 'Eveil Scientifique', 'Oral (Ecouter/Dire)',
                      'Lecture/ Ecriture', 'Copie/ Dictée', 'Exercices écrits', 'Poésie',
                      'Projet de classe']

    level3_courses = ["",'Maths', 'Eveil Scientifique', 'Act. Orales',
                      'Lecture', 'Poésie',
                      'Ecriture / Copie', "Prod. De l'écrit",
                      'Projet de classe', 'Exercices écrits']

    level4_courses = ["",'Maths', 'Eveil Scientifique', 'Projet de classe', 'Act.Orales', 'Lecture', 'Ecriture Copie',
                      'Grammaire', 'Conjugaison', 'Orthographe', 'Poésie', 'P.  de l’écrit', 'Dictèe']

    level_5_6_courses = ["",'Maths', 'Eveil Scientifique', 'Act. orales', 'Lecture', 'Lexique', 'Grammaire',
                         'Conjugaison', 'Orthographe', 'Production de l’écrit',
                         'Lecture diction', 'Projet de classe']

    for n, m in enumerate(["premier", "deuxieme"]):
        niveau = form.selectbox("Sélectionnez le niveau", range(1, 7),
                                placeholder="choisissez une option",
                                index=None, key=f"niveau{n}")
        x = ''
        form.form_submit_button(f"Confirmez le {m} niveau")

        form.header(f"Emplois Du Niveau: {niveau if niveau != None else x}")
        for jour in range(1, 7):
            form.info(f"Jour : {jour}")
            for i in range(1, 5):
                form.markdown(f"<h3 style='text-align: center;font-size: 12px;'>Matiere : {i}</h1>",
                              unsafe_allow_html=True)
                col1, col2,col3 = form.columns(3)
                matiere = col1.selectbox("Sèlèctionnez une matière:",
                                         level1_courses if niveau == 1
                                         else level2_courses if niveau == 2
                                         else level3_courses if niveau == 3
                                         else level4_courses if niveau == 4
                                         else level_5_6_courses if (niveau == 5)
                                                                   or (niveau == 6)
                                         else [None]
                                         , key=f"matiere{i}jour{jour}niveau{n}")

                duree = col2.number_input("Entrez la durée: ",value=0,
                                          key=f"dure{i}jour{jour}niveau{n}")
                seance = col3.number_input("Entrez la séance: ",value=0,
                                          key=f"seance{i}jour{jour}niveau{n}")

                form.write("----------------")

                matieres.append(matiere)
                dures.append(int(duree) if duree!=0 else np.nan )
                seances.append(int(seance) if seance!=0 else np.nan)
                jours.append(jour)
                niveaux.append(niveau)

    enregistrer = form.form_submit_button("Confirmez et enregistrez")  # , on_click=emplois_df(emplois=emplois))
    if enregistrer:
        try:
            emplois_df(emplois=emplois)
            st.success("votre emplois a été bien enregistrè!")
        except :
            st.warning("Il faux au moins sèlèctioner une matière avec sa durèe "
                       "et sa sèance!")


elif creat_or_import == "Importer votre emplois":
    # """warnings: you have to add instructions!"""
    st.warning(
        'Remarque: Votre fichier doit se forme CSV.'
        'Les colonnes de votre fichier doivent être "Niveau", "Jour", "Matière", "Séance" et "Durée"')

    if st.button("Cliquez ici pour voir un exemple! "):
        # You have change this:
        example = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/1tWMj4Lfe22t2aUuLiromCUhAN5bsXA4OFPI_sXz6ELQ/gviz/tq?tqx=out:csv&sheet=emplois_3_4")
        st.info("Emplois du temps de 3 et 4 aep: ")
        st.table(example)
    # Upload a CSV file
    file = st.file_uploader("Importez votre emplois", type=["csv"])

    if file is not None:
        # Read the CSV file into a DataFrame

        emplois = pd.read_csv(file)
        if all(item in list(emplois.columns) for item in ["Jour", "Matière", "Sèance", "Durèe", "Niveau"]):
            emplois.dropna(inplace=True)
            emplois.index=range(emplois.shape[0])
            #emplois["Sèance"]=emplois["Sèance"].astype("int")
            #emplois["Durèe"]=emplois["Durèe"].astype("int")

            #st.table(emplois)
            st.success("votre emplois a été bien importè!")
            # print(emplois)
        else:
            #warnings
            st.warning("Attention:Les colonnes de votre fichier doivent "
                       "être :  Jour, Matière, Sèance, Durèe et Niveau!")
            st.warning(f"Vous avez importé un fichier avec les colonnes:"
                       f"{list(emplois.columns)}")



emplois[["Sèance", "Durèe"]] = emplois[["Sèance", "Durèe"]].astype("int")

st.table(emplois)
st.session_state["emplois"]=emplois
# connect google adsense
st.write("ads")
st.markdown("""
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4265574502229447"
    crossorigin="anonymous"></script>""",unsafe_allow_html=True)

