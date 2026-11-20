"""Single source of truth for the FICTIONAL AeroPure AQ-200 product docs.

Everything here is invented for a demo. No real company, product, customer or
internal data. "Nimbus Home Appliances" and "AeroPure" are fictional names.
"""

COMPANY = "Nimbus Home Appliances (fictional)"
DISCLAIMER = "FICTIONAL SAMPLE - FOR DEMO ONLY. Not a real product. Contains no confidential data."

MODELS = ["AQ-200 Lite", "AQ-200", "AQ-200 Pro"]

SPECS = [
    # (row label, Lite, Standard, Pro)
    ("CADR (smoke, m3/h)", "220", "320", "450"),
    ("Recommended room size", "15-25 m2", "25-38 m2", "38-55 m2"),
    ("Main filter (part no.)", "H13 HEPA + carbon (FL-200H)", "H13 HEPA + carbon (FL-200H)", "H13 HEPA + carbon (FL-200P)"),
    ("UV-C sterilization lamp", "No", "No", "Yes (UV-200)"),
    ("Sensors", "Laser PM2.5", "Laser PM2.5", "Laser PM2.5 + VOC"),
    ("Noise (sleep / max)", "24 / 50 dB", "22 / 52 dB", "20 / 55 dB"),
    ("Max power consumption", "28 W", "38 W", "55 W"),
    ("Standby power", "< 0.5 W", "< 0.5 W", "< 0.5 W"),
    ("Input voltage", "100-240 V AC, 50/60 Hz", "100-240 V AC, 50/60 Hz", "100-240 V AC, 50/60 Hz"),
    ("Wi-Fi / app control", "No", "Yes (2.4 GHz)", "Yes (2.4 GHz)"),
    ("Remote control", "No", "Optional (RC-200)", "Included"),
    ("Weight", "4.2 kg", "5.6 kg", "7.8 kg"),
    ("Dimensions (W x D x H)", "24 x 24 x 45 cm", "27 x 27 x 55 cm", "32 x 32 x 66 cm"),
    ("Warranty", "2 years", "2 years", "3 years"),
    ("List price (USD)", "$149", "$229", "$349"),
]

UNIT_PRICE = {"AQ-200 Lite": 149, "AQ-200": 229, "AQ-200 Pro": 349}

SETUP_STEPS = [
    "Unbox the purifier and remove ALL plastic packaging from the main filter (the filter ships sealed in a plastic bag inside the unit).",
    "Place the purifier on a flat, hard floor at least 30 cm away from walls, curtains and furniture. Do not place it on carpet with long pile.",
    "Plug the power cable into a 100-240 V outlet. Avoid shared multi-plug extension cords.",
    "Press and hold the Power button for 3 seconds. The ring light turns white and the unit starts in Auto mode.",
    "Let the sensor calibrate for the first 10 minutes. During calibration the air-quality ring blinks blue; do not move the unit.",
    "(AQ-200 and AQ-200 Pro only) Install the AeroPure Home app, then press and hold Wi-Fi + Timer for 5 seconds until the Wi-Fi icon blinks, and follow the in-app pairing. Only 2.4 GHz networks are supported.",
    "Choose a mode: Auto (recommended), Sleep (lowest noise, display off), or manual fan speed 1-4 (Turbo = speed 4).",
]

MAINTENANCE = [
    # (component, interval, action, models)
    ("Pre-filter (PF-200, washable)", "Every 2 weeks", "Vacuum or rinse with water; dry fully (24 h) before reinstalling.", "All"),
    ("Exterior and air inlets", "Every month", "Wipe with a dry soft cloth. No solvents.", "All"),
    ("PM2.5 sensor lens", "Every 2 months", "Open the sensor cover on the side; clean lens with a dry cotton swab.", "All"),
    ("Main filter (FL-200H / FL-200P)", "Every 6 months (normal use) or every 4 months with pets, smoking or heavy cooking", "Replace the filter, then hold Filter Reset for 3 seconds.", "All"),
    ("UV-C lamp (UV-200)", "Every 12 months (8,000 operating hours)", "Replace the lamp module; unit must be unplugged.", "Pro only"),
    ("Fan and internal duct inspection", "Every 24 months", "Inspection by an authorized service center (labor fee applies outside warranty).", "All"),
]

ERROR_CODES = [
    # (code, meaning, likely cause, fix, models)
    ("E01", "Filter not detected", "Main filter missing or not seated correctly", "Open the back cover and push the filter in until it clicks. Close the cover firmly.", "All"),
    ("E02", "Filter life expired", "Filter has reached its rated life (about 2,160 h)", "Replace the main filter (FL-200H for Lite/AQ-200, FL-200P for Pro), then hold Filter Reset for 3 s.", "All"),
    ("E03", "Airflow blocked (packaging)", "Plastic bag not removed from a new filter; shows within the first 30 minutes of use", "Unplug, remove the plastic bag from the filter, reinstall and restart.", "All"),
    ("E04", "Fan motor stalled", "Foreign object in the fan or a failed motor", "Unplug, remove any object from the outlet grille. If E04 returns, contact service (motor part FM-200 / FM-200P).", "All"),
    ("E05", "Fan speed abnormal", "Dust build-up on the fan or unstable power", "Clean the pre-filter and inlets, plug directly into a wall outlet. If it persists, contact service.", "All"),
    ("E06", "PM2.5 sensor dirty", "Dust on the sensor lens; readings stuck high", "Clean the sensor lens with a dry cotton swab (see maintenance).", "All"),
    ("E07", "PM2.5 sensor failure", "Sensor module not responding", "Restart the unit. If E07 persists, replace sensor module SN-PM25.", "All"),
    ("E08", "VOC sensor failure", "VOC sensor not responding", "Restart the unit. If E08 persists, replace VOC sensor SN-VOC.", "Pro only"),
    ("E09", "Front cover open", "Safety interlock switch detects an open cover", "Close the front cover until it clicks. The fan will not run while the cover is open.", "All"),
    ("E10", "Over-temperature", "Internal temperature above 60 C, usually blocked inlet or heat source nearby", "Unit shuts down automatically. Move it at least 1 m from heaters, clear the inlets, wait 30 minutes, restart.", "All"),
    ("E11", "Wi-Fi connection failed", "Wrong password, 5 GHz network, or router out of range", "Use a 2.4 GHz network, then hold Wi-Fi for 5 s to reset networking and pair again.", "AQ-200, Pro"),
    ("E12", "Firmware update failed", "Power or network lost during an update", "Keep the unit plugged in and retry from the app. To recover, hold Power + Mode for 10 s.", "AQ-200, Pro"),
    ("E13", "UV-C lamp fault", "UV-C lamp at end of life or disconnected", "Replace the UV-C lamp module UV-200. The purifier keeps filtering without UV-C.", "Pro only"),
    ("E14", "Input voltage abnormal", "Voltage outside 100-240 V or unstable extension cord", "Plug directly into a grounded wall outlet. Do not use voltage converters.", "All"),
    ("E15", "Control panel not responding", "Moisture or dirt on the touch panel, or panel board fault", "Wipe the panel dry, unplug for 1 minute and restart. If it persists, replace control board CP-200 at a service center.", "All"),
]

FAQ = [
    ("Can I wash the main HEPA filter?", "No. Only the pre-filter (PF-200) is washable. Washing the HEPA/carbon filter destroys it."),
    ("Can I use the purifier in a bathroom?", "No. Do not use the purifier where relative humidity is above 80% or where it can be splashed with water."),
    ("Why is the air-quality ring red right after I turn it on?", "During the first 10 minutes the sensor is calibrating. If the ring stays red for more than 1 hour in a closed room, clean the PM2.5 sensor lens."),
    ("Does the purifier remove viruses?", "The H13 HEPA filter captures 99.95% of particles at 0.3 microns in lab tests. AeroPure makes no medical claims."),
    ("Does the AQ-200 support 5 GHz Wi-Fi?", "No. Only 2.4 GHz Wi-Fi is supported on AQ-200 and AQ-200 Pro. The Lite has no Wi-Fi."),
    ("How do I turn on child lock?", "Hold the Lock (padlock) button for 3 seconds. Hold again for 3 seconds to unlock."),
    ("How long does a filter last?", "About 6 months (2,160 h) in normal use, or about 4 months with pets, smoking or heavy cooking. The filter indicator turns red at end of life."),
    ("Is the filter the same for all models?", "No. AQ-200 Lite and AQ-200 use FL-200H. AQ-200 Pro uses the larger FL-200P."),
    ("What does the warranty cover?", "Manufacturing defects for 2 years (Lite, AQ-200) or 3 years (Pro). Filters, pre-filters and UV-C lamps are consumables and are not covered."),
]

PARTS = [
    # (part no, description, compatible, price USD)
    ("FL-200H", "Main filter H13 HEPA + activated carbon", "AQ-200 Lite, AQ-200", 39),
    ("FL-200P", "Main filter H13 HEPA + activated carbon (large)", "AQ-200 Pro", 59),
    ("FL-200H-2", "Value pack: 2 x FL-200H", "AQ-200 Lite, AQ-200", 70),
    ("PF-200", "Washable pre-filter", "All models", 12),
    ("SN-PM25", "Laser PM2.5 sensor module", "All models", 24),
    ("SN-VOC", "VOC sensor module", "AQ-200 Pro", 29),
    ("UV-200", "UV-C lamp module", "AQ-200 Pro", 35),
    ("FM-200", "Fan motor assembly", "AQ-200 Lite, AQ-200", 68),
    ("FM-200P", "Fan motor assembly (high flow)", "AQ-200 Pro", 82),
    ("CP-200", "Control panel board", "All models", 45),
    ("PSU-200", "Power supply cable / adapter", "All models", 22),
    ("RC-200", "Infrared remote control", "AQ-200, AQ-200 Pro", 15),
]
SERVICE_FEES = [
    ("Service labor, in warranty", 0),
    ("Service labor, out of warranty (flat per visit)", 25),
    ("Fan/duct inspection (24-month check)", 25),
]

MONTHS = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026", "May 2026", "Jun 2026",
          "Jul 2026", "Aug 2026", "Sep 2026", "Oct 2026"]
UNITS = {
    "AQ-200 Lite": [410, 385, 450, 520, 610, 700, 760, 690, 560, 530],
    "AQ-200":      [620, 590, 680, 760, 880, 1020, 1105, 980, 840, 800],
    "AQ-200 Pro":  [210, 205, 240, 290, 345, 410, 455, 420, 360, 350],
}
TICKET_CATS = ["Filter", "Sensor", "Wi-Fi/App", "Noise", "Other"]
TICKETS = [  # per month, in TICKET_CATS order
    [38, 12, 25, 9, 7],
    [35, 10, 22, 8, 6],
    [41, 14, 47, 10, 8],
    [44, 13, 30, 11, 9],
    [52, 15, 28, 12, 10],
    [60, 18, 26, 15, 11],
    [66, 21, 29, 17, 12],
    [63, 35, 27, 16, 11],
    [55, 19, 24, 13, 10],
    [51, 17, 22, 12, 9],
]
RESOLUTION_H = [20.5, 19.8, 31.2, 22.4, 21.0, 23.5, 24.1, 26.8, 21.7, 19.9]
CSAT = [4.4, 4.5, 3.9, 4.3, 4.4, 4.3, 4.2, 4.0, 4.4, 4.5]
REPORT_NOTES = [
    "March 2026: firmware 2.3 caused Wi-Fi reconnect issues (E11) on AQ-200 and AQ-200 Pro; fixed by firmware 2.3.1 on 28 March.",
    "June-July 2026: seasonal peak (summer haze season in the fictional sales region).",
    "August 2026: high humidity led to more E06 'sensor dirty' tickets; a sensor-cleaning reminder was added to the app in September.",
]
