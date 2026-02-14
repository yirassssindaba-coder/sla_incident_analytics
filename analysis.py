import sys
import pandas as pd
import matplotlib.pyplot as plt

REQUIRED = ["incident_id","opened_at","resolved_at","priority","status"]

def main(path: str):
    df = pd.read_csv(path)

    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing required columns: {missing}")

    df["opened_at"] = pd.to_datetime(df["opened_at"], errors="coerce")
    df["resolved_at"] = pd.to_datetime(df["resolved_at"], errors="coerce")

    # handle NA safely
    df["is_resolved"] = df["resolved_at"].notna() & (df["status"].str.lower() == "resolved")
    df["resolution_minutes"] = (df["resolved_at"] - df["opened_at"]).dt.total_seconds() / 60.0
    df.loc[~df["is_resolved"], "resolution_minutes"] = pd.NA

    # KPI
    total = len(df)
    resolved = int(df["is_resolved"].sum())
    avg_minutes = float(df["resolution_minutes"].dropna().mean()) if resolved else 0.0

    kpi = pd.DataFrame([{
        "total_incidents": total,
        "resolved_incidents": resolved,
        "avg_resolution_minutes": round(avg_minutes, 2)
    }])

    # trend by day
    df["opened_day"] = df["opened_at"].dt.date
    trend = df.groupby("opened_day").size().reset_index(name="incidents")

    out_kpi = "kpi_summary.csv"
    out_trend = "trend_by_day.csv"
    kpi.to_csv(out_kpi, index=False)
    trend.to_csv(out_trend, index=False)

    # plot
    plt.figure()
    plt.plot(trend["opened_day"].astype(str), trend["incidents"])
    plt.xticks(rotation=30, ha="right")
    plt.title("Incident Trend by Day")
    plt.tight_layout()
    plt.savefig("trend.png")

    print("Saved:", out_kpi, out_trend, "trend.png")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_incidents.csv"
    main(path)
