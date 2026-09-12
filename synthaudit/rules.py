CHECKS = {
    "precursors": {
        "label": "Precursors or reagents",
        "weight": 15,
        "patterns": [r"\b(?:precursor|reagent|nitrate|chloride|oxide|acetate|carbonate|salt)\b"],
    },
    "quantity": {
        "label": "Quantities or concentrations",
        "weight": 12,
        "patterns": [r"\b\d+(?:\.\d+)?\s?(?:mg|g|kg|mmol|mol|mL|ml|L|M|mM|wt%)\b"],
    },
    "solvent": {
        "label": "Solvent and volume",
        "weight": 10,
        "patterns": [r"\b(?:solvent|water|ethanol|methanol|acetone|toluene|dmf)\b"],
    },
    "temperature": {
        "label": "Temperature",
        "weight": 12,
        "patterns": [r"(?:\b\d+(?:\.\d+)?\s?(?:°\s?)?[CFK]\b|room temperature)"],
    },
    "duration": {
        "label": "Reaction or treatment duration",
        "weight": 10,
        "patterns": [r"\b\d+(?:\.\d+)?\s?(?:h|hr|hrs|hour|hours|min|minutes|day|days)\b"],
    },
    "atmosphere": {
        "label": "Atmosphere",
        "weight": 8,
        "patterns": [r"\b(?:air|argon|nitrogen|oxygen|vacuum|inert atmosphere)\b"],
    },
    "pressure_ph": {
        "label": "Pressure or pH, where relevant",
        "weight": 7,
        "patterns": [r"\b(?:pH\s?\d+(?:\.\d+)?|\d+(?:\.\d+)?\s?(?:bar|atm|Pa|MPa|psi))\b"],
    },
    "post_processing": {
        "label": "Cooling, washing, or drying",
        "weight": 10,
        "patterns": [r"\b(?:cool(?:ed|ing)?|wash(?:ed|ing)?|dry|dried|drying|filtered|centrifuged)\b"],
    },
    "characterisation": {
        "label": "Characterisation method",
        "weight": 16,
        "patterns": [r"\b(?:XRD|PXRD|SEM|TEM|EDS|EDX|FTIR|Raman|TGA|DSC|NMR|ICP|UV[- ]?Vis)\b"],
    },
}
