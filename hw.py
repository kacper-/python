from langchain_community.llms import Ollama
ollama = Ollama(model="phi")
print(ollama.invoke("why is the sky blue"))