import pandas as pd


def generate_report(results):

    df = pd.DataFrame(results)

    df.to_csv(
        "outputs/delivery_summary.csv",
        index=False
    )

    print("Report Generated Successfully")