import collections
import math
import random


class NGramLanguageModel:

    def __init__(self, n=3):
        """Initializes the model.

        n=2 is a Bigram, n=3 is a Trigram, etc.
        """
        self.n = n
        # Stores counts of (context) -> {next_word: count}
        self.model = collections.defaultdict(collections.Counter)
        self.vocabulary = set()

    def _get_context(self, tokens, index):
        """Helper to extract the context window preceding a target token."""
        start = max(0, index - (self.n - 1))
        context = tuple(tokens[start:index])
        # Pad with empty strings if the context is shorter than n-1 (at the start of a text)
        while len(context) < self.n - 1:
            context = ("",) + context
        return context

    def train(self, text):
        """Tokenizes text and builds the N-gram frequency tables."""
        # Simple tokenization: lowercase and split by spaces
        tokens = text.lower().split()
        self.vocabulary.update(tokens)

        for i, token in enumerate(tokens):
            context = self._get_context(tokens, i)
            self.model[context][token] += 1

    def get_word_probability(self, context, word, alpha=1.0):
        """Calculates the probability of a word given its context.

        Applies Laplace (Add-one) smoothing to handle unseen variations.
        """
        context = tuple(context)
        context_counts = self.model[context]
        total_context_occurrences = sum(context_counts.values())

        # Vocabulary size plus 1 for potential unknown tokens (<UNK>)
        vocab_size = len(self.vocabulary) + 1

        # Laplace (Add-Alpha) Smoothing formula
        word_count = context_counts[word]
        probability = (word_count + alpha) / (
            total_context_occurrences + (alpha * vocab_size)
        )
        return probability

    def generate_text(self, seed_text, max_length=20):
        """Generates text word-by-word based on a seed text."""
        tokens = seed_text.lower().split()
        generated = list(tokens)

        for _ in range(max_length):
            # Extract the last context window from what we have generated so far
            context = self._get_context(generated, len(generated))

            # If context was never seen, fall back to random selection from vocabulary
            if context not in self.model:
                next_word = random.choice(list(self.vocabulary))
            else:
                # Sample a word weighted by its frequency in this context
                candidates = list(self.model[context].keys())
                weights = list(self.model[context].values())
                next_word = random.choices(candidates, weights=weights)[0]

            generated.append(next_word)

        return " ".join(generated)

    def evaluate_perplexity(self, evaluation_text):
        """Evaluates the model's performance using Perplexity.

        Lower perplexity indicates a better model.
        """
        tokens = evaluation_text.lower().split()
        if not tokens:
            return float("inf")

        log_probability_sum = 0.0
        N = len(tokens)

        for i, token in enumerate(tokens):
            context = self._get_context(tokens, i)
            # Use small alpha smoothing to avoid log(0) for unseen words
            prob = self.get_word_probability(context, token, alpha=0.1)
            log_probability_sum += math.log2(prob)

        # Perplexity = 2^(-1/N * sum(log2(P(w_i | context))))
        avg_negative_log_likelihood = -log_probability_sum / N
        perplexity = math.pow(2, avg_negative_log_likelihood)
        return perplexity


# ==========================================
# Demonstration & Usage
# ==========================================
if __name__ == "__main__":
    # 1. Prepare Training Data
    corpus = """
    i love machine learning .
    i love natural language processing . 
    i love sahyadri .
    """

    # 2. Train a Trigram Model (n=3)
    trigram_model = NGramLanguageModel(n=3)
    trigram_model.train(corpus)
    print("Model trained successfully!")
    print(f"Vocabulary size: {len(trigram_model.vocabulary)} words\n")

    # 3. Text Generation
    # We provide a seed context, and let it generate the next sequence
    seed = "i love"
    generated_output = trigram_model.generate_text(seed, max_length=8)
    print(f"Generated Text starting with '{seed}':")
    print(f"   \"{generated_output}\"\n")

    # 4. Evaluation using Perplexity
    # Perfect match test text (should have low perplexity)
    good_test = "i love aiml"
    # Unfamiliar text (should have high perplexity)
    bad_test = "i hate sahyadri"

    perp_good = trigram_model.evaluate_perplexity(good_test)
    perp_bad = trigram_model.evaluate_perplexity(bad_test)

    print("Model Evaluation (Perplexity):")
    print(f"   - Perplexity for familiar text ('{good_test}'): {perp_good:.2f}")
    print(f"   - Perplexity for unfamiliar text ('{bad_test}'): {perp_bad:.2f}")
    print(
        "   (Note: Lower perplexity means the model found the sentence more predictable and natural!)"
    )
