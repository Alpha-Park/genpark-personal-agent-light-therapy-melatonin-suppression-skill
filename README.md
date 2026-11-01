# Personal Agent Light Therapy Melatonin Suppression Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Melanopic Equivalent Daylight Illuminance (mEDI / CIE S 026) calculator, ipRGC melanopsin retinal phototransduction modeler, and circadian phototherapy scheduler.

## Architecture

```mermaid
flowchart TD
    LightInput[Photopic Lux & Spectrum Source] --> MEDIEngine[CIE S 026 mEDI Calculation Engine]
    MEDIEngine --> MelanopsinDose[ipRGC Retinal Dose & Melatonin Suppression %]
    WakeTime[Individual Wake Time & Chronotype] --> PhototherapyScheduler[Phase Response Curve PRC Scheduler]
    PhototherapyScheduler --> ClinicalProtocol[10,000 Lux Light Box & Evening Blackout Strategy]
```

## Quickstart

```python
from client import PersonalAgentLightTherapyMelatoninSuppression

agent = PersonalAgentLightTherapyMelatoninSuppression()
res = agent.calculate_melanopic_stimulus(photopic_lux=2500.0, light_source="sunlight")
print(f"mEDI: {res['melanopic_equivalent_daylight_illuminance_medi_lux']} lux | Melatonin Suppression: {res['pineal_melatonin_suppression_pct']}")
```
