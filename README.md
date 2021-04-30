# Blossom Algorithm

Implementation and animation of the Blossom algorithm to construct a maximum matching in any graph. The blossom algorithm is a polynomial time maximum graph matching algorithm that has a complexity O(|V<sup>2</sup>|x|E|). We have used [NetworkX](https://networkx.org/) along with [Matplotlib](https://matplotlib.org/) to maintain and visualize the graph. The animation is interactive and the steps of the algorithm can be viewed one-by-one by pressing the `enter` key while the program is executing. A video of the algorithm can be viewed in the `video/` folder.

## Team members

1. Bishal Pandia IMT2017010
2. Kaustubh Nair IMT2017025
3. Sarthak Khoche IMT2017038


## Prerequisites and Setup 

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

## Animations
Here are some animations of the algorithm:

<!-- <img src="/video/complete.gif?raw=true" > -->

<img src="/video/blossom.gif?raw=true" >

<img src="/video/path.gif?raw=true" >

## Algorithm

A step-by-step run through of the whole algorithm

### Initialization

A sample graph is first initialized with the help of `src/sample_graphs.py`

<img src="/imgs/Figure_1-0.png?raw=true" >

### Finding free vertices

All the free vertices with `matched` attribute as False are shown (yellow)

<img src="/imgs/Figure_1-1.png?raw=true" >

### Finding random vertex

A random vertex is picked from all the free vertices (red)

<img src="/imgs/Figure_1-2.png?raw=true" >

### Breadth First Search

With the random vertex as root, we start the BFS and highlight the next vertex (red)

<img src="/imgs/Figure_1-3.png?raw=true" >

If the next vertex is unmatched, we construct an augmenting path between them (yellow)

<img src="/imgs/Figure_1-4.png?raw=true" >

And then invert the augmenting path to increase its length by 1 (green)

<img src="/imgs/Figure_1-5.png?raw=true" >

In the case that next vertex is matched

<img src="/imgs/Figure_1-8.png?raw=true" >

We add the matched edge to the augmenting path initially (yellow)

<img src="/imgs/Figure_1-9.png?raw=true" >

We check the next vertex from root, if it is matched as well, that suggests presence of an odd cycle. We construct a blossom and shrink it to a `supernode` (visualization of blossom can be seen in `Animations` above)

If the next vertex from the root is unmatched, weconstruct an augmenting path from that edge instead (yellow)

<img src="/imgs/Figure_1-10.png?raw=true" >

And then invert it (green)

<img src="/imgs/Figure_1-11.png?raw=true" >

We keep repeating these step until we have no free vertex left. That is when we obtain the maximum matching (red) of the graph according to Edmonds' Blossom Algorithm 

<img src="/imgs/Figure_1-12.png?raw=true" >

## Brief about the code
Here is an overview about the files related to the implementation:

`src/sample_graphs.py` contains some example graphs which can be used for the algorithm.

`main.py` contains code regarding initialization of the graph, running the algorithm and animation of the graph.

`src/blossom.py` contains the implementation of the Blossom algorithm.

`src/helpers.py` contains helpers used for the animation.
