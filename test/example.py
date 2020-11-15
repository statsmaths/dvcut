import numpy as np
from dvcut.core import DataExtraction, FrameInput
from dvcut.annotate.diff import DiffAnnotator
from dvcut.aggregate.cut import CutAggregator
from dvcut.aggregate.cut import CutAggregator

# Extract the frame by frame differences
dextra = DataExtraction(FrameInput(input_path="Dickvandykeshow19650915excerpt.mp4"))
#dextra = DataExtraction(FrameInput(input_path="bw_s04_e19.mp4"))
dextra.run_annotators([DiffAnnotator(quantiles=[40])])
diff = dextra.get_data()['diff']

# Look at largest differences (hint at tuning parameters)
np.sort(diff['q40'].array)[-20:]
np.sort(diff['h40'].array)[-20:]

# Detect Shots
dextra.run_aggregator(CutAggregator(
    min_len=10,
    cut_vals={'q40': 6, 'h40': 0.10}
))
shots = dextra.get_data()['cut']
shots

# Compute metrics
print("MSL: {:.3f}".format(shots['time_diff'].median()))
print("ASL: {:.3f}".format(shots['time_diff'].mean()))
