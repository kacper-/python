from langchain_community.llms import Ollama

ollama = Ollama(
    model="phi",
    system="you are helpful AI giving short answers"
    )

print(ollama.invoke("what is capital city of Poland"))