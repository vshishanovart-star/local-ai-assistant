# Local AI Assistant

## Overview

Local AI Assistant is a Python-based AI workstation that integrates local language models, task routing, prompt generation, memory, and external AI tools into a single workflow.

The project is designed to help users work with AI locally without relying on cloud services.

## Key Features

### AI Task Router

Automatically analyzes a user task and selects the most appropriate tool.

Supported tools:

* Chat
* File Analyzer
* Project Overview
* Image Generation
* Text-to-Speech (TTS)

### Prompt Generation

Generates structured prompts for AI tools.

Examples:

* Image generation prompts for ComfyUI
* Speech generation prompts for Qwen3-TTS

### Memory System

The assistant stores:

* task history
* prompts
* session results
* summaries
* successful executions

and can reuse previous experience when solving similar tasks.

### Session Management

The system tracks:

* current task
* current prompt
* completed tasks
* successful results

All sessions are stored locally in JSON format.

### AI Ecosystem Integration

Integrated with:

* Ollama
* ComfyUI
* Qwen3-TTS
* Open WebUI

### Project Analytics

Provides:

* project overview
* recent tasks
* memory statistics
* tool usage statistics
* project reports

---

## Architecture

Task

↓

Task Router

↓

Tool Selection

↓

Prompt Builder

↓

Tool Executor

↓

Result

↓

Summary Generator

↓

Session Memory

---

## Technologies

* Python
* Ollama
* Local LLMs
* ComfyUI
* Qwen3-TTS
* Open WebUI
* Git
* JSON-based memory system

---

## Project Structure

Main modules:

* assistant_menu.py
* task_router.py
* task_prompt_builder.py
* tool_executor.py
* session_memory.py
* task_session.py
* complete_task.py
* experience_score.py
* ai_memory_chat.py

---

## Running

Clone repository:

git clone <repository>

Open project folder:

cd local-ai-assistant

Run:

py start.py

---

## Current Status

Version: v0.6

Implemented:

* Task routing
* Prompt generation
* Tool execution
* Session memory
* Experience tracking
* Current task tracking
* Current prompt tracking
* Project reporting

---

## Future Plans

* Automatic ComfyUI workflow execution
* Automatic result collection
* Multi-agent workflows
* Local AI workstation dashboard
* Freelance-oriented automation tools

---

## Author

Personal educational and portfolio project focused on local AI workflows, automation, and practical AI tooling.
