from features import (
    name_similarity,
    package_similarity,
    icon_distance,
    cert_mismatch
)

def compute_score(sample, official):
    name_sim = name_similarity(sample["app_name"], official["app_name"])
    pkg_sim = package_similarity(sample["package_name"], official["package_name"])
    icon_dist = icon_distance(sample["icon_path"], official["icon_path"])
    cert_mis = cert_mismatch(sample["cert_fingerprint"], official["cert_fingerprint"])

    name_fake = 100 - name_sim
    pkg_fake = 100 - pkg_sim
    icon_fake = (icon_dist / 64) * 100

    score = (
        0.4 * name_fake +
        0.3 * pkg_fake +
        0.2 * icon_fake +
        0.1 * cert_mis
    )

    return round(score, 2)

def classify(score):
    if score < 30:
        return "Likely Safe"
    elif score < 60:
        return "Suspicious"
    else:
        return "Likely FAKE"
