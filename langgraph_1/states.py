#we are creating a graph over here 
#and the first thing we create is a state 

import os 


#1) typed DICT 
from typing import TypedDict

class State(TypedDict):
    topic: str
    summary: str 
    scoire: str

#2) pydantic approach 
#it is good at data validation and type chekcing at runtime 

from pydantic import BaseModel,field_validator

class State(BaseModel):
    topic:str 
    score:int 
    summary: str = "" 

    @field_validator 
    def score_positive(cls,v):
        if v<0:
            raise ValueError("Score must be positive")


#3) pythonb data classes 
#standard python dataclasses but it is used very rarely 

from dataclasses import dataclass, field 

@dataclass 
class State:
    topic:str=""
    summary: str=""
    messages:list = field(default_factory=list)


#4)by using the state that comes by default from langgraph itself 

from langgraph.graph import MessagesState

class State(MessagesState):
    #messges field is already included with add_messages reducer 
    #just add the extra fields 
    user_naem:str 
    language: str