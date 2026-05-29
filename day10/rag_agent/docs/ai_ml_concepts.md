# Artificial Intelligence and Machine Learning Concepts

## What is Machine Learning?
Machine learning (ML) is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. ML focuses on developing computer programs that can access data and use it to learn for themselves.

## Types of Machine Learning

### Supervised Learning
Supervised learning uses labeled training data to learn a mapping function from inputs to outputs. Common algorithms include linear regression, decision trees, random forests, and support vector machines. Applications include spam detection, image classification, and medical diagnosis.

### Unsupervised Learning
Unsupervised learning finds hidden patterns or intrinsic structures in unlabeled data. Clustering (K-means, DBSCAN) and dimensionality reduction (PCA, t-SNE) are key techniques. Use cases include customer segmentation and anomaly detection.

### Reinforcement Learning
Reinforcement learning trains agents to make decisions by rewarding desired behaviors and punishing undesired ones. It powers game-playing AIs like AlphaGo and real-world applications like robotics and recommendation systems.

## Deep Learning
Deep learning uses neural networks with many layers (hence "deep") to learn representations of data. Convolutional Neural Networks (CNNs) excel at image tasks; Recurrent Neural Networks (RNNs) handle sequential data; Transformers have revolutionized NLP.

## Key Concepts

### Overfitting and Underfitting
Overfitting occurs when a model learns training data too well, including noise, and performs poorly on new data. Underfitting happens when a model is too simple to capture the underlying pattern. Regularization techniques (L1, L2, dropout) combat overfitting.

### Cross-Validation
Cross-validation is a technique to evaluate model generalization. K-fold cross-validation splits data into k subsets, trains on k-1, and tests on the remaining fold, rotating through all folds.

## Large Language Models (LLMs)
Large Language Models are trained on massive text corpora using self-supervised learning. Models like GPT-4, Claude, and Mistral use the Transformer architecture with billions of parameters. They exhibit emergent capabilities including reasoning, code generation, and in-context learning.

### Retrieval-Augmented Generation (RAG)
RAG combines LLMs with information retrieval systems. Instead of relying solely on parametric knowledge, RAG retrieves relevant documents at inference time and conditions the LLM response on them. This reduces hallucination and allows knowledge updates without retraining.

### Fine-tuning vs Prompting
Fine-tuning updates model weights on task-specific data. Prompt engineering (few-shot, chain-of-thought) steers behavior without weight updates. RLHF (Reinforcement Learning from Human Feedback) aligns models with human preferences.
