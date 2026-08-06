# Week 04: Probability, Statistics, Information Theory

## Outcome

By Sunday you can simulate and reason about the distributions that recur
throughout the course, explain maximum likelihood estimation and connect it to
loss functions, and answer — three different ways — why cross entropy is the loss
for classification.

Concretely: `bootstrap/math-labs/tests/test_probability.py` passes, and the
Month 1 capstone package is assembled and published.

## Why This Matters For OpenAI/Anthropic-Level Interviews

This week supplies the vocabulary for everything downstream. Cross entropy is
the loss for every classifier and every language model you will train. KL
divergence is the regularizer keeping an RLHF policy near its reference model
(Month 12) and the standard tool for comparing model output distributions
(Week 36). Perplexity is the language model metric (Week 35). Entropy is the
decision tree split criterion (Week 7). Bootstrap confidence intervals are what
make every result you report from Week 11 onward defensible rather than
anecdotal.

The unifying idea worth internalizing now: **training a model is maximum
likelihood estimation.** Cross-entropy loss is the negative log likelihood of a
categorical distribution; MSE is the negative log likelihood of a Gaussian with
fixed variance. Once you have derived both, loss functions stop being a menu and
become consequences of a modeling assumption. That framing is what a strong
answer to "why this loss?" sounds like.

The base-rate question — 99% accurate test, 1-in-10,000 disease, what is
P(disease | positive)? — is asked constantly and it is the same reasoning as "your
fraud model is 99.9% accurate and useless," which is Week 11.

## Time Budget: 15-20 Hours

- Theory: 4 hours
- Coding: 6 hours
- Project: 4 hours (capstone assembly)
- Interview practice: 2 hours
- Review/write-up: 2 hours

## Theory Lessons

1. **Descriptive statistics**
   1. Mean, variance, standard deviation
   2. ddof, and why NumPy defaults to 0 while pandas defaults to 1
   3. Covariance and correlation; the covariance matrix as Week 2's PCA input
   4. Standardization, and why you must reuse *training* statistics
2. **Distributions**
   1. Bernoulli — the distribution behind every binary classifier output
   2. Gaussian — the default, and why (central limit theorem, plus convenience)
   3. Poisson — counts per interval; query arrivals, lock waits, error rates
   4. Categorical — what a language model outputs at every position
3. **Likelihood and estimation**
   1. Likelihood versus probability — the distinction people get wrong
   2. Why we maximize the *log* likelihood: products underflow, sums do not
   3. MLE for Bernoulli (derive it — the answer is the sample mean)
   4. MLE for Gaussian, and why the variance estimate is biased low
   5. **Training as MLE.** Derive cross-entropy from a categorical likelihood
      and MSE from a Gaussian likelihood. This is the week's central idea.
4. **Bayes rule**
   1. Prior, likelihood, evidence, posterior
   2. The base rate fallacy, worked numerically
   3. Why a 99% accurate test for a rare condition is mostly false positives
5. **Uncertainty**
   1. Sampling distributions and standard error
   2. The bootstrap: resample, recompute, take percentiles
   3. Why the bootstrap works for statistics with no analytic formula
   4. Confidence intervals as the honest way to report a number
6. **Information theory**
   1. Entropy as average surprise, and as a coding-length bound
   2. Cross entropy as the cost of using the wrong code
   3. KL divergence as the *excess* cost — non-negative, asymmetric
   4. **The identity:** H(p, q) = H(p) + D(p‖q). Minimizing cross entropy
      minimizes KL, because H(p) is fixed by the data.
   5. Jensen-Shannon divergence: symmetric, bounded
   6. Perplexity as exp(mean NLL), and why it is tokenizer-dependent
   7. Mutual information, conditional entropy, and information gain

## Required Free Resources

**Primary:**
- Mathematics for Machine Learning, chapter 6 —
  https://mml-book.github.io/
- Seeing Theory (interactive) — https://seeing-theory.brown.edu/
  Chapters 1-4. Excellent for building intuition quickly.
- 3Blue1Brown, "Bayes theorem" and "The medical test paradox" —
  https://www.3blue1brown.com/topics/probability

**For information theory:**
- Chris Olah, "Visual Information Theory" — https://colah.github.io/posts/2015-09-Visual-Information/
  The clearest treatment of entropy, cross entropy, and KL available anywhere.
  Read this one properly; it is worth the hour.

**Reference:**
- MIT OCW 18.05 — https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/
- SciPy stats documentation — https://docs.scipy.org/doc/scipy/reference/stats.html
  Your reference oracle in the tests.

## Hands-On Exercises

```bash
cd bootstrap/environment && make week W=4
```

1. **Descriptive statistics** (1h) — `mean`, `variance`, `covariance_matrix`,
   `correlation_matrix`, `standardize`. Note that `standardize` returns the mean
   and std so you can apply training statistics to held-out data. That is the
   Week 10 leakage lesson arriving six weeks early.
2. **Distributions** (2h) — `Bernoulli`, `Gaussian`, `Poisson`, `Categorical`.
   Implement the PDFs and PMFs yourself; SciPy is the test oracle only. Two
   numerical traps with tests waiting for them: use `lgamma` for Poisson's
   factorial (200! overflows a float64), and compute `log_pdf` directly rather
   than as `log(pdf(x))` (which is `-inf` in the tails).
