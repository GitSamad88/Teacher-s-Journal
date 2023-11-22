import pandas as pd
import numpy as np
import json

def fr_manuel_level(manuel, level):
    mes_app1 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\Repa  fr dire faire 1aep final.csv")  # to be changed!
    mes_app2 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\repa fr mes app 2aep (Edited _6).csv")
    mes_app3 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\repartition_annuelle_fr_mes_apprentissage_3aep_final.csv")
    mes_app4 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\repartiton_FR_Mes apprentissage_4AEP.csv")
    mes_app4["Dictèe"] = mes_app4["Orth / Dictée"]
    mes_app4.rename(columns={"Orth / Dictée": "Orthographe"}, inplace=True)
    mes_app5 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\annuelle repa mes app 5aep (Edited _7).csv")
    mes_app6 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\fr repa\Mes apprentissage\Repa Fr Mes app 6 aep (Edited _3).csv")

    Mes_app_manuel = [mes_app1, mes_app2, mes_app3, mes_app4, mes_app5, mes_app6]
    fr_manuels = {"Mes apprentissages": Mes_app_manuel, "L'oasis des mots": [], "Pour communiquer": [],
                  "L'école des mots": [], "Le nouvel espace": [], "Mon livre de français": []}

    try:
        return fr_manuels[str(manuel)][int(level) - 1]
    except:
        print("Ce manuel n'est disponible pour ce niveau, essayez un autre manuel!")
        print("Remarque: le niveau doit etre entre 1 et 6!")


# Maths

def maths_manuel_level(manuel, level):
    moufid1 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Almoufid\Repa Maths Moufid 1aep.csv")
    moufid2 = pd.DataFrame()
    moufid3 = pd.DataFrame()
    moufid4 = pd.DataFrame()
    moufid5 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Almoufid\Repa Maths Almoufid 5aep .csv")
    moufid6 = pd.DataFrame()
    moufid_manuel = [moufid1, moufid2, moufid3, moufid4, moufid5, moufid6]

    # Jayed
    jayed1 = pd.DataFrame()
    jayed2 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Jayed\Repa Maths Jayed 2 aep.csv")
    jayed3 = pd.DataFrame()
    jayed4 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Jayed\Repartition_Maths_Jayed_4aep.csv")
    jayed5 = pd.DataFrame()
    jayed6 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Jayed\Repa Maths Jayed 6 aep.csv")
    jayed_manuel = [jayed1, jayed2, jayed3, jayed4, jayed5, jayed6]

    # Fadaa:
    fada1 = pd.DataFrame()
    fada2 = pd.DataFrame()
    fada3 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\Maths repa\Fada2\Repa__3aep_Maths_Fada2.csv")
    fada4 = pd.DataFrame()
    fada5 = pd.DataFrame()
    fada6 = pd.DataFrame()
    fadaa_manuel = [fada1, fada2, fada3, fada4, fada5, fada6]

    Maths_manuels = {"المفيد": moufid_manuel, "الجيد": jayed_manuel, "الفضاء": fadaa_manuel}

    try:
        if Maths_manuels[str(manuel)][int(level) - 1].empty:
            return "Ce manuel n'est pas disponible pour ce niveau, choisissez un autre manuel!"
        else:

            return Maths_manuels[str(manuel)][int(level) - 1]
    except:
        print("Ce manuel n'est pas disponible pour ce niveau, choisissez un autre manuel!")
        print("Remarque: le niveau doit etre entre 1 et 6!")


# In[94]:


maths_manuel_level(manuel="الجيد", level=1)


# ### Eveil Scientifque:
#

# In[106]:


def EvSc_manuel_level(level, manuel):
    # Jadid
    es_Jadid1 = pd.read_csv(r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Jadid\Repa EvSc Jadid 1aep.csv")
    es_Jadid1 = es_Jadid1[["U", "S", "Eveil Scientifique", "Sèance"]].dropna(axis=0)
    es_Jadid1["Sèance"] = [json.loads(es_Jadid1["Sèance"][i]) for i in range(len(es_Jadid1["Sèance"]))]

    es_Jadid2 = pd.DataFrame()
    es_Jadid3 = pd.DataFrame()
    es_Jadid4 = pd.DataFrame()
    es_Jadid5 = pd.DataFrame()
    es_Jadid6 = pd.DataFrame()
    es_jadid_manuel = [es_Jadid1,
                       es_Jadid2,
                       es_Jadid3,
                       es_Jadid4,
                       es_Jadid5,
                       es_Jadid6]

    # Fadaa
    es_fadaa1 = pd.DataFrame()
    es_fadaa2 = pd.DataFrame()
    es_fadaa3 = pd.DataFrame()
    es_fadaa4 = pd.DataFrame()
    es_fadaa5 = pd.DataFrame()
    es_fadaa6 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Fada2\Repa EvSc Fada2 6aep (Edited _3).csv")
    es_fadaa6 = es_fadaa6[["U", "S", "Eveil Scientifique", "Sèance"]].dropna(axis=0)
    es_fadaa6["Sèance"] = [json.loads(es_fadaa6["Sèance"][i]) for i in range(len(es_fadaa6["Sèance"]))]
    es_fadaa_manuel = [es_fadaa1,
                       es_fadaa2,
                       es_fadaa3,
                       es_fadaa4,
                       es_fadaa5,
                       es_fadaa6]

    # Manhal

    manhal1 = pd.DataFrame()
    manhal2 = pd.DataFrame()
    manhal3 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Manhal\Repa EvSc Manhal 3aep (Edited _4).csv")
    manhal3 = manhal3[["U", "S", "Eveil Scientifique", "Séance "]].dropna(axis=0)
    manhal3.rename(columns={"Séance ": "Sèance"}, inplace=True)
    manhal3["Sèance"] = [json.loads(manhal3["Sèance"][i]) for i in range(len(manhal3["Sèance"]))]

    manhal4 = pd.DataFrame()
    manhal5 = pd.DataFrame()
    manhal6 = pd.DataFrame()

    manhal_manuel = [manhal1,
                     manhal2,
                     manhal3,
                     manhal4,
                     manhal5,
                     manhal6]
    # for df in manhal_manuel:
    #   df=df[["U","S","Eveil Scientifique","Sèance"]].dropna(axis=0)

    # Moufid

    es_moufid1 = pd.DataFrame()
    es_moufid2 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Moufid\Repa EvSc Moufid 2aep (Edited _5).csv")
    es_moufid2["Sèance"] = [json.loads(es_moufid2["Sèance"][i]) for i in range(len(es_moufid2["Sèance"]))]

    es_moufid3 = pd.DataFrame()
    es_moufid4 = pd.DataFrame()
    es_moufid5 = pd.DataFrame()
    es_moufid6 = pd.DataFrame()

    es_moufid_manuel = [es_moufid1,
                        es_moufid2,
                        es_moufid3,
                        es_moufid4,
                        es_moufid5,
                        es_moufid6]

    # Mounir
    es_mounir1 = pd.DataFrame()
    es_mounir2 = pd.DataFrame()
    es_mounir3 = pd.DataFrame()
    es_mounir4 = pd.DataFrame()
    es_mounir5 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Mounir\Repa EvSc Mounir 5aep (Edited _6).csv")
    es_mounir5["Sèance"] = [json.loads(es_mounir5["Sèance"][i]) for i in range(len(es_mounir5["Sèance"]))]

    es_mounir6 = pd.DataFrame()
    es_mounir_manuel = [es_mounir1,
                        es_mounir2,
                        es_mounir3,
                        es_mounir4,
                        es_mounir5,
                        es_mounir6]

    # Marji3:
    es_marjii1 = pd.DataFrame()
    es_marjii2 = pd.DataFrame()
    es_marjii3 = pd.DataFrame()
    es_marjii4 = pd.read_csv(
        r"C:\Users\hp\Downloads\edited repartitions\EvSc repa\Marji3\Eveil Scientifique 4 aep ALMARJI3.csv")
    es_marjii4["Sèance"] = [json.loads(es_marjii4["Sèance"][i]) for i in range(len(es_marjii4["Sèance"]))]
    es_marjii5 = pd.DataFrame()
    es_marjii6 = pd.DataFrame()

    es_marjii_manuel = [es_marjii1,
                        es_marjii2,
                        es_marjii3,
                        es_marjii4,
                        es_marjii4,
                        es_marjii5,
                        es_marjii6
                        ]

    EvSc_manuels = {"الجديد": es_jadid_manuel,
                    "المنهل": manhal_manuel,
                    "الفضاء": es_fadaa_manuel,
                    "المفيد": es_moufid_manuel,
                    "المنير": es_mounir_manuel,
                    "المرجع": es_marjii_manuel}

    try:
        if EvSc_manuels[str(manuel)][int(level) - 1].empty:
            return "Ce manuel n'est pas disponible pour ce niveau, choisissez un autre manuel!"

        else:

            return EvSc_manuels[str(manuel)][int(level) - 1]
    except:
        print("Ce manuel n'est pas disponible pour ce niveau, choisissez un autre manuel!")
        print("Remarque: le niveau doit etre entre 1 et 6!")

