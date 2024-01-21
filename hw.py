from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

ollama = Ollama(model="orca-mini:3b")

loader = PyPDFLoader("/Users/kacper/Downloads/Kacper.pdf")
data = loader.load_and_split()

oembed = OllamaEmbeddings(model="orca-mini:3b")
vectorstore = Chroma.from_documents(documents=data, embedding=oembed)

question="Does Kacper from Netherlands have cats?"
docs = vectorstore.similarity_search(question)

print()
print("DOCS ----------------")
print()
print(docs)

qachain=RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
print()
print()
print(qachain({"query": question}))

