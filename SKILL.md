---
name: genpark-personal-agent-light-therapy-melatonin-suppression-skill
version: "1.0.0"
description: "Zero-dependency Melanopic Equivalent Daylight Illuminance (mEDI / CIE S 026) calculator, ipRGC melanopsin retinal phototransduction modeler, and circadian phototherapy scheduler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Light Therapy Melatonin Suppression Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to optimize retinal circadian photobiology, calculate Melanopic Equivalent Daylight Illuminance (mEDI) per CIE S 026 standards, model pineal melatonin suppression, and schedule therapeutic light interventions.

## Agent In-Context Capabilities

- **CIE S 026 mEDI Calculation**: Distinguishes visual photopic lux from biological melanopic lux using source-specific Melanopic Daylight Ratios (MDR).
- **ipRGC Melanopsin Modeling**: Predicts 480nm photon absorption driving central suprachiasmatic nucleus (SCN) phase advancement.
- **Clinical Phototherapy Scheduling**: Prescribes 10,000 lux SAD protocols and enforces evening darkness (< 10 mEDI lux) to safeguard nocturnal sleep architecture.

## Tools Summary

1. `calculate_melanopic_stimulus`: Computes mEDI lux, melanopic dose units, and melatonin suppression percentage.
2. `schedule_phototherapy_session`: Prescribes start times, intensity levels, and durations for circadian phase shifting.
