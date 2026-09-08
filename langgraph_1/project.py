import os 
from typing import TypedDict 

#Lets create the state first 

class pipelinestate(TypedDict):
    raw_input:str 
    edited_text:str
    script_text:str
    final_output:str 

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)

def editor_node(state:pipelinestate)->dict:
    """Stage 1: Clenas up grammar,removes typos,and refines the tone"""

    prompt=(
        "You are an expert copyeditor.Clean up the following raw text"
        "Fix any grammatical errors, spelling mistakes, and smooth out the transition  flow"
        "while keeping hte core message intact. Return only the edited text.\n\n"
        f"Text:\n{state['raw_input']}"
    )
    response = llm.invoke(prompt)

    return {"edited_text":response.content.strip()}

def scriptwriter_node(state:pipelinestate)->dict:
    """Stage 2:Formats the clean text ionto an engaging video script style."""
    print("\n--- [stage 2] Executing Scriptwriter Node ---")

    prompt=(
        "You are a charismatic YoutTube content creator. Take this edited text and transform"
        "it into a highly engaging,punchy,conversational video script hook. Make it sound"
        "like a real person speaking passionately. Return only the script content.\n\n"
        f"Edited_text:\n{state['edited_text']}"
    )
    response = llm.invoke(prompt)
    return {"script_text":response.content.strip()}

def translator_node(state:pipelinestate)->dict:
    """Stage 3:Translates the script into natural flowing Banglish"""
    print("\n--- [stage 3] Executing Translator Node ---")

    prompt=(
        "You are an expert content localizer for the Bangladesh Market.Tale the following script"
        "and convert it into a natural,flowing 'Banglish'. Do not simply translate it sentence by sentence"
        "or repeat information. Alternating comfortably between Bangla and English"
        "an Intellectual tech educator woudl speak aturally on a live stream"
        "Return only the final Banglish text.\n\n"
        f"Script:\n{state['script_text']}"
    )
    response = llm.invoke(prompt)
    return {"final_output":response.content.strip()}

#up and until this point the nodes and the state are ready now we have to create the graph 
#for creating the grpah we have to connect this nodes , for that we have to use the edges
#edges are very important for creating the graphs 

from langgraph.graph import StateGraph,START,END

#create the graph 
graph = StateGraph(pipelinestate)

#add the nodes in our graph 
graph.add_node("editor",editor_node)
graph.add_node("scriptwriter",scriptwriter_node)
graph.add_node("translator",translator_node)

#add edhes to the graph (sequential - one after another)

graph.add_edge(START,"editor")
graph.add_edge('editor',"scriptwriter")
graph.add_edge('scriptwriter',"translator")
graph.add_edge('translator',END)

#compile the graph 
app = graph.compile()

result = app.invoke({
    "raw_input":"Ai agents are the future of tech. They can think,plan,and act on their own"
})

#output 
print("Here is your result - \n")
print(result['final_output'])
