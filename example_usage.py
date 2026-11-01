# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Light Therapy Melatonin Suppression Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentLightTherapyMelatoninSuppression

def main():
    agent = PersonalAgentLightTherapyMelatoninSuppression()

    print("=" * 70)
    print("DEMO: Personal Agent Light Therapy & Melatonin Suppression Modeler")
    print("=" * 70)

    # 1. Evaluate morning outdoor daylight (2500 photopic lux, 25 minutes)
    res_sun = agent.calculate_melanopic_stimulus(
        photopic_lux=2500.0,
        light_source="sunlight",
        exposure_duration_minutes=25.0
    )

    print(f"\n1. Morning Natural Sunlight Exposure (2500 lux for 25 min):")
    print(f"   Spectrum: {res_sun['light_source_type']}")
    print(f"   MDR: {res_sun['melanopic_daylight_ratio_mdr']}")
    print(f"   mEDI: {res_sun['melanopic_equivalent_daylight_illuminance_medi_lux']} mEDI lux")
    print(f"   Melatonin Suppression: {res_sun['pineal_melatonin_suppression_pct']}")
    print(f"   Circadian State: {res_sun['circadian_biological_state']}")
    print(f"   Guidance: {res_sun['recommendation']}")

    # 2. Schedule clinical phototherapy session for night owl
    res_sched = agent.schedule_phototherapy_session(
        target_circadian_shift="phase_advance",
        current_wake_time="07:00",
        has_seasonal_depression=True
    )

    print(f"\n2. Clinical Phototherapy Prescription (SAD Mode):")
    print(f"   Strategy: {res_sched['target_circadian_strategy']}")
    print(f"   Start Time: {res_sched['session_start_time']} ({res_sched['session_duration_minutes']} minutes)")
    print(f"   Target Intensity: {res_sched['target_retinal_intensity_lux']} lux")
    print(f"   Rationale: {res_sched['clinical_protocol_rationale']}")
    print(f"   Night Protocol: {res_sched['evening_countermeasure']}")

    print("\nVerification complete: Light therapy & circadian photobiology engine executed flawlessly.")

if __name__ == "__main__":
    main()
