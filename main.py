import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import UnstructuredFileLoader, CSVLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.agents import Tool
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
import gradio as gr
import pandas as pd
from langchain.document_loaders import UnstructuredFileLoader, PyPDFLoader, WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langgraph.prebuilt import create_react_agent
from langchain.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key="AIzaSyC6TmVb5Vk5J0r6z0oCmjvNgzbblDKuf3Y",
    # other params...
)

template = """
Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question:
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""
prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)
cross_systhesis_prompt="""
you are an expert in analyzing a brand documents and after that you will answer the any user questions like a moderator for that brand 

"""
qa = None
summaries = []

def vector(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", 
        google_api_key="AIzaSyC6TmVb5Vk5J0r6z0oCmjvNgzbblDKuf3Y"
    )
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory
    )
    return qa_chain

def url(link):
    global qa
    loader = WebBaseLoader(link)
    docs = loader.load()
    qa = vector(docs)
    return "Link uploaded and processed successfully!"
    

def file_upload(file):
    global qa
    if file.name.endswith('.pdf'):
        loader = PyPDFLoader(file.name)
    elif file.name.endswith('.docx') or file.name.endswith('.txt'):
        loader = UnstructuredFileLoader(file)
    else:
        return "Unsupported file type."

    documents = loader.load()
    qa = vector(documents)
    answer = qa.run("Give a title and summarize the document in 5-6 lines.")
    summaries.append(answer)
    return answer

def chat_bot_interface(message, history):
    if qa is None:
        return "Please upload a document or URL first."
    return qa.run(message)

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Document Summarizer & Chatbot")

    with gr.Tabs():
        with gr.Tab("Upload Document"):
            with gr.Row():
                with gr.Column():
                    file_input = gr.File(label="Upload your document")
                    file_input.change(fn=file_upload, inputs=file_input, outputs=None)

        with gr.Tab("Upload the Link"):
            with gr.Row():
                with gr.Column():
                    link_input = gr.Textbox(label="Enter the URL")
                    link_output = gr.Textbox(label="Link Status")
                    search_button = gr.Button("Submit", variant="primary")
                    search_button.click(fn=url, inputs=link_input, outputs=link_output)  # FIXED LINE

        with gr.Tab("Chat with Document"):
            gr.Markdown("Ask questions based on the uploaded document or URL.")
            gr.ChatInterface(
                fn=chat_bot_interface,
                chatbot=gr.Chatbot(),
                title="Chat with Your Document",
                textbox=gr.Textbox(
                    placeholder="Ask something about the document...",
                    lines=1,
                    label="Your question"
                )
            )

demo.launch(debug=True)
