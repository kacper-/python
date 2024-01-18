from langchain_community.llms import Ollama
ollama = Ollama(base_url='http://localhost:11434', model="phi")
print(ollama("why is the sky blue"))