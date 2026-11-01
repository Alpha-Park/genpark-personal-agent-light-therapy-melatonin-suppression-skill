# -*- coding: utf-8 -*-
"""
Personal Agent Light Therapy Melatonin Suppression Client
Zero-dependency Melanopic Equivalent Daylight Illuminance (mEDI / CIE S 026) calculator,
ipRGC melanopsin retinal phototransduction modeler, and circadian phototherapy scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentLightTherapyMelatoninSuppression:
    """
    Quantifies melanopic biological illuminance, modeling intrinsically photosensitive retinal
    ganglion cell (ipRGC) activation, pineal melatonin suppression, and circadian phase resets.
    """

    def calculate_melanopic_stimulus(
        self,
        photopic_lux: float,
        light_source: str = "sunlight",
        exposure_duration_minutes: float = 30.0
    ) -> Dict[str, Any]:
        """
        Calculates Melanopic Equivalent Daylight Illuminance (mEDI lux) based on CIE S 026:
        mEDI = photopic_lux * Melanopic Daylight Efficacy Ratio (MDR).
        480nm wavelength sensitivity activates melanopsin in ipRGCs, driving cortisol and halting melatonin.
        """
        lux = max(1.0, min(150000.0, float(photopic_lux)))
        dur = max(1.0, min(720.0, float(exposure_duration_minutes)))
        src = str(light_source).lower()

        # CIE S 026 standard Melanopic Daylight Ratios (MDR)
        if "sun" in src or "natural" in src or "sky" in src:
            mdr = 1.10 # Clear daylight
            spectrum_desc = "Natural Full-Spectrum Sunlight (Rich 480nm melanopsin peak)"
        elif "phototherapy" in src or "sad_lamp" in src or "10000" in src:
            mdr = 0.95 # Commercial clinical phototherapy box
            spectrum_desc = "Clinical SAD Light Box (Enriched blue-cyan circadian stimulus)"
        elif "cool" in src or "6500" in src:
            mdr = 0.88 # 6500K Cool White LED
            spectrum_desc = "Cool White Daylight LED (High melanopic potency)"
        elif "office" in src or "4000" in src:
            mdr = 0.65 # Standard 4000K commercial fluorescent/LED
            spectrum_desc = "Standard Office Neutral White (Moderate melanopic efficacy)"
        elif "warm" in src or "2700" in src or "incandescent" in src:
            mdr = 0.45 # 2700K Warm White
            spectrum_desc = "Warm Domestic Incandescent/LED (Low melanopic disruption)"
        elif "candle" in src or "fire" in src:
            mdr = 0.20 # Candlelight
            spectrum_desc = "Candlelight / Firelight (Zero melanopsin activation)"
        else:
            mdr = 0.70
            spectrum_desc = "Generic Domestic Artificial Light"

        # Calculated Melanopic Equivalent Daylight Illuminance (mEDI)
        medi_lux = round(lux * mdr, 1)

        # Retinal ipRGC melanopic dose (mEDI * log(duration))
        melanopic_dose = round(medi_lux * math.log10(dur + 1.0), 1)

        # Melatonin suppression percentage (Hill equation approximation)
        # Half-maximal suppression occurs around ~100-150 mEDI lux
        ec50 = 120.0
        suppression_pct = round((math.pow(medi_lux, 1.4) / (math.pow(medi_lux, 1.4) + math.pow(ec50, 1.4))) * 100.0, 1)
        suppression_pct = min(99.0, max(0.0, suppression_pct))

        # Circadian biological impact classification
        if medi_lux >= 250.0:
            circadian_status = "Robust Daytime Circadian Entrainment (mEDI >= 250 lux)"
            action = "Ideal morning/midday biological signal. Promotes high alertness, elevated cortisol, and nighttime sleep pressure."
        elif medi_lux <= 10.0:
            circadian_status = "Circadian Nighttime Sanctuary (mEDI <= 10 lux)"
            action = "Zero pineal gland interference. Natural nocturnal melatonin synthesis uninhibited."
        else:
            circadian_status = "Circadian Twilight / Sub-Optimal Ambiguity (10 - 250 lux)"
            action = "Insufficient for morning circadian resetting; yet excessively bright if experienced within 3 hours of sleep."

        return {
            "measured_photopic_lux": lux,
            "light_source_type": spectrum_desc,
            "melanopic_daylight_ratio_mdr": mdr,
            "melanopic_equivalent_daylight_illuminance_medi_lux": medi_lux,
            "exposure_duration_minutes": dur,
            "iprgc_melanopic_dose_units": melanopic_dose,
            "pineal_melatonin_suppression_pct": f"{suppression_pct}% suppressed",
            "circadian_biological_state": circadian_status,
            "recommendation": action
        }

    def schedule_phototherapy_session(
        self,
        target_circadian_shift: str = "phase_advance",
        current_wake_time: str = "07:30",
        has_seasonal_depression: bool = False
    ) -> Dict[str, Any]:
        """
        Prescribes clinical phototherapy timing (light box or natural sunlight) to shift the
        human Phase Response Curve (PRC) for phase advancement, phase delay, or SAD management.
        """
        def parse_h(t_str: str) -> float:
            parts = str(t_str).split(":")
            return float(parts[0]) + (float(parts[1]) / 60.0 if len(parts) > 1 else 0.0)

        def format_h(h_val: float) -> str:
            hh = int(h_val) % 24
            mm = int((h_val - int(h_val)) * 60)
            return f"{hh:02d}:{mm:02d}"

        wake_h = parse_h(current_wake_time)
        shift = str(target_circadian_shift).lower()

        if "advance" in shift or "early" in shift:
            # Phase advance: Night owl desiring earlier sleep onset
            # Deliver bright light immediately upon waking (within 30-45 minutes)
            start_h = (wake_h + 0.25) % 24.0
            dur_mins = 30.0 if has_seasonal_depression else 20.0
            lux_target = 10000.0 if has_seasonal_depression else 5000.0
            protocol_desc = "Deliver 10,000 lux phototherapy within 30 min of waking to advance the central pacemaker (SCN)."
        elif "delay" in shift or "late" in shift:
            # Phase delay: Early bird wanting to stay awake later
            # Deliver light in late afternoon / early evening (17:00 - 19:00)
            start_h = 17.5
            dur_mins = 30.0
            lux_target = 2500.0
            protocol_desc = "Deliver late afternoon photic stimulus to suppress early evening melatonin and shift sleep phase later."
        else:
            # General circadian synchronization
            start_h = (wake_h + 0.5) % 24.0
            dur_mins = 20.0
            lux_target = 5000.0
            protocol_desc = "Standard morning photic anchor to lock in 24-hour master clock synchronization."

        return {
            "target_circadian_strategy": "Circadian Phase Advance (Earlier Sleep Onset)" if "advance" in shift else "Circadian Synchronization",
            "session_start_time": format_h(start_h),
            "session_duration_minutes": dur_mins,
            "target_retinal_intensity_lux": lux_target,
            "seasonal_affective_disorder_mode": "Active (10,000 lux protocol)" if has_seasonal_depression else "Inactive (Standard circadian maintenance)",
            "clinical_protocol_rationale": protocol_desc,
            "evening_countermeasure": "Enforce < 10 mEDI lux and wear 480nm amber blue-blockers starting 2.5 hours before target sleep."
        }
