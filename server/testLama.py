import dotenv
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

config = dotenv.dotenv_values("./.env")
os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEY']

while(input != 'quit'):
    documents = SimpleDirectoryReader('./server/store').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    input = input("Enter your question : ")
    response = query_engine.query(input)
    print(response)