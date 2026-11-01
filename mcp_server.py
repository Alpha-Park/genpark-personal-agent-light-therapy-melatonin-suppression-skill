# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Light Therapy Melatonin Suppression Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentLightTherapyMelatoninSuppression

mcp = FastMCP("PersonalAgentLightTherapyMelatoninSuppression")
client = PersonalAgentLightTherapyMelatoninSuppression()

@mcp.tool()
def calculate_melanopic_stimulus(
    photopic_lux: float,
    light_source: str = "sunlight",
    exposure_duration_minutes: float = 30.0
) -> str:
    """Calculates CIE S 026 mEDI lux, ipRGC activation, and pineal melatonin suppression."""
    import json
    return json.dumps(client.calculate_melanopic_stimulus(photopic_lux, light_source, exposure_duration_minutes), indent=2)

@mcp.tool()
def schedule_phototherapy_session(
    target_circadian_shift: str = "phase_advance",
    current_wake_time: str = "07:30",
    has_seasonal_depression: bool = False
) -> str:
    """Prescribes clinical phototherapy start time, lux intensity, and duration for circadian shifts."""
    import json
    return json.dumps(client.schedule_phototherapy_session(target_circadian_shift, current_wake_time, has_seasonal_depression), indent=2)

if __name__ == "__main__":
    mcp.run()
