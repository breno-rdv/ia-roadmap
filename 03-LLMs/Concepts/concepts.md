# Concepts
This topic reviews the main concepts of LLMs

## Foundation Model
It is a large-scale model trained on massive, diverse data that can be adapted to many downstream tasks.

**Key characteristics:**
- Trained on broad data
- Very large (billions+ parameters)
- General-purpose
- Adaptable (fine-tuning, RAG, prompting, LoRA)

**Foundation models can be:**
- Text models
- Image models
- Audio models
- Multimodal models

**Examples:**
- OpenAI GPT models
- Anthropic Claude
- Stability AI Stable Diffusion (image model)

> Notice: Stable Diffusion is not an LLM — but it is a foundation model.

# LLM (Large Language Models)

Large Language Models (LLMs) are foundation models specialized in understanding and generating natural language. They are a core component of text-based Generative AI and are widely used for:
- Code generation
- Summarization
- Translation
- Question answering
- Conversational agents

> LLMs are based on the Transformer architecture, which uses self-attention mechanisms to learn patterns in text and predict the next token in a sequence.

They are general-purpose models and can be adapted for specific tasks using:
- Fine-tuning
- RAG (Retrieval-Augmented Generation)
- LoRA (Low-Rank Adaptation)

**Core Concepts**
_Tokens_ – basic units of text processed by the model
_Embeddings_ – dense vector representations of tokens
_Weights_ – learned parameters of the neural network
_Context Window_ – maximum number of tokens the model can process at once