class Graph{
    constructor(){
        this.numberOfNodes = 0;
        this.adjacentList = {};
    }
    addVertex(node){
        this.adjacentList[node] = [];
        this.numberOfNodes++;
    }
    addEdge(node1, node2){
        //* undirected Graph 
        this.adjacentList[node1].push(node2);
        this.adjacentList[node2].push(node1);
    }
    showConnections(){
        const allNodes = Object.keys(this.adjacentList);
        for(let node of allNodes){
            let nodeConnections = this.adjacentList[node];
            let connections = "";
            for(let vertex of nodeConnections){
                connections += vertex + " ";
            }
            console.log(node + "-->" + connections);
        }
    }

}
const myGraph = new Graph();
myGraph.addVertex('1');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');
myGraph.addVertex('8');

console.log(myGraph);
myGraph.addEdge('3', '5');
myGraph.addEdge('6', '3');
myGraph.addEdge('1', '6');
myGraph.addEdge('1', '3');
myGraph.addEdge('1', '4');
myGraph.addEdge('4', '5');
myGraph.addEdge('8', '4');
console.log(myGraph);
myGraph.showConnections();
