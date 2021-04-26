# Coloring animation

Animation is done by saving the intermediate states of the graph while running the algorithm. (states include, nodes, edges, and their colors) After the algorithm is over, these states are plotted one by one, on pressing `enter`.

## Coloring edges

Call `update_edge_color(colors, v1, v2, color_name)` to update the color of an edge. This function assigns some color to an edge.
Here,
1. `colors` is the dictionary passed in `blossom.run()`
2. `v1`, `v2` are the vertex numbers according to those present in `g.nodes()`
3. `color_name` is a string denoting color. Examples are `red`, `blue`, `black`,`green`, etc.

## Coloring vertices

Call `update_vertex_color(colors, v, color_name)` to update the color of a vertex. This function assigns some color to a vertex.
Here,
1. `colors` is the dictionary passed in `blossom.run()`
2. `v`, is the vertex number according to the one present in `g.nodes()`
3. `color_name` is a string denoting color. Examples are `red`, `blue`, `black`,`green`, etc.


## Updating data

`update(animation_data, g, colors)` MUST be called everytime after calling `update_edge_color()` and `update_vertex_color()` for it to show up in the animation. Basically, `update()` saves the current color states as an intermediate state - which will be a step in the animation.
The parameters need not be changed. If `update_vertex_color()` and `update_edge_color()` are both used at the same time for a step, `update(animation_data, g, colors)` should only be called once.

