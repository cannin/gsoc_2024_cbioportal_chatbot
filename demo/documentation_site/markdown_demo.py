from langchain_community.document_loaders import DirectoryLoader
import os
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser
import gradio as gr
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_core.runnables import RunnableLambda
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


load_dotenv()
_ = load_dotenv(find_dotenv())  # read local .env file

#Azure_OpenAI llm    
llm_azure = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"], 
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION_4"],
    deployment_name=os.environ["DEPLOYMENT_NAME_4"],
    openai_api_type=os.environ["AZURE_OPENAI_API_TYPE"]
)

embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.environ["DEPLOYMENT_NAME_EMBEDDING"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION_4"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

# vectordb = Chroma.from_documents(
#     documents=raw_documents,
#     embedding=embeddings,
#     persist_directory="vectordb/chroma/markdown"
# )
# vectordb.persist()
vectordb = Chroma(persist_directory="demo/vectordb/chroma/markdown", embedding_function=embeddings)


# self-query retriever
document_content_description = "documentation site of cBioportal "
metadata_field_info = [
    AttributeInfo(
        name="url",
        description="The url for document_content",
        type="string",
    )
]
SelfQuery_Retriever = SelfQueryRetriever.from_llm(
    llm_azure,
    vectordb,
    document_content_description,
    metadata_field_info,
    search_kwargs={'k': 3}
    # search_type="mmr"
)

# retriever = vectordb.as_retriever(k=3)

# build prompt template
ANSWER_PROMPT = """You are a professional assistant.
                Answer the question based only on the following context and chat history, "
                and return the url of all the contexts :

                Do not return source of contexts
{context}
Question: {question}
"""


prompt = ChatPromptTemplate.from_template(ANSWER_PROMPT)


def get_documentation_site_chain():
    chain = (
        RunnableLambda(lambda x: x['question']) |
        {"context": SelfQuery_Retriever, "question": RunnablePassthrough()} 
        | prompt  # choose a prompt
        | llm_azure  # choose a llm
        | StrOutputParser()
    )
    return chain



