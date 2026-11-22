# Working notes — the-plan-make-fun-will-carry-20261122-2138

## The judge's criteria (quoted verbatim from the kit's RULES.txt)

> Weigh them on these, most important first:
> 1. It is a plan you can carry out yourself: steps an AI agent can take with a browser, code, APIs and $100. Text that is not a plan, or a plan whose core work needs a human, loses to any real plan.
> 2. Expected money: what you would most likely hold on day 30, not the best case. A plan that probably turns $100 into $500 beats one that might make a million but most likely loses the $100.
> 3. It works today: every step uses services, markets and buyers that exist now and would take an agent's work and pay for it. Nothing rests on luck, inside access or a payment that never comes.
> 4. Concrete: it names what is sold or done, who pays, where they are found, the price, and what to do on day one.
> 5. Edge: a reason it wins where a thousand other agents with the same $100 would try the same obvious idea.
>
> Length for its own sake does not count.

## Candidates (all authored fresh in this session, each 1–280 chars)

### C1 — missed-call texter for local plumbers (275 chars)
Day 1: email 100 local plumbers offering an AI missed-call texter: Twilio answers missed calls by SMS in 60s. $99 setup + $29/mo; $20 buys the Twilio number. Close 5 setups in 30 days = $495 + $145/mo. Edge: a missed call is a lost job; agents pitch generic chatbots instead.

### C2 — Fiverr dashboards for Etsy sellers (275 chars)
Day 1: list a $40 Fiverr gig: turn a shop's messy sales CSV into a clean Excel dashboard in 24h. DM 30 Etsy/Shopify sellers daily with a free sample of their own data, then $40/shop. ~12 jobs in 30 days = $480. Edge: sellers already pay for this; agents chase crypto instead.

### C3 — Upwork data cleanup (260 chars)
Day 1: on Upwork bid $30/job cleaning small-business customer lists: dedupe, format, verify emails with Python. Spend $15 on connects. Win 2 jobs/day after week one. Likely $450-600 in 30 days. Edge: boring, repeatable work buyers post daily; agents ignore it.

### C4 — Google Business Profile upkeep (256 chars)
Day 1: email 100 local dentists and salons offering Google review replies + profile upkeep for $49/mo. $0 ad spend. Close 10 clients = $490/mo recurring. Edge: every local business needs it, yet almost no agent sells to Main Street instead of the internet.

### C5 — lead lists for trades (276 chars)
Day 1: build verified lists of 500 local homeowners needing roofers/plumbers from public records; sell each list for $25 on Gumroad and by cold email. Spend $20 on email tooling. Sell 20 lists in 30 days = $500. Edge: agents sell to consumers; tradespeople pay cash for leads.

### C6 — Shopify audit PDFs (259 chars)
Day 1: offer $25 speed-and-SEO audit PDFs to 50 Shopify stores a day via their contact forms, generated with Python. $0 spend. Close 1 in 25; ~2 sales a day after week one = $500+. Edge: stores already spend on apps; an audit is a cheap yes before a big sale.

### C7 — LinkedIn rewrites on Fiverr (271 chars)
Day 1: list a $35 LinkedIn rewrite gig on Fiverr, delivered in 24h. DM 30 job-seekers a day offering a free headline rewrite, upsell the $35 profile. ~12 clients in 30 days = $420. Edge: job-seekers pay fast and decide in minutes; agents pitch businesses that take weeks.

## Pairwise tournament (each criterion scored 1–5, criterion order = weight)

| Cand | C1 executability | C2 expected $ | C3 works today | C4 concrete | C5 edge | Total |
|------|------------------|---------------|----------------|-------------|---------|-------|
| C1   | 5 | 4 | 5 | 5 | 4 | **23** |
| C2   | 5 | 3 | 4 | 5 | 3 | 20 |
| C3   | 5 | 3 | 5 | 4 | 3 | 20 |
| C4   | 5 | 3 | 5 | 5 | 4 | **22** |
| C5   | 3 | 2 | 3 | 4 | 3 | 15 |
| C6   | 5 | 3 | 5 | 5 | 3 | 21 |
| C7   | 5 | 3 | 4 | 5 | 3 | 20 |

Head-to-heads that matter:
- C1 vs C4 (final): both sell to local businesses, but C1's $99 one-time setup is an easier yes than C4's $49/mo retainer, C1 names its tool (Twilio) and cost ($20), and C1's recurring $145/mo stacks on a $495 setup haul. C1 wins.
- C1 vs C6: C6's "1 in 25 close, 2/day" math implies 60 sales ($1,500) while claiming only "$500+", an internal inconsistency a reasoning judge can spot; C1's numbers reconcile exactly (5 x $99 = $495, 5 x $29 = $145). C1 wins.
- C3 loses on internal inconsistency too ("2 jobs/day after week one" is ~$1,260, not "$450-600").
- C5 loses: "verified homeowners needing roofers" from public records is not verifiable, and Gumroad with no audience sells ~nothing.
- C2/C7 lose on expected money: a brand-new Fiverr gig gets ~zero organic orders in week one, and cold DMs on Etsy/LinkedIn convert poorly and risk account limits.

**Tournament winner: C1.**

## Self-judge pass on C1 (scored as the judge would, from the text alone)

1. Executable by an agent: 5/5. Every step is browser/code/API work: cold email, Twilio API, SMS. No human needed.
2. Expected money: 3.5/5 — WEAKEST. "Email 100 local plumbers" reads as 100 emails total, so 5 closes implies a 5% cold-email close rate, which is optimistic and strains the median-outcome claim. Fix: make the outreach daily ("100 a day" = 3,000 emails in 30 days, 5 closes = 0.17%, very credible), which directly strengthens the expected-value claim.
3. Works today: 5/5. Twilio, SMS, local plumbers, $99 setup — all real, all paying today.
4. Concrete: 5/5. Service, buyer, price, day-one action, and the $20 spend are all named.
5. Edge: 4/5. "A missed call is a lost job" is a sharp, specific pain; the contrast with generic chatbots is real.

**Fix applied (revision in a later edit, then re-verified):** "email 100 local plumbers" -> "email 100 local plumbers a day"; trimmed "generic chatbots" -> "chatbots" to stay within 280 chars. Revised text is 273 chars; the close-rate math (5 of 3,000) now supports the median outcome instead of undermining it.
