def recommend_funds(risk_appetite, df):

    return (
        df[
            df['risk_grade']
            .str.lower()
            ==
            risk_appetite.lower()
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )