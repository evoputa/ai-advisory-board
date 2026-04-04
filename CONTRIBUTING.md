# Contributing to AI Boardroom

Thanks for your interest in contributing. This project is maintained by **Evangel (Ev) Oputa**, Founder of [Begine Fusion](https://beginefusion.com) and Co-Founder of [OnStack AI Labs](https://OnStacklabs.ai).

---

## Ways to Contribute

### Add a Leader

The board benefits from diverse, accomplished perspectives. To add a leader:

1. **Choose the primary domain** from the 18 existing domains
2. **Write a persona profile** following the format in any existing `references/personas/*.md` file
3. **Add the leader** to `references/persona-index.md`
4. **Add to the domain** `references/personas/[domain].md` and `domains/[domain]/references/personas.md`
5. **Maintain balance** - additions should maintain or improve geographic and gender representation

### Add a Domain

1. Create a new folder in `domains/`
2. Write a `SKILL.md` following the pattern of existing domain skills
3. Create persona profiles for 4-6 leaders
4. Add the domain to `references/persona-index.md`
5. Update the main `SKILL.md` domain table

### Fix an Issue

Check the [Issues](https://github.com/evoputa/ai-advisory-board/issues) tab for open items.

---

## Persona Standards

Every leader profile must be based on **publicly documented** philosophy, frameworks, and decision-making approaches. This means:

- Published books, interviews, speeches, and documented business decisions
- No invented quotes or fabricated positions
- No speculation about private beliefs or unpublished views

The goal is accuracy to each leader's documented thinking, not creative interpretation.

---

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b add-leader-name`)
3. Make your changes
4. Ensure your additions follow existing formatting patterns
5. Submit a pull request with a clear description of what you added and why

---

## Code of Conduct

- Be respectful of the leaders represented in this project
- Ensure all persona content is based on public, verifiable sources
- Maintain the project's commitment to geographic and gender diversity
- No promotional or fictional personas

---

## Security

This repo uses [BF Git Guardian](https://github.com/evoputa/bf-git-guardian) to prevent accidental commits of sensitive data. If you clone this repo, run:

```bash
python .github/hooks/install-hooks.py
```

This installs the pre-commit hook that scans for personal paths, API keys, and sensitive patterns before every commit.

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
