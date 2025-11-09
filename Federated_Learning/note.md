# Federate Learning

## 1. Concept Overview
Federated Learning (FL) is a decentralized machine learning paradigm that enables multiple clients (devices, organizations, or data silos) to collaboratively train a shared model **without exchanging raw data**.

In traditional machine learning, datasets are collected and sent to a central
server where training occurs. However, this raises **privacy, security, and
compliance** issues, especially when data contains sensitive information (e.g.,
healthcare, finance, or personal data).

FL addresses these challenges by **keeping data local** and only sharing model updates (gradients or weights) with a coordinating server or among peers.

---

## 2. Key Idea

> Instead of sending data **to** the model (in the case of traditional ML), FL sends the model **to the data**.

Each participant:
- Trains a local copy of the global model on its private dataset.
- Sends only model updates (e.g., parameter differences) to an aggregator.
- The aggregator (central or distributed) combines all updates to produce an improved **global model**.

**This approach preserves data locality while enabling collective learning.**

---

## 3. Core Workflow

### a. Initialization
- A **global model** is initialized.
- In **centralized FL**, the server initializes and distributes the model.
- In **fully decentralized (peer-to-peer) FL**, clients agree on a shared seed or model initialization collaboratively.

### b. Local Training
- Each client trains the model on its **private local data** for several epochs.
- The client computes the **model update** (e.g., difference between the new and old model parameters).

### c. Aggregation of Updates
- Clients send updates to the server (or to peers in a decentralized setting).
- The **Federated Averaging (FedAvg)** algorithm aggregates them.

Although FL prevents raw data sharing. However, it is still vulnerable to
different attacks such as:
- **Inference attacks:** Attackers reconstruct data from gradients or updates.
- **Model poisoning:** Malicious clients inject false updates.
- **Membership inference:** Adversaries infer if specific data points were used.

Different techniques are being suggested and implemented to enhance privacy of
FL:
 Technique | Description | Benefit |
|------------|--------------|----------|
| **Differential Privacy (DP)** | Adds random noise to updates before sharing, limiting individual data leakage. | Protects against inference attacks. |
| **Secure Multi-Party Computation (SMPC)** | Allows multiple parties to jointly compute an aggregate function without revealing their inputs. | Ensures confidentiality during aggregation. |
| **Homomorphic Encryption (HE)** | Enables computations on encrypted data (e.g., sum or average) without decryption. | Preserves confidentiality of updates. |
| **Secure Aggregation** | Server aggregates encrypted updates and only learns the aggregated result. | Prevents the server from accessing individual updates. |

