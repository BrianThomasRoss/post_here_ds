"""takes raw text and obtains a prediction"""


def predict(post: str, n: int = 5) -> dict:
    """
    Serve subreddit predictions.
    
    Parameters
    ----------
    post : string
        Selftext that needs a home.
    n    : integer
        The desired name of the output file,
        not including the '.pkl' extension.

    Returns
    -------
    Python dictionary formatted as follows:
        [{'subreddit': 'PLC', 'proba': 0.014454},
         ...
         {'subreddit': 'Rowing', 'proba': 0.005206}]
    """
    
    # Vectorize the post -> sparse doc-term matrix
    post_vec = vocab.transform([post])
    
    # Generate predicted probabilities from trained model
    proba = nb.predict_proba(post_vec)
    
    # Wrangle into correct format
    return (pd
                .DataFrame(proba, columns=[le.classes_])  # Classes as column names
                .T  # Transpose so column names become index
                .reset_index()  # Pull out index into a column
                .rename(columns={"level_0": "subreddit", 0: "proba"})  # Rename for aesthetics
                .sort_values(by="proba", ascending=False)  # Sort by probability
                .iloc[:n]  # n-top predictions to serve
                .to_dict(orient="records")
               )

