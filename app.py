#Import de Streamlit
import streamlit as st

#Import de Matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Option de couleur du modèle pour centraliser
theme = st.color_picker('', '#02BD02')

st.title(f":green[Simulateur de stratégie d'option]")

col1, col2 = st.columns(2)



#1.1 cette section concerne la page titre
st.title(f":green[Paramètres]")

with col1:
   Option = st.selectbox(
    "Choisissez une stratégie d'option",
    ("Long Call", "Long Put", "Short Call", "Short Put", "Covered Call", "Protective Put", "Straddle", "Strangle", "Butterfly Spread", "Bull Call Spread", "Bull Put Spread", "Bear Call Spread", "Bear Put Spread"))

#1.2 Cette section définie la stratégie du Long Call
def long_call(c, s, xc):
    
    """Cette fonction calcule les profits et pertes 
    sur l'achat d'un call
    c : la prime du call
    S : le prix du sous-jacent
    Xc : le prix d'exercice
    """
    
    profit = -c + max(0, s - xc)
    return profit

#1.3 Cette section définie la stratégie du Long Put
def long_put(p, s, xp):

    """Cette fonction calcule les profits et pertes 
    sur l'achat d'un put
    p : la prime (prix) du put
    S : le prix du sous-jcent
    Xp : le prix d'exercice
    """
    profit = -p + max(0, xp - s)
    return profit

#1.4 Cette section définie la stratégie du Short Call
def short_call(xc, c, s):
    
    """Cette fonction calcule les profits et pertes 
    sur la vente d'un call
    c : la prime du call
    S : le prix du sous-jcent
    Xc : le prix d'exercice
    """
    
    profit = c - max(0, s - xc)
    return profit

#1.5 Cette section concerne la stratégie de Short Put
def short_put(xp, p, s):
    
    """Cette fonction calcule les profits et pertes 
    sur la vente d'un put
    p1 : la prime du put
    S : le prix du sous-jcent
    Xp : le prix d'exercice
    """
    
    profit = p - max(0, xp - s)
    return profit

#1.6 Cette section définie la stratégie Covered Call
def long_action(s, So):
    return (s - So)

def covered_call(xc, c, s, So):

    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options covered call
    c : la prime du call
    S : le prix du sous-jcent
    Xc : le prix d'exercice
    So: Le prix d'achat initial
    """
    return short_call(xc, c, s) + long_action(s, So)

#1.7 Cette section concerne la stratégie du Protective Put
def protective_put(xp, p, s, So):

    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options protective put
    p : la prime du put
    S : le prix du sous-jcent
    Xp : le prix d'exercice
    So: Le prix d'achat initial
    """
    return long_put(p, s, xp) + long_action(s, So)

#1.8 Cette section concerne la stratégie du Straddle   
def straddle(c, p, s, xc, xp):

    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Straddle
    c : la prime du call
    p : la prime du put
    S : le prix du sous-jcent
    X : le prix d'exercice du call

    """
    return long_call(c, s, xc) + long_put(p, s, xp)

#1.9 Cette section concerne la stratégie du strangle
def strangle(c, p, s, xc, xp):

    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Straddle
    c : la prime du call
    p : la prime du put
    S : le prix du sous-jcent
    Xc : le prix d'exercice du call
    xp : Le prix d'exercice du put
    """
    return long_call(c, s, xc) + long_put(p, s, xp)

#1.10 Cette section définie la stratégie du Long Put qui va être utilisé pour le short put et troisième prix d'exercice du Butterfly Spread
def short_put(xp1, p1, s1):

    """Cette fonction calcule les profits et pertes 
    sur l'achat d'un put
    p1 : la prime (prix) du put
    s1 : le prix du sous-jcent
    xp1 : le prix d'exercice
    """
    profit1 = p1 - max(0, xp1 - s1)
    return profit1

def long_put2(p2, s2, xp2):

    """Cette fonction calcule les profits et pertes 
    sur l'achat d'un put
    p2 : la prime (prix) du put
    s2 : le prix du sous-jcent
    xp2 : le prix d'exercice
    """
    profit2 = -p2 + max(0, xp2 - s2)
    return profit2

#1.11 Cette section concerne la stratégie du Butterfly Spread
def butterfly_spread(xp, s, p, xp1,s1, p1, xp2, s2, p2):

    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Butterfly Spread
    p : la prime du put à 
    S : le prix du sous-jcent
    Xc : le prix d'exercice du call
    xp : Le prix d'exercice du put
    """
    return long_put(p, s, xp) +2*short_put(xp1, p1, s1) + long_put2(p2, s2, xp2)

#1.12 Cette section concerne la stratégie du Bull Call Spread
def bull_call_spread(xc, xc1, c, c1, s):
     
    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Bull Call Spread
    xc : le prix d'exercice du long call
    xc1 : le prix d'exercice du short call
    c : la prime du long call
    c1 : la prime du short call
    s : le prix du sous-jacent
    """
    short_call2 = c1 - max(0, s - xc1)
    return long_call(c, s, xc) + short_call2