3. **MLE** (1.5h) — `mle_bernoulli`, `mle_gaussian`, `log_likelihood`. Derive
   both on paper first. Then verify empirically that the MLE variance estimate is
   biased low — there is a test for it, and seeing the bias is more convincing
   than reading about it.
4. **Bayes** (0.5h) — `bayes_rule`. Work the base-rate problem and confirm you
   get ≈1%. Be able to explain that number in 60 seconds.
5. **Bootstrap** (1h) — `bootstrap_confidence_interval`. Verify the interval
   narrows with more data, and that it works for the median where no simple
   analytic formula exists.
6. **Information theory** (2h) — `entropy`, `cross_entropy`, `kl_divergence`,
   `js_divergence`, `perplexity`, `mutual_information`, `conditional_entropy`,
   `information_gain`, `gini_impurity`.

   The test to focus on is `test_the_identity`: H(p,q) = H(p) + D(p‖q). When you
   see that numerically, "why is cross entropy the loss?" has a real answer.

   Note that `information_gain` and `gini_impurity` are written now and used in
   Week 7. Decision trees are an information-theoretic algorithm, and building
   the tool three weeks before the application makes that connection stick.

## Bootstrap Files To Create

Implement:

```text
bootstrap/math-labs/src/probability.py
bootstrap/math-labs/src/information_theory.py
```

Create:

```text
bootstrap/math-labs/notebooks/distribution_simulations.ipynb
```

The notebook should show: samples from each distribution against its analytic
density; the central limit theorem demonstrated by summing uniform variables;
a likelihood surface for a Gaussian with the MLE marked; the base-rate problem
visualized; and entropy plotted against p for a Bernoulli, peaking at 0.5.

## Tests To Write

`tests/test_probability.py` is the specification. Add three:

1. A test that maximum likelihood recovers the true parameters as sample size
   grows — run at n = 10, 100, 1000, 10000 and assert the error shrinks.
2. A test that KL divergence is infinite (or raises) when q has a zero where p
   does not, and that add-k smoothing fixes it.
3. A test connecting Weeks 3 and 4: cross entropy computed by your
   `information_theory.cross_entropy` matches the loss computed by your Week 3
   `autodiff_scalar.cross_entropy` on the same inputs.

That third test is worth more than it looks — it forces you to reconcile two
implementations written from different angles, and any discrepancy is a
misunderstanding you would otherwise carry forward.

## Portfolio Artifact

This week produces the **Month 1 capstone**. See `capstone.md` for the full
specification. In summary:

- The `ml-math-toolkit` package, installable, all five modules, all tests passing
- A README mapping each module to the ML concept it underpins
- Two polished notebooks
- Published to a public GitHub repository

## Interview Drills

**Coding (45 min).** Two problems. This week, choose ones with a counting or
probability flavor.

**ML theory (30 min).** Three questions, out loud, one recorded:

> 1. Why is cross entropy the loss function for classification? Give three
>    different answers.
> 2. A test is 99% sensitive and 99% specific. The disease affects 1 in 10,000.
>    You test positive. What is the probability you have it, and why does that
>    surprise people?
> 3. What is KL divergence, and why is it not a distance metric?

For question 1, the three answers are: maximum likelihood (it is the negative log
likelihood of a categorical distribution); information theory (minimizing it
minimizes KL to the true distribution, since H(p) is constant); and the practical
one (its gradient with respect to the logits is `p - y`, which is well-behaved
and does not saturate the way squared error on a sigmoid does). Having all three
ready is what distinguishes a 9 from a 7.

**Behavioral (15 min).** Draft story #8 from `INTERVIEW_PREP.md`: learning
something hard, fast. Use this month. Get it to 90 seconds in STAR form.

## Evaluation Rubric

| Score | Standard |
| ----- | -------- |
| 3 | Some distributions implemented. Information theory not attempted. |
| 5 | Tests pass. Cannot explain the relationship between cross entropy and KL. |
| 7 | All tests pass. Notebook complete. Can derive MLE for Bernoulli and state the H(p,q) identity. |
| 9 | Above, plus can answer "why cross entropy?" three ways, and the capstone package is published with a clean README. |
| 10 | Above, plus your cross-module consistency test caught a real discrepancy, and you can explain perplexity's tokenizer dependence unprompted. |

## Stretch Goal

Implement a small Bayesian linear regression: place a Gaussian prior on the
weights, compute the posterior analytically, and plot the *predictive
distribution* rather than a point estimate.

Two payoffs. First, seeing that ridge regression is exactly MAP estimation with a
Gaussian prior connects Week 4 to Week 5 in a way that makes regularization feel
principled rather than arbitrary. Second, uncertainty-aware prediction is directly
relevant to Month 11 — an agent that reports "I am 60% confident" needs a
defensible notion of what that number means, and most agent projects hand-wave it.

---

## Month 1 Wrap

This is the last week of Month 1. Before starting Month 2:

1. Complete `coach/weekly_checkin_template.md` for Week 4.
2. Complete `coach/monthly_review_template.md` for Month 1.
3. Score the capstone with `coach/capstone_review_rubric.md`.
4. Publish the repository.
5. Re-derive one thing from Week 1, cold, as a retention check.

If the month average is below 7, write the remediation plan before Week 5. The
Month 1 material is load-bearing for the next seventeen months; a shaky
foundation here is the most expensive debt available to you.
