# tc2website-flask (+ nextjs)
Hello, this is the flask implementation for tdc-2 website (UPDATE: with nextjs). Our documentation is still under development. For most matters, you can refer to the TDC repo.

We have developed a new, more decentralized method for adding entries to TDC leaderboards. Follow the following minimalist guide to add your entries.

To add your entry to the leaderboard, add your results to the corresponding leaderboard in this file
https://github.com/mims-harvard/tdc2website-flask/blob/main/benchmark/leaderboards.py
You must match the format for your leaderboard in that file. In short, the format is as follows:

1. On the fourth item of the list paired with your leaderboard, you will find a list with entries corresponding to the metadata for your entry and the 
mean value for the leaderboard metric. Fill out this information and add an entry to that list.

2. On the fifth item of the list paired to your leaderboard, you will find a list containing the metric value and standard deviation entries. Add your numbers to that list.

Last, create a PR for this repo and contact @amva13 or contact@tdcommons.ai for approval!

The PR must include the following in the description:

A. A link to the codes for training the model and running the benchmarks.

B. Instructions for replicating your results running these codes.

C. Description of the hardware used for training the model.

D. Link to paper to be included on the website

E. Paper authors and developers of the model.

F. The dictionary string output of running the TDC benchmark group evaluations.

See example here https://github.com/mims-harvard/tdc2website-flask/pull/2 . Please feel free to reach out with any questions.
