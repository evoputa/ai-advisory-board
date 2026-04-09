# AI Boardroom

AI tells you what you want to hear. This boardroom tells you what you need to hear.

An open-source Claude skill where 109 real business leaders challenge your thinking from different angles, and you get a clear recommendation. Built and battle-tested since 2023.

Built by **Evangel (Ev) Oputa**, Founder of **[Begine Fusion](https://beginefusion.com)** and Co-Founder of **[OnStack AI Labs](https://OnStacklabs.ai)**.

---

## The Problem

AI is sycophantic by design. OpenAI documented this with GPT-4o: the model agrees with you, validates your assumptions, and tells you what you want to hear. They called it sycophancy. It's a known, documented flaw.

Most people use AI for business advice and get one clean answer. One perspective. One recommendation. No tension.

That's not how good decisions get made.

Real advisory boards work because people disagree. You bring in people who see the world differently so they can pressure-test your assumptions, challenge your framing, and force you to confront tradeoffs you were trying to avoid.

We built the opposite of sycophancy: a system that manufactures productive disagreement on demand.

---

## What This Does

You bring a business question. The AI Boardroom:

1. **Names the strategic tension** - every real decision has a tradeoff. The board identifies it before advising.
2. **Selects 3-5 advisors** from the relevant domains, regions, and perspectives
3. **Each leader speaks in first person** - in their authentic voice, using their documented frameworks
4. **Leaders challenge each other** - that tension is the board's highest-value output
5. **Delivers a Board Synthesis** - one recommended path, a risk flag, and a specific next action

This is not motivational content. The board pressure-tests, challenges assumptions, and makes calls.

---

## The Roster

109 real business leaders. Every persona is based on their publicly documented philosophy, frameworks, and decision-making approach.

### Domains (18)

| Domain | Example Leaders |
|--------|----------------|
| Corporate Leadership & Governance | Mary Barra, Ratan Tata, Ana Botin, Aliko Dangote |
| Marketing & Sales | Seth Godin, Bernard Arnault, Mo Abudu, Oprah Winfrey |
| Technology | Bill Gates, Jensen Huang, Fei-Fei Li, Strive Masiyiwa |
| Entrepreneurship & Venture | Elon Musk, Sara Blakely, Jack Ma, Kiran Mazumdar-Shaw |
| Operations | Tim Cook, Akio Toyoda, Amancio Ortega, Mary Dillon |
| Finance & Accounting | Warren Buffett, Christine Lagarde, Ho Ching, James Mwangi |
| Legal | Kenneth Frazier, Thuli Madonsela, Brad Smith, Amal Clooney |
| Negotiation | Chris Voss, Ngozi Okonjo-Iweala, William Ury, Carlos Ghosn |
| HR & People Ops | Patty McCord, Laszlo Bock, Satya Nadella, Leena Nair |
| Product & Design | Steve Jobs, Jony Ive, Pony Ma, Daniel Ek |
| Supply Chain & Logistics | Jeff Bezos, Terry Gou, Kathy Warden, Aliko Dangote |
| Real Estate & Investing | Sam Zell, Li Ka-shing, Cathie Wood, Masayoshi Son |
| PR & Communications | Oprah Winfrey, Richard Edelman, Arianna Huffington |
| Strategy & Planning | Michael Porter, Peter Thiel, Guler Sabanci, Mo Ibrahim |
| Customer Experience | Tony Hsieh, Howard Schultz, Horst Schulze, Sonia Cheng |
| Data & Analytics | Andrew Ng, Cassie Kozyrkov, Demis Hassabis, Timnit Gebru |
| Sustainability & ESG | Yvon Chouinard, Paul Polman, Wangari Maathai |
| M&A & Corporate Development | Bernard Arnault, Henry Kravis, Safra Catz, Tony Elumelu |

### Geographic Representation

| Region | Leaders | Coverage |
|--------|---------|----------|
| North America | 42 | USA, Canada, Mexico |
| Asia | 27 | India, China, Japan, Hong Kong, Singapore, Taiwan, Saudi Arabia |
| Europe | 22 | UK, France, Germany, Spain, Sweden, Netherlands, Turkey |
| Africa | 21 | Nigeria, South Africa, Kenya, Zimbabwe, Ghana, Ethiopia, Sudan |

### Gender Balance

| Gender | Count | Percentage |
|--------|-------|------------|
| Male | 67 | 61% |
| Female | 42 | 39% |

---

## Origin

This system has been in production use inside Begine Fusion since 2023. It started as a custom GPT, was rebuilt as a modular Claude skill after Anthropic officially introduced Claude Skills on October 16, 2025, and is now open-sourced because people need to start using AI differently.

This isn't a launch. It's a reveal of something that's been running on real decisions for over two years.

---

## Installation

### Quick Install (Developers)

One command. Clones directly into your Claude skills directory and tracks the repo for easy updates.

**Mac / Linux:**
```bash
git clone https://github.com/evoputa/ai-advisory-board.git ~/.claude/skills/ai-advisory-board
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/evoputa/ai-advisory-board.git $env:USERPROFILE\.claude\skills\ai-advisory-board
```

Restart Claude Desktop. Done.

### Updating

Because the skill is a live git clone, updates are one command:

```bash
cd ~/.claude/skills/ai-advisory-board && git pull
```

New advisors, refined prompts, and fixes land instantly. Click **Watch** on this repo and select **Releases** to get notified when there's something worth pulling.

### Non-Technical Install (No Git Required)

Never touched a terminal? No problem. See **[INSTALL-EASY.md](INSTALL-EASY.md)** for a step-by-step ZIP download walkthrough. No GitHub account, no command line, just download and drag.

Tradeoff: ZIP users won't get automatic updates. To stay current, they need to re-download manually when new versions ship.

### Individual Domains

Only want one domain panel? Each domain folder under `domains/` is self-contained with its own SKILL.md and persona references. Copy just the folder you want:

```bash
# Example: just the Finance & Accounting panel
cp -r ~/.claude/skills/ai-advisory-board/domains/finance-accounting ~/.claude/skills/advisory-finance
```

---

## Configuration

For the best experience, fill out your company profile:

```bash
cp ai-advisory-board/config/company-profile-template.md ai-advisory-board/config/company-profile.md
```

Edit `company-profile.md` with your business context - revenue, targets, team size, challenges. The boardroom uses this to give specific, relevant counsel instead of generic advice.

**This step is optional.** The board works without it - you'll just get more general strategic counsel.

---

## Usage

### Full Board Session

> "I'm considering raising my prices by 40% but I'm afraid of losing my current clients. What does the board think?"

The board will:
- Name the strategic tension (margin discipline vs. market access)
- Select leaders from Finance (Buffett on margins), Marketing (Godin on positioning), Negotiation (Voss on communication), and Customer Experience (Schultz on perceived value)
- Each speaks in their authentic voice
- Deliver a synthesis with a specific recommendation and next action

### Domain-Specific Session

> "Advisory board - technology panel: Should we build our own AI infrastructure or use cloud APIs?"

Uses only the Technology panel advisors.

### Quick Counsel

> "What would Warren Buffett say about this acquisition?"

Single-leader perspective, 2-3 sentences.

### Cross-Domain Debate

> "I need the Finance panel and the Marketing panel to debate whether we should invest in brand or cut costs."

Structured point/counterpoint from different domains.

### Geographic Lens

> "I'm expanding into West Africa. What do my African advisors think I need to know?"

Filters to leaders with relevant regional experience.

---

## How Personas Work

Every leader's profile includes:

- **Voice**: How they communicate - folksy, analytical, provocative, measured
- **Core principles**: Their documented beliefs about business
- **Signature frameworks**: The models and tools they're known for
- **Bring to the table when**: The specific situations where their expertise is most relevant

All personas are based on publicly documented philosophy and frameworks. No invented quotes or positions.

---

## Project Structure

```
ai-advisory-board/
├── README.md                          # This file
├── SKILL.md                           # Full board orchestrator
├── config/
│   └── company-profile-template.md    # User customization
├── references/
│   ├── advisory-protocol.md           # How sessions run
│   ├── persona-index.md               # Master roster (109 leaders)
│   └── personas/                      # Detailed profiles by domain
│       ├── corporate-leadership.md
│       ├── marketing-sales.md
│       ├── technology.md
│       └── ... (18 domain files)
├── domains/                           # A la carte domain skills
│   ├── corporate-leadership/
│   │   ├── SKILL.md
│   │   └── references/personas.md
│   ├── marketing-sales/
│   │   ├── SKILL.md
│   │   └── references/personas.md
│   └── ... (18 domain folders)
```

---

## Security

This repo uses **[BF Git Guardian](https://github.com/evoputa/bf-git-guardian)** to prevent accidental commits of sensitive data (personal paths, API keys, client names, credentials).

After cloning, install the pre-commit hook:

```bash
python .github/hooks/install-hooks.py
```

Every commit is automatically scanned. See `.github/.sensitive-patterns` for the full rule set.

---

## Contributing

### Adding a Leader

1. Choose the primary domain
2. Write a persona profile following the format in any existing `personas/*.md` file
3. Add the leader to `references/persona-index.md`
4. Add to the relevant domain's `references/personas.md`
5. Ensure the addition maintains or improves geographic and gender balance

### Adding a Domain

1. Create a new folder in `domains/`
2. Write a SKILL.md following the pattern of existing domain skills
3. Create persona profiles for 4-6 leaders
4. Add the domain to the persona index
5. Update the main SKILL.md domain table

---

## Built By

**Evangel (Ev) Oputa**, Founder of **[Begine Fusion](https://beginefusion.com)**, a digital adoption company that sets up AI, CRM, automation, and growth marketing systems inside businesses, and Co-Founder of **[OnStack AI Labs](https://OnStacklabs.ai)**, Calgary's first innovative, structured, collaborative skills and applied AI lab, working across a global ecosystem.

Technical implementation assisted by Claude Code (Anthropic).

---

## License

MIT License. Use it, modify it, share it.
