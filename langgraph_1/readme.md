# LangGraph AI Workflow Collection

This repository is a practical learning space for building agentic workflows with Python, LangGraph, LangChain, Groq, and retrieval-based AI patterns. It is designed to show how LLM applications are not just single prompts, but structured systems where tasks move through a graph of nodes, share state, branch, and combine results.

The projects here are intentionally small and beginner-friendly, but they cover the core patterns used in real agentic AI systems:

- linear workflows
- parallel branches
- tool use
- review-and-rewrite loops
- conditional routing
- RAG-based document retrieval
- state-driven orchestration

---

## Repository Structure

The repo contains the following major projects:

- `sequential.py` — linear multi-stage content transformation workflow
- `parallel_reducer.py` — parallel branch execution with final aggregation
- `linkedin_post_generator.py` — LinkedIn post writer with review loop and web search
- `conditrional_RAG.py` — conditional retrieval-augmented generation for academic and fee queries

---

## What This Repo Teaches

This repo focuses on the real building blocks of agentic systems:

1. State management with `TypedDict`
2. Shared memory passed between nodes
3. Node-based task execution
4. Explicit graph edges between nodes
5. Conditional branching depending on runtime state
6. LLM tool calling
7. Retrieval using vector databases
8. Controlled loops for iterative improvement
9. Restructuring AI behavior as workflows instead of one-off prompts

The main idea is simple:

- an LLM task is broken into smaller functions
- each function becomes a node
- the graph decides the flow between nodes
- state carries all necessary data forward

This is the core LangGraph thinking pattern.

---

## Core LangGraph Concepts Used in This Repo

### 1. State
Every workflow uses a `TypedDict` or structured state object. This keeps relevant data in one place.

Example idea:
```python
class State(TypedDict):
    topic: str
    messages: Annotated[list, add_messages]
    draft: str
    review_feedback: str
    is_approved: bool
    attempt: int
```

This is important because:
- different nodes read from the same state
- nodes update pieces of it
- the graph flows based on the state values

---

### 2. Nodes
Each node is a function that receives the current state and returns an updated dictionary.

Example:
```python
def editor_node(state):
    edited = ...
    return {"edited_text": edited}
```

A node may:
- call an LLM
- use tools
- retrieve documents
- classify user intent
- validate output

---

### 3. Edges
Edges define how execution moves from one node to another.

Example:
```python
graph.add_edge(START, "writer")
graph.add_edge("reviewer", END)
```

This creates a clear flow.

---

### 4. Conditional Routing
Some graphs do not always follow the same path. A router decides which node should run next.

Example:
```python
def route_query(state):
    if state["query_type"] == "academic":
        return "academic_rag"
    elif state["query_type"] == "fee":
        return "fee_rag"
    else:
        return "general"
```

This is the heart of a conditional workflow.

---

### 5. Tool Calling
Some nodes can invoke tools such as:
- web search
- external document lookup
- APIs
- data retrieval systems

This is how an LLM can move beyond static prompt generation and interact with real-world resources.

---

### 6. Loops and Iteration
Some workflows improve output over multiple attempts.

Example pattern:
- draft
- review
- reject and revise
- try again until approved or max attempts reached

This is the same principle behind self-checking or agentic correction loops.

---

## Project 01 — Sequential Content Pipeline

File: `sequential.py`

This is the first and simplest workflow in the repo. It demonstrates a linear chain of transformations:

```text
START -> editor -> scriptwriter -> translator -> END
```

### Purpose
The system takes a raw input and transforms it through multiple stages:
1. grammar and text polishing
2. script-like narrative conversion
3. Banglish/localized final output

### State Structure
The shared state typically includes:
- `raw_input`
- `edited_text`
- `script_text`
- `final_output`

### Node Responsibilities
- `editor_node`: improves grammar and flow
- `scriptwriter_node`: rewrites in a script-like voice
- `translator_node`: converts the result into Banglish

### Why It Matters
This project introduces the basic LangGraph model:
- create a state
- define nodes
- connect them in order
- pass data through the state
- use LLMs in multi-step sequence

It is the foundation for all later workflows in the repo.

---

## Project 02 — Parallel Reducer Workflow

File: `parallel_reducer.py`

This introduces branching and aggregation.

### Flow
```text
START -> branch_1 -> reduce
START -> branch_2 -> reduce
START -> branch_3 -> reduce
reduce -> END
```

### Purpose
Instead of a single linear process, multiple nodes run concurrently, each generating a different perspective or answer. Then a reducer node combines them into one final output.

### Why It Matters
This teaches:
- parallel node execution
- multiple worker agents or expert roles
- final synthesis from multiple outputs
- multi-perspective reasoning

### Real-World Use
This pattern is useful when:
- different specialists answer the same question
- multiple drafts are created from different angles
- a final answer should merge multiple expert outputs

This is a classic agentic workflow design.

---

## Project 03 — LinkedIn Post Generator

File: `linkedin_post_generator.py`

This project is a more advanced agentic workflow that writes a LinkedIn post, reviews it, and improves it until it meets the standards.

### Workflow Pattern
```text
START -> writer -> (tool? or extract_draft) -> reviewer -> if approved END else writer
```

