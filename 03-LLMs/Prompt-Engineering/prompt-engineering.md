# Prompt Engineering

Prompt Engineering is the discipline of designing and refining inputs (prompts) given to Large Language Models (LLMs) to guide them toward producing accurate, relevant, and reliable outputs. It leverages the model's language comprehension capabilities to maximize response quality without modifying the model's weights.

## Prompting Techniques

### Zero-shot
The model is asked to perform a task **without any examples**, relying entirely on its pre-trained knowledge.

> _"Translate the following sentence to French: 'The sky is blue.'"_

### Few-shot
The prompt includes **input-output example pairs** that demonstrate the desired behavior before presenting the actual task. This helps the model infer the expected pattern.

> _Example 1: Input: "Happy" → Output: "Positive"_
> _Example 2: Input: "Terrible" → Output: "Negative"_
> _Now classify: Input: "Amazing" → Output:_

### Chain-of-Thought (CoT)
The model is prompted to **reason through a problem step by step** before giving a final answer, improving accuracy on complex reasoning tasks.

- **Zero-shot CoT**: Append "Let's think step by step." to the prompt — no examples needed.
- **Few-shot CoT**: Provide examples that include explicit reasoning chains, showing both the thought process and the final answer.

> Reference: Wei et al., 2022 — _"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"_

---

## Anatomy of a Good Prompt

A well-structured prompt typically includes:

| Component | Description |
|---|---|
| **Role** | Define a persona for the model (e.g., "You are an expert software engineer") |
| **Task / Instruction** | Clearly state what the model should do |
| **Context** | Provide relevant background information |
| **Examples** | Illustrate expected input/output pairs (few-shot) |
| **Output Format** | Specify the structure, tone, or format of the desired response |

---

## Other Notable Techniques

- **Role Prompting** — Assigning a specific role or persona to steer the model's tone and expertise level.
- **Tree of Thoughts (ToT)** — Extends CoT by exploring multiple reasoning branches simultaneously.
- **ReAct** — Combines reasoning and acting, allowing the model to interleave thought steps with tool use or external lookups.