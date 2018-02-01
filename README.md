Intelligent Backtracking
====

Sudoku board solver through intelligent backtracking search. Legal input boards are solved to completion, and illegal input boards return an error indicating so.

### Methodology

Solving Sudoku boards by brute force permutation (e.g. simple depth-first backtracking search) most certainly works, but may take a very long time. In particular, if validation is only enforced on board completion, the vast majority of search paths will be wasteful. Here we take more intelligent approaches with several methods of pruning away the search tree.

#### 1. Validation

First, in our depth-first branching, validation is done upon node expansion, so that only legal additions are pursued. This is the first improved method, expandV(), implemented by the valid.py module. This is a step in the right direction, but is still an exhaustive trial-and-error approach that may take a rather long time depending on the initial board state.

#### 2. Forward-Checking

Second, we can do better if we enforce forward-checking upon generation of children nodes, instead of validating upon node expansion. This is implemented in the method expandFC(), with the check.py module. This is a strictly more efficient method, since it prunes away unworthy portions of the search tree earlier by ensuring arc consistency.

#### 3. Minimum-Remaining-Value Heuristic

 Third, for each layer, how do we decide on the order of children to search down? Here we use the MRV heuristic, which is implemented in the method expandMRV(), which uses the heap.py module. This is the most efficient method, since it further prunes the search tree by first eliminating paths that are most likely to fail.

### Instructions

To run the driver, type the following (if desired, input boards can be modified within driver.py):

	python driver.py

To run the animated version that shows the board being solved live on the console:

	python animate.py

### Output

The solution board found by each method is shown, together with the total number of boards searched. The relative efficiency of each of the three methods can be inspected, and the results are as expected. Note that, given a board location to search down, the choice of values to be searched is set to be the deterministic numerical priority. For random outcomes we could alternatively have set the priority to be the shuffled range(1, 10) instead; this does not affect the time complexity.

### Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
