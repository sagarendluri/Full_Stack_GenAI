Table of Content:

Install & Import Dependencies
Load Documents 
Transformer Documents
Generate Text Embeddings
Vector store - Chroma
Retrieve Answers
Structure the Output



Install & Import Dependencies: please make sure all necessary modules are installed. 
Loads PDF files available in my(your) directory with pypdf ( as for now, we are uploading only pdf , later will develop the AI app for all)
Pypdf, is going to read all the files and it break them down into chunks, for to feed the model 
convert those chunks(segments) into embeddings(numbers) such as the numerical representation 
of this documents using sentence_transformer, which then will be stored into the Chroma Vector 
database)
Once we have this information, the end-user comes up and he give a query in the form of the text or anything, for which we will try to again have the emeddings and take it straight forward into Chroma vector store, to perform semantic search.
Once we are done with the semantic search, we might have the relevant documents that are very close to the question, so that also you can provide.
Once, we are ready with this information along with the query , passed to the Mistral-7b.
From there we will get an output from Mitral-7b

<img width="803" alt="Screenshot 2024-06-04 at 3 50 40 PM" src="https://github.com/sagarendluri/Full_Stack_GenAI/assets/56343742/432ab411-559e-4a81-a64f-fc3990a116f2">
# Full_Stack_GenAI
<img src="https://t.bkit.co/w_665f37db00d1f.gif" />
Built a LLM of Mistral7b-based chat with text by using my full-stack AI skills at work. On top of that, I recently created a prototype using the Streamlit API (module).
