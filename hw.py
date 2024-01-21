from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import warnings

question=input("Ask:\n")

ollama = Ollama(model="orca-mini:3b")

loader = PyPDFLoader("/Users/kacper/Downloads/Kacper.pdf")
data = loader.load_and_split()

oembed = OllamaEmbeddings(model="orca-mini:3b")
vectorstore = Chroma.from_documents(documents=data, embedding=oembed)

docs = vectorstore.similarity_search(question)

with warnings.catch_warnings(action="ignore"):
    qachain=RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
    response=qachain({"query": question})

print(response['result'].strip())

