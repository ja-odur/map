## __Map__ 
An app for creating and traversing through maps using graph datastructure. 


## ___Prerequisites___

* `Git` [Guide to Git](https://git-scm.com/doc) [Installing Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
* `Python 3.5 or higher`
* `Pip` [Guide to installing pip](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)
* `Pipenv` [Pipenv documentation](https://docs.pipenv.org/en/latest/)


## __Cloning and installing dependencies__
* After installing the **`prerequisites`** above, clone the repository Develop branch
using this command `git clone -b develop https://github.com/ja-odur/map.git`
* Change into the newly cloned repo through `cd map`

### __Installing virtual environment__
* Using pipenv, start the environment and install requirements
* $ **`pipenv shell`**
* $ **`pipenv install`**. That didn't work,  try **`pipenv install --skip-lock`** 


## __Usage__
* Import the Map class **`from map import Map`**
* Instantiate the Map class **`graph = Map(['place1', 'place2', 'place3'])`**
* Add edges between any of the places **`graph.add_edge('place1', 'place3')`**
* Find the shortest path between two places **`graph.shortest_path('place1', 'place3')`**
* Topologically sort DAG (Directed Acyclic Graphs) **`graph.topological_sort()`**
* Establish the minimum spanning tree **`graph.minimum_spanning_tree()`**
