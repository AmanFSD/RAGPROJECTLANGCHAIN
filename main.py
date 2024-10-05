from dotenv import load_dotenv
from langchain.chains import RetrievalQA

from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from colorama import Fore
import os
import warnings 

warnings.filterwarnings("ignore")

# LOAD ENV VARIABLES
load_dotenv()

# Load the model
model = ChatOpenAI()

# Load the PDF
pdf_path = "ProjectTopics.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# prompt templates
template = """You're professor {question} based on your knowledge and {context}
"""
prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"])

# RETRIEVER - Load embeddings and create a vector store 
embeddings = OpenAIEmbeddings() 
db = FAISS.from_documents(documents, embeddings)

# GENERATE - Define the function to generate the response
def generate(query: str):
    chain_type_kwargs = {"prompt": prompt}
    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=db.as_retriever(search_kwargs={"k": 1}),
    )
    
    return chain.run(query)


def start():
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Ask a question")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:

            response = generate(user_input)

            print(Fore.BLUE + f"A: " + response + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()