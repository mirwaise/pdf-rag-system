
from pypdf import PdfReader
import re
import chromadb
from groq import Groq

reader=PdfReader('sample_resume.pdf')

all_text=''
for page in reader.pages:
    text=page.extract_text()
    if text:
        all_text+=text + '\n'
clean_text=re.sub(r'\s',' ',all_text)

chunks=[
    chunk.strip()
    for chunk in clean_text.split('.')
    if chunk.strip() 
]

ids=[str(i) for i in range(len(chunks))]

client=chromadb.PersistentClient('./path')
collection=client.get_or_create_collection(name='my_documents')
collection.add(
    documents=chunks,
    ids=ids
)
print(collection.count())

question=input("What is your question: ")
result=collection.query(
    query_texts=[question],
    n_results=2
)

context="\n".join(result['documents'][0])
prompt=f"""
You are a helpful assistant.

Use only the provided context.

If the answer is not in the context, say:
"I could not find that information in the document."
Context:
{context},

Question:
{question}

Answer:
"""
groq_client=Groq(api_key='Your_api_key')
response=groq_client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[{
        'role':'user',
        'content':prompt
    }]
)
print(response.choices[0].message.content)




