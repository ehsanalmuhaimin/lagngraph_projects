# LangGraph AI Workflow Collection

This project is a small learning and experimentation space for building agentic AI workflows with Python, LangGraph, LangChain, and Groq LLM models. The goal is to understand how LLM pipelines can be designed as graphs where tasks move from one node to another through explicit edges.

We started by building two working examples:

1. `sequential.py` — a linear content transformation workflow
2. `parallel_reducer.py` — a parallel workflow that runs multiple branches and reduces the results into one final answer

More projects will be added in the same learning track, and this README keeps space for the next ideas.

---

## Project 01 — Sequential Content Pipeline

File: `sequential.py`

This is the first project and the simplest example of a LangGraph state machine.

### What the project does

The system receives a raw input, then passes it through three specialized stages:

1. `editor_node`
   - Cleans grammar and spelling
   - Fixes language flow
   - Returns a polished edited version of the raw input

2. `scriptwriter_node`
   - Converts the cleaned text into a colorful script format
   - Makes the message sound more like an engaging spoken script

3. `translator_node`
   - Converts the script into natural Banglish
   - Makes the final output feel local and friendly for a Bangladeshi audience

### State

The shared state is a `TypedDict` called `pipelinestate` with these fields:

- `raw_input`
- `edited_text`
- `script_text`
- `final_output`

### Graph Flow

The graph is created using `StateGraph` and connected like this:

```text
START -> editor -> scriptwriter -> translator -> END
```

This creates a strict linear workflow, where each stage waits for the previous one to finish before beginning.

### Learning Outcome

This example teaches the basics of:

- creating a LangGraph state
- defining nodes
- connecting nodes with edges
- invoking an LLM in a multi-step workflow
- passing output from one node to the next through the state object

---

## Project 02 — Parallel Reducer Workflow

File: `parallel_reducer.py`

This is the second example and introduces a different graph design: parallel execution.

### What the project does

Instead of using one long sequence of instructions, the workflow splits work into multiple branches. Each branch processes the same or similar input independently, and then the outputs are merged or reduced to a final result.

This type of design is useful when:

- multiple expert roles need to generate answers at the same time
- multiple branches work on different angles of the same problem
- a single final answer should be created by combining different outputs

### Graph Style

The logic in this project represents a workflow where:

```text
START -> branch_1 -> reduce
START -> branch_2 -> reduce
START -> branch_3 -> reduce
reduce -> END
```

In other words:

- the graph starts from one point
- multiple worker nodes run in parallel
- a reducer or final node collects the partial outputs
- the final result is returned as one combined answer

### Learning Outcome

This example teaches the basics of:

- branching in LangGraph
- parallel node execution
- reducer-style final aggregation
- building workflows that do not only move in one straight line
- designing multi-perspective reasoning systems

---

## Why this project matters

This repository is meant to be a training path for understanding how agentic workflows can be built with LangGraph.

From the beginning, the focus is not only on “calling an LLM,” but on:

- shaping the task into nodes
- moving data through a state object
- deciding when tasks should run sequentially or in parallel
- combining expert roles into a working graph
- designing the flow of information in a structured way

---

## Project 03 — Coming Soon

This section is reserved for the next project in the series.

The next project will extend the workflow idea further with another real-world pattern, such as:

- a routing workflow
- an agentic multi-tool workflow
- a reflection and validation pattern
- a more advanced chain of reasoning

Space is intentionally kept open for this project.

---

## Project 04 — Coming Soon

This section will document a future workflow that goes beyond the basic sequential and parallel examples.

Possible directions include:

- customer support or chatbot automation
- content generation and audience targeting
- multi-stage research and summarization
- evaluation and quality-checking using LLMs

Space is reserved for this project.

---

## Project 05 — Coming Soon

This section will hold the next advanced LangGraph project.

This may include:

- agent routing
- memory and context layers
- human-in-the-loop workflows
- external tool use
- reusable graph architecture

This repository is designed to grow naturally as more projects are added.

---

## Tools and Libraries

The examples in this repository use:

- Python
- LangGraph
- LangChain
- Groq LLM integration
- `TypedDict` state structure
- `dotenv` for environment configuration

---

## Project Goals

These projects aim to show how to:

- organize reasoning into graph nodes
- move data with a shared state
- run LLM tasks in different workflow shapes
- build small AI pipelines that are easy to understand and extend
- prepare for more complex agentic systems in future projects

---

## Summary

This repository starts with two simple but important ideas:

- a sequential LLM text transformation pipeline in `sequential.py`
- a parallel branch and reducer workflow in `parallel_reducer.py`

The repository will continue with additional LangGraph-based projects that build on these same principles.