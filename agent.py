from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialisation du modèle Ollama local
# (Remplacez "gemma2" par le nom du modèle que vous avez téléchargé, ex: "llama3")
llm = Ollama(model="gemma2")

# Gestion de la mémoire pour que l'agent se souvienne de la discussion
memory = ConversationBufferMemory()

# Création de la chaîne de conversation
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def repondre_a_l_utilisateur(message_utilisateur: str) -> str:
    """
    Fonction appelée par app.py pour transmettre le message 
    à l'agent et récupérer sa réponse.
    """
    reponse = conversation.predict(input=message_utilisateur)
    return reponse
