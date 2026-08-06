# AI Frontier Career Roadmap

An 18-month, 78-week training program that takes a senior database engineer to
serious-candidate readiness for AI Engineer, ML Engineer, LLM Platform Engineer,
Research Engineer, and AI Infrastructure Engineer roles at frontier AI labs.

**This is not a job guarantee.** No course is. What this course does guarantee is
a structure: if you execute it at a high standard for 78 weeks, you will finish
with the mathematical depth, implementation skill, systems judgment, public
portfolio, and interview fluency needed to compete for those roles seriously
rather than hopefully. The gap between "interested in AI" and "hireable at a
frontier lab" is roughly 1,200 focused hours of the right work. This repository
is the schedule for those hours.

---

## The Positioning

You are not becoming a generic AI learner. There are hundreds of thousands of
those and they are indistinguishable from each other on paper.

You are becoming this:

> **AI Systems Engineer / LLM Platform Engineer specializing in autonomous
> database intelligence, enterprise knowledge systems, evaluation, reliability,
> and production-grade AI tooling.**

Your DBA background is not a liability to explain away. It is the moat. Almost
nobody applying to these roles has ever been paged at 3am for a query plan
regression, tuned a production database under load, or run a postmortem that
executives read. Frontier labs are drowning in people who can fine-tune a model
and starving for people who can operate systems. The course is engineered so
that every phase compounds that advantage rather than diluting it.

---

## Repository Layout

```text
ai-frontier-career-roadmap/
  README.md                  <- you are here
  COURSE_MAP.md              <- the 18-month arc, phase by phase
  WEEKLY_PLAN.md             <- all 78 weeks in one place
  MONTHLY_CAPSTONES.md       <- all 18 capstones in one place
  INTERVIEW_PREP.md          <- the interview training system
  RESOURCE_INDEX.md          <- every resource, organized by topic
  PORTFOLIO_STRATEGY.md      <- what you build and why recruiters care
  SCORECARD.md               <- how you are graded and when you may advance
  coach/                     <- templates you fill in each week and month
  bootstrap/                 <- the code you actually write, ten lab packages
  months/                    <- 18 month folders, one file per week
```

- **`months/`** is where you live day to day. Open the current week's file.
- **`bootstrap/`** is where the code goes. Ten packages, built up over 18 months.
- **`coach/`** is where you write down what happened. Templates only work if used.

---

## How To Use This Course

### The weekly loop

1. **Monday (30 min).** Open `months/month-XX-*/week-YY.md`. Read the whole
   file before writing any code. Note the outcome statement and the rubric — you
   are being graded against them on Sunday.
2. **Weekdays (10-14 hours).** Theory first, then implementation. Never read
   theory you do not implement within 72 hours; unimplemented theory evaporates.
3. **Interview drills (2 hours, spread out).** Every week has them from Week 1.
   Do not defer interview prep to Month 18 — Month 18 is polish, not learning.
4. **Saturday (2-4 hours).** Finish the artifact. Write tests. Push clean commits.
5. **Sunday (1 hour).** Fill in `coach/weekly_checkin_template.md`. Score
   yourself honestly against the six axes in `SCORECARD.md`. Average below 7/10
   means you write a remediation plan before starting the next week.

### The monthly loop

1. Weeks 1-3 of the month build the capability.
2. Week 4 of the month spends its project hours on the capstone.
3. End of month: fill in `coach/monthly_review_template.md`, score the capstone
   with `coach/capstone_review_rubric.md`, publish the artifact publicly.

### The quarterly loop

Every third month, run a full mock interview loop from `INTERVIEW_PREP.md` and
record it. Watch the recording. It will be unpleasant and it is the single
highest-leverage hour in the quarter.

---

## Time Budget

15-20 hours per week, allocated roughly:

| Bucket             | Hours | Purpose                                     |
| ------------------ | ----- | ------------------------------------------- |
| Theory             | 3-5   | Lectures, papers, textbook sections         |
| Coding             | 5-7   | Implementation and debugging                |
| Project / capstone | 3-5   | The portfolio artifact                      |
| Interview practice | 2     | Coding, ML theory, system design, narrative |
| Review / write-up  | 1-2   | READMEs, blog posts, weekly check-in        |

If you get 12 hours in a bad week, cut the stretch goal and the blog post. Keep
theory, keep the tests, keep the check-in. If you get three bad weeks in a row,
do not roll the debt forward — declare a catch-up week and reset. The plan
assumes 78 productive weeks, not 78 consecutive calendar weeks.

---

## Getting Started

```bash
cd bootstrap/environment
make setup          # creates the venv and installs the base toolchain
make test           # should pass with zero tests collected on day one
cd ../..
open months/month-01-foundations/week-01.md
```

Then:

1. Create a public GitHub repository for the course itself.
2. Create a second public GitHub organization or account-level home for the
   flagship projects — recruiters will look at the flagships, not the coursework.
3. Commit at least three times per week. Commit history is scouting tape.

---

## The Non-Negotiables

These are the rules that make the difference between finishing the course and
finishing the course *well*. Violating any of them silently converts this into
a tutorial-watching habit.

- Every week produces something concrete that did not exist on Monday.
- Every month produces a capstone with a README a stranger can follow.
- Every project has tests, an evaluation section, and a stated limitation.
- Every theory topic gets implemented, not just read.
- Every implementation gets converted into a spoken explanation you can deliver
  without notes.
- Every artifact is public. Private work does not count toward the portfolio.
- Your DBA background appears in the portfolio as an advantage in at least four
  of the nine flagship projects.

---

## Coaching Contract

The coach in this repository is direct. It will not flatter you, will not
celebrate half-finished work, and will not tell you that you are ready when you
are not. In exchange:

- Every week has a stated reason for existing.
- Every drill builds a specific, named capability.
- Every month ends with a match-level test of that capability.
- Every quarter ends with a measurable, honest performance review.

Fundamentals are conditioning. Projects are practice matches. Capstones are
tournament matches. Interview practice is penalty kicks. Paper reproduction is
tactical analysis. The portfolio is the scouting tape.

Start with `COURSE_MAP.md`, then open Week 1.
