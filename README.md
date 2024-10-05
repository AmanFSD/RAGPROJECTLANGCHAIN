This proect implements a question-answering system that reads a PDF, processes its contents, and generates answers based on user queries. It uses LangChain’s PDF loader, OpenAI embeddings, and FAISS for fast document retrieval. The user can interact with the system via a simple menu to ask questions, and the code combines the question with context from the PDF to generate responses using an OpenAI model.

put your  openai api keys in .env file using the link https://platform.openai.com/api-keys
for windows on the terminal
run these commands

python -m venv env
env\Scripts\activate
pip install -r requirements.txt 
python main.py

for mac on the terminal
run these commands

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 main.py

![sample_output](sample_output.png)