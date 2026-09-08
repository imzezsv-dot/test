# Not the deliverable — see `imzezsv-dot/vocalyze`

This repository holds an **early snapshot** of the Vocalyze integration and
privacy component. It was a scratch repository during development and is no
longer maintained.

## → The submitted project is at **https://github.com/imzezsv-dot/vocalyze**

Everything for review, grading and the demo is there.

---

### Why this repository should not be reviewed

It is missing most of what makes the component reviewable:

| | This repository | `imzezsv-dot/vocalyze` |
|---|---|---|
| Test suite | none | 121 tests, no network, no model weights |
| Group notebook | none | `notebooks/Vocalyze.ipynb`, all four components |
| Demo generator | none | `tools/make_demo.py` |
| Retention sweeper hardening | no | yes |
| Honest demo-mode badging | no | yes |
| Docs | partial | `README` · `API` · `PRIVACY` · `INTEGRATION` · `HANDOVER` |

The code here also predates several fixes, including one that let plaintext
audio survive a crashed process.

**If you were given a link to this repository, use the one above instead.**