#1.13 Cette section concerne la stratégie du Bull Put Spread
def bull_put_spread(xp, xp1, p, p1, s):
     
    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Bull Put Spread
    xp : le prix d'exercice du long put
    xp1 : le prix d'exercice du short put
    p : la prime du long put
    p1 : la prime du short put
    s : le prix du sous-jacent
    """
    short_put2 = p1 - max(0, xp1 - s)
    return long_put(p, s, xp) + short_put2

#1.14 Cette section concerne la stratégie du Bear Call Spread
def bear_call_spread(xc, xc1, c, c1, s):
     
    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Bear Call Spread
    xc : le prix d'exercice du short call
    xc1 : le prix d'exercice du long call
    c : la prime du short call
    c1 : la prime du long call
    s : le prix du sous-jacent
    """
    long_call2 = (-c1 + max(0, s - xc1))
    return short_call(xc, c, s) + long_call2

#1.15 Cette section concerne la stratégie du Bear Put Spread
def bear_put_spread(xp, xp1, p, p1, s):
     
    """Cette fonction calcule les profits et pertes 
    sur une stratégie d'options Bear Put Spread
    xp : le prix d'exercice du short put
    xp1 : le prix d'exercice du long put
    p : la prime du short put
    p1 : la prime du long put
    s : le prix du sous-jacent
    """
    long_put2 = -p1 + max(0, xp1 - s)
    return short_put(xp, p, s) + long_put2

#2 Cette section écrit les bonnes réponses selon le choix de la stratégie
#2.1 Réponse du Straddle
if Option == "Straddle":
    xc = st.number_input(f"Quel est le prix d'exercice du call ?", step=1.00)
    xp = xc
    c = st.number_input(f"Quel est le coût de la prime du Call ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du Put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent? aujourd'hui", step=1.00)
    st.write(f"La valeur du {Option} est de {straddle(c, p, s, xc, xp)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xc or xp or c or p or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [straddle(c, p, s, xc, xp) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Call\n-  1x Long Put\n\nou \n-  1x Short Call\n-  1x Short Put')

#2.2 Réponse du Long Call
elif Option == "Long Call":
    xc = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du Call ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)

#Message d'erreur en cas d'entrée négative
    if (xc or c or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')

    st.write(f"La valeur du {Option} est de {long_call(c, s, xc)}$")
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [long_call(c, s, xc) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(" Fonction de profit d'un Long Call ")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Call')

#2.3 Réponse du Long Put
elif Option == "Long Put":
    xp = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du Put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)

    #Message d'erreur en cas d'entrée négative
    if (xp or p or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')

    st.write(f"La valeur du {Option} est de {long_put(p, s, xp)}$")
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [long_put(p, s, xp) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(" Fonction de profit d'un Long Put ")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Put')

#2.4 Réponse du Short Call
elif Option == "Short Call":
    xc = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du Call ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)

    #Message d'erreur en cas d'entrée négative
    if (xc or c or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')

    st.write(f"La valeur du {Option} est de {short_call(xc, c, s)}$")
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [short_call(xc, c, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(" Fonction de profit d'un Short Call ")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Short Call')

#2.5 Réponse du Short Put
elif Option == "Short Put":
    xp = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du Put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)

    #Message d'erreur en cas d'entrée négative
    if (xp or p or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')

    st.write(f"La valeur du {Option} est de {short_put(xp, p, s)}$") 
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [short_put(xp, p, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(" Fonction de profit d'un Short Put ")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Short Put')

#2.6 Réponse du Covered Call
elif Option == "Covered Call":
    xc = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du Call ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    So = st.number_input(f"Quel est le prix d'achat de l'action", step=1.00)
    st.write(f"La valeur du {Option} est de {covered_call(xc, c, s, So)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xc or c or s or So) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [covered_call(xc, c, s, So) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Short Call\n-  1x Le titre sous-jacent')
    
#2.7 Réponse du Protective Put
elif Option == "Protective Put":
    xp = st.number_input(f"Quel est le prix d'exercice ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    So = st.number_input(f"Quel est le prix d'achat de l'action", step=1.00)
    st.write(f"La valeur du {Option} est de {protective_put(xp, p, s, So)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xp or p or s or So) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [protective_put(xp, p, s, So) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Put\n-  1x Le titre sous-jacent')
        
#2.8 Réponse du Strangle
elif Option == "Strangle":
    xc = st.number_input(f"Quel est le prix d'exercice du call ?", step=1.00)
    xp = st.number_input(f"Quel est le prix d'exercice du put ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du Call ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du Put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    st.write(f"La valeur du {Option} est de {straddle(c, p, s, xc, xp)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xc or xp or c or p or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [straddle(c, p, s, xc, xp) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Call\n-  1x Long Put')
        
#2.9 Réponse du Butterfly Spread
elif Option == "Butterfly Spread":
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    xp = st.number_input(f"Quel est le prix d'exercice du premier Long Put ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du premier Long Put ?", step=1.00)
    xp1 = st.number_input(f"Quel est le prix d'exercice du Short Put ?", step=1.00)
    s1 = s
    p1 = st.number_input(f"Quel est le coût de la prime du short ?", step=1.00)
    xp2 = st.number_input(f"Quel est le prix d'exercice du deuxième Long Put ?", step=1.00)
    s2 = s
    p2 = st.number_input(f"Quel est le coût de la prime du deuxième Long Put ?", step=1.00)
    st.write(f"La valeur du {Option} est de {butterfly_spread(xp, s, p, xp1,s1, p1, xp2, s2, p2)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (s or p or xp1 or s1 or p1 or xp2 or s2 or p2) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [butterfly_spread(xp, s, p, xp1,s1, p1, xp2, s2, p2) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Put à S1\n-  1x Short Put à S2\n-  1x Long Put à S3')
    
    
#2.10 Réponse du Bull Call Spread
elif Option == "Bull Call Spread":
    xc = st.number_input(f"Quel est le prix d'exercice du long call ?", step=1.00)
    xc1 = st.number_input(f"Quel est le prix d'exercice du short call ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du long call ?", step=1.00)
    c1 = st.number_input(f"Quel est le coût de la prime du short call ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    st.write(f"La valeur du {Option} est de {bull_call_spread(xc, xc1, c, c1, s)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xc or xc1 or c or c1 or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [bull_call_spread(xc, xc1, c, c1, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Call à S1\n-  1x Short Call à S2')
    
#2.11 Réponse du Bull Put Spread
elif Option == "Bull Put Spread":
    xp = st.number_input(f"Quel est le prix d'exercice du long put ?", step=1.00)
    xp1 = st.number_input(f"Quel est le prix d'exercice du short put ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du long put ?", step=1.00)
    p1 = st.number_input(f"Quel est le coût de la prime du short put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    st.write(f"La valeur du {Option} est de {bull_put_spread(xp, xp1, p, p1, s)}$")
   
    #Message d'erreur en cas d'entrée négative
    if (xp or xp1 or p1 or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [bull_put_spread(xp, xp1, p, p1, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Long Put à S1\n-  1x Short Put à S2')
    
#2.12 Réponse du Bear Call Spread
elif Option == "Bear Call Spread":
    xc = st.number_input(f"Quel est le prix d'exercice du short call ?", step=1.00)
    xc1 = st.number_input(f"Quel est le prix d'exercice du long call ?", step=1.00)
    c = st.number_input(f"Quel est le coût de la prime du short call ?", step=1.00)
    c1 = st.number_input(f"Quel est le coût de la prime du long call ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    st.write(f"La valeur du {Option} est de {bear_call_spread(xc, xc1, c, c1, s)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xc or xc1 or c or c1 or s) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [bear_call_spread(xc, xc1, c, c1, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Short Call à S1\n-  1x Long Call à S2')
    
#2.13 Réponse sur Bear Put Spread
elif Option == "Bear Put Spread":
    xp = st.number_input(f"Quel est le prix d'exercice du short put ?", step=1.00)
    xp1 = st.number_input(f"Quel est le prix d'exercice du long put ?", step=1.00)
    p = st.number_input(f"Quel est le coût de la prime du short put ?", step=1.00)
    p1 = st.number_input(f"Quel est le coût de la prime du long put ?", step=1.00)
    s = st.number_input(f"Quel est le prix du sous-jacent aujourd'hui ?", step=1.00)
    st.write(f"La valeur du {Option} est de {bear_put_spread(xp, xp1, p, p1, s)}$")
    
    #Message d'erreur en cas d'entrée négative
    if (xp or xp1 or s or p or p1) < 0:
        st.warning('Les valeurs ne peuvent pas être négative')
    
    valeurs = np.linspace(0, 2*s, 40)
    profits_achats = [bear_put_spread(xp, xp1, p, p1, s) for s in valeurs]
    fig, ax = plt.subplots(facecolor = "grey")
    ax.plot(valeurs, profits_achats, color = theme)
    ax.set_xlabel('Prix du sous-jacent ($)', color = 'k')
    ax.set_ylabel('Profit ($)', color = 'k')
    ax.set_title(f" Fonction de profit d'un {Option}")
    
    plt.grid()
    st.pyplot(fig)
    
    #Zone de texte qui identifie la composition de la stratégie
    with col2:
        st.write('Cette stratégie se compose de:')
        st.write('-  1x Short Put à S1\n-  1x Long Put à S2')
   


#Cette section consiste à ajouter la section don de notre site
st.subheader(f"\n:green[*** Faites dès aujourd'hui un don pour soutenir notre page ainsi que des étudiants démunis ***]")

if st.button('👏👏Faire un don via PayPal👏👏'):
    st.balloons()
    st.success('Merci de votre générosité !')
    st.write(f'''
    <a target="_self" href="https://www.paypal.com/signin">
        <button>
            100$
        </button>
        <button>
            200$
        </button>
        <button>
            500$
        </button>
        <button>
            1000$
        </button>
        <button>
            Chèque en blanc électronique
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)

    
    
    
    