### What It Does
The workflow:

1. takes a topic from the user
2. writes a LinkedIn post
3. optionally calls Tavily search if fresh facts are needed
4. extracts the generated draft
5. sends the draft to a reviewer LLM
6. checks if the post is publish-ready
7. if rejected, rewrites it with feedback
8. loops until approved or max attempts reached

### Important Design Choices
This project teaches many real agentic patterns:

- tool use for web search
- LLM-as-reviewer pattern
- iterative feedback loops
- state-based retry logic
- reviewer evaluation against a checklist
- controlled improvement process

### State
The state includes:
- `topic`
- `messages`
- `draft`
- `review_feedback`
- `is_approved`
- `attempt`

### Node Types
- `writer_node`: creates or revises the post
- `ToolNode`: executes web search through Tavily
- `extract_draft_node`: pulls the final content from the latest message
- `reveiwer_node`: validates whether the content is ready

### Routing Logic
The workflow uses conditional logic:

- if the writer generated tool calls -> use tools
- otherwise -> extract the draft
- after reviewing:
  - if approved -> stop
  - if attempt limit reached -> stop
  - else -> go back to writer

### Why This Project Is Important
This is a very realistic pattern for:
- content generation systems
- AI editorial workflows
- post-drafting assistants
- self-checking and refinement loops

It goes beyond simple prompting and demonstrates actual agent workflow architecture.

---

## Project 04 — Conditional RAG Assistant

File: `conditrional_RAG.py`

This project is built around retrieval-augmented generation and conditional routing.

### Workflow Pattern
```text
START -> classifier -> academic_rag / fee_rag / general -> response -> END
```

### What It Does
The system receives a student question and decides which knowledge path to use:

- `academic` questions -> use academic handbook retrieval
- `fee` questions -> use fee structure retrieval
- `general` questions -> answer without retrieval

This is an example of a domain-aware RAG workflow.

### Why It Matters
This is one of the most important agentic patterns in production AI:

- classify the user request
- pick the right source of knowledge
- retrieve only relevant context
- generate a grounded answer

### Retrieval Setup
The workflow loads PDFs and builds separate retrievers:

- academic handbook PDF
- fee structure PDF

Using:
- `PyPDFLoader`
- `RecursiveCharacterTextSplitter`
- `FAISS`
- `HuggingFaceEmbeddings`

This creates vector databases for semantic search.

### Node Responsibilities
- `classifier_node`: decides if the question is academic, fee, or general
- `academic_rag_node`: retrieves relevant chunks from the academic PDF
- `fee_rag_node`: retrieves relevant chunks from the fee PDF
- `general_node`: handles non-document questions directly
- `response_node`: produces final answer with proper context

### Why This Is a Proper RAG Workflow
This demonstrates how retrieval should be used properly:
- not every question needs retrieval
- retrieval is selected based on intent
- documents are chunked and embedded
- relevant snippets are injected before final response generation
- results are tailored to a specific student program

This is how real AI assistants often do grounding.

---

## Setup and Environment

This repo expects the following dependencies:

- Python
- LangGraph
- LangChain
- Groq LLM access
- Tavily Search
- FAISS
- Hugging Face embeddings
- `python-dotenv`

### Environment Variables
Create a `.env` file in the project root with values such as:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

These are needed for:
- Groq-based LLM inference
- Tavily web search for the LinkedIn workflow

---

## Example Run Commands

From the project root:

```bash
python sequential.py
python parallel_reducer.py
python linkedin_post_generator.py
python conditrional_RAG.py
```

---

## How the Repo Is Structured as a Learning Path

This repository is intentionally organized in increasing complexity:

1. Basic state-based sequential workflow
2. Parallel branching and reduction
3. Writing + review + rewrite agent loop
4. Retrieval + routing + grounding with RAG

This progression helps you understand how AI systems evolve from:
- a single prompt
- to a workflow
- to a multi-node agent
- to a grounded assistant

---

## The Bigger Design Idea

The repo is not just about “calling an LLM” in one script. It is about designing systems where:

- each task is given a purpose
- state becomes the memory of the workflow
- nodes transform information
- edges decide how work moves
- conditionals decide which branch is needed
- tools extend the model beyond its own context
- review loops increase reliability

This is the foundation of agentic AI design.

---

## Summary

This repo contains four important LangGraph learning projects:

- `sequential.py` — a simple linear multi-step pipeline
- `parallel_reducer.py` — parallel workflow with result aggregation
- `linkedin_post_generator.py` — tool-using writer + reviewer loop
- `conditrional_RAG.py` — routed and grounded retrieval system

Together, they show the core patterns behind real-world agentic systems:

- state-driven orchestration
- branches and merges
- tool use
- review loops
- retrieval and grounding
- decision-making workflows

This makes the project a solid starting point for anyone learning how to build structured AI workflows with LangGraph.

---

## Final Learning Outcome

By the end of this repo, you should understand:
- how to define state in LangGraph
- how to build nodes and edges
- how to route flow conditionally
- how to build workflows for generation, review, and retrieval
- how to create small but realistic AI agents

The repo is small, but the design principles are foundational for larger and more advanced agent systems.