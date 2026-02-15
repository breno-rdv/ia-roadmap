# Architectures

LLMs use transformer-based architectures. Main patterns and variants:

## Core patterns
- Decoder-only (autoregressive, e.g., GPT): next-token prediction, causal masking, used for open-ended generation and chat.
- Encoder-decoder (seq2seq, e.g., T5, BART): denoising / translation style training, strong for conditional generation and tasks requiring input->output mapping.
- Encoder-only (e.g., BERT): bidirectional representations for understanding tasks; not generative by itself but used in mixed pipelines.

## Common extensions & variants
- Mixture-of-Experts (MoE): sparse routing for very large models with conditional computation.
- Retrieval-augmented (RAG): external knowledge retrieval + generator for up-to-date and factual outputs.
- Memory / cache augmented: long-term state or key-value memory to extend context beyond token window.
- Multimodal transformers: fuse text with images/audio (CLIP, Flamingo, GPT‑4 multimodal).
- Long-context / sparse-attention models: Longformer, Reformer, Performer, etc., to scale context with reduced complexity.
- Efficient attention (FlashAttention, grouped/multi-query): speed and memory optimizations for training/inference.

## Architectural building blocks
- Self-attention (Q/K/V), multi-head attention
- Feed-forward layers (MLP), layer norm, residuals
- Positional encodings (sinusoidal, learned, RoPE)
- Tokenization + embeddings
- Training objectives: next-token, masked language modeling, denoising, prefix-LM

## Training & inference considerations
- Pretrain (large corpora) → fine-tune / instruction-tune / RLHF
- Decoding: greedy, beam, temperature, top-k/top-p sampling
- Scaling trade-offs: depth, width, context length, sparsity, compute vs latency

## Practical notes
- Choose decoder-only for open generation, encoder-decoder for structured conditional tasks.
- Combine retrieval or memory for factuality and long-history use cases.
- Use efficient attention and quantization for deployment constraints.
