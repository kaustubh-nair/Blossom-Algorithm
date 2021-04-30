# Blossom Algorithm

Implementation and animation of the Blossom algorithm to construct a maximum matching in any graph. The blossom algorithm is a polynomial time maximum graph matching algorithm that has a complexity `O(|V|x|E<sup>2</sup>|)`. We have used [NetworkX](https://networkx.org/) along with [Matplotlib](https://matplotlib.org/) to maintain and visualize the graph. The animation is interactive and the steps of the algorithm can be viewed one-by-one by pressing the `enter` key while the program is executing. A video of the algorithm can be viewed in the `video/` folder.

## Prerequisites and Setup 
Make sure your Python version is 3.6.x

To install dependencies, run
```
$ pip install -r requirements.txt
```

## Usage

To run the algorithm, in your terminal, enter

```
$ python main.py
```

Press the `enter` key to update graph and view the next step in the algorithm.


## Algorithm

## Brief about the code
Here is an overview about the files related to the implementation:

`src/sample_graphs.py` contains some example graphs which can be used for the algorithm.

`main.py` contains code regarding initialization of the graph, running the algorithm and animation of the graph.

`src/blossom.py` contains the implementation of the Blossom algorithm.

`src/helpers.py` contains helpers used for the animation.
