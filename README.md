# ECPP — Learning the Mathematics, Building the Algorithms

> **Status: Work in progress.** This repository documents my ongoing study and Python implementation of the mathematical foundations needed to understand Atkin–Morain Elliptic Curve Primality Proving (ECPP).

## About the project

I am a final-year cybersecurity engineering student at EMSI with a strong interest in **number theory, algorithms, mathematical proofs, and cryptography**.

My approach is simple:

**Understand → Prove → Analyze → Implement → Test.**

Rather than treating ECPP as a black box, I am building my understanding step by step, starting with number-theoretic and modular-arithmetic algorithms. I aim to study the theorems behind each component, justify its correctness, analyze its complexity, and translate it into tested Python code.

**This project is not finished and should not be presented as a complete ECPP implementation.**

## What is ECPP?

**Elliptic Curve Primality Proving (ECPP)** is a family of methods for proving that an integer is prime using properties of elliptic curves. Atkin–Morain ECPP uses ideas from complex multiplication to construct suitable elliptic curves and produce primality proofs that can be checked independently.

This repository is currently focused on the mathematical and algorithmic prerequisites, rather than a complete prover or certificate verifier.

## Current repository structure

The repository currently includes these Python files:

| File | Purpose |
| --- | --- |
| `modular.py` | Work on modular-arithmetic algorithms |
| `number_theory.py` | Work on foundational number-theory algorithms |
| `test_modular.py` | Tests and experiments for modular-arithmetic code |
| `test_number_theory.py` | Tests and experiments for number-theory code |

The modules and their tests are evolving as I progress through the mathematics.

## Mathematical learning roadmap

The following topics form my **study and development plan**, not a list of completed features:

- [ ] Consolidate elementary number theory, the Euclidean algorithm, Bézout's identity, and modular arithmetic.
- [ ] Study the Chinese Remainder Theorem and primality-related algorithms.
- [ ] Develop a rigorous understanding of finite fields and polynomial arithmetic.
- [ ] Study elliptic curves over finite fields and their group law.
- [ ] Understand the primality criteria underlying elliptic-curve primality proving.
- [ ] Explore complex multiplication and Hilbert class polynomials.
- [ ] Study Atkin–Morain ECPP certificate construction and independent verification.
- [ ] Analyze correctness, performance, and algorithmic complexity.

*These checkboxes track future learning goals; they do not imply the listed subjects have not been studied in theory or that their implementations are complete.*

## Running the code

The project uses **Python 3**. Clone the repository and inspect the modules and accompanying tests:

```bash
git clone https://github.com/achraflazrak01/ECPP.git
cd ECPP
```

If you use `pytest`, you can try:

```bash
python -m pytest -q
```

Test execution may depend on the current state of the code and your Python environment. The project is under active development.

## From ECPP to broader mathematical cryptography

I chose ECPP partly to strengthen the mathematical foundations I want to bring to future research in **post-quantum cryptography**, especially **isogeny-based cryptography**.

**ECPP is not a post-quantum cryptographic scheme.** However, studying finite fields, elliptic curves, number theory, and mathematical proofs provides a useful foundation for exploring advanced cryptographic constructions. Other PQC families, such as lattice-based cryptography, require additional mathematical tools.

## Project philosophy

> I don't just want to learn how algorithms work. I want to understand **why** they work, prove their correctness, analyze their complexity, and implement them myself.

**Understand. Prove. Analyze. Implement.**

## Author

**Achraf Lazrak**  
Final-year Engineering Student — Cybersecurity and Network Infrastructure, EMSI  
GitHub: [@achraflazrak01](https://github.com/achraflazrak01)

---

*Educational and research-oriented code. Not intended for production cryptographic use.*
