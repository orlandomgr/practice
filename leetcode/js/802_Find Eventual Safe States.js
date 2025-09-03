function isSafe(node, graph, visited, safe) {
    if (safe[node]) {
        return safe[node];
    }
    if (visited[node]) {
        return safe[node];
    }
    visited[node] = true;
    safe[node] = true;
    for (let i in graph[node]) {
        if (isSafe(graph[node][i], graph, visited, safe)) {
            return true;
        }
    }
    safe[node] = false;
    return false;
}

/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function (graph) {
    let visited = new Array(graph.length);
    let safe = new Array(graph.length);

    for (let i = 0; i < graph.length; i++) {
        isSafe(i, graph, visited, safe);
    }

    let result = [];
    for (let i = 0; i < safe.length; i++) {
        if (!safe[i]) {
            result.push(i);
        }
    }

    return result;
};

console.log(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])); // [2,4,5,6]
console.log(eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])); // [4]

