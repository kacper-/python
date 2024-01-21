from langchain_community.llms import Ollama
from langchain_community.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader("/Users/kacper/Downloads/Kacper_Marczewski.pdf", mode="elements")
data = loader.load()

ollama = Ollama(
    model="phi",
    system="you are helpful AI that gives answers as short as possible"
    )

print(ollama.invoke("what is capital city of Poland"))