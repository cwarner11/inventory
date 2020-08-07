### Inventory API

This is an open-ended problem with no definitive solution so one should aim to provide a simple but robust solution which others could easily use and extend. 
The solution should be implemented in any open-source language using only commonly available libraries. Defensive coding against malformed inputs is not required and terse simplicity should be favored where possible. Unit-tests are not required though the code should be structured in a way that would support them.

There is access to an API that gives a variety of information about the nodes (inventory-api).

Do the following:

1/ Write an API client that consumes the API and is able to do the following:

- Shows the total CPU, memory, and disk space of each group and allows us to limit to top-k results (invdb group-resources --limit 5)
- Checks for group overlap. Given two groups, print all nodes that are in both. (invdb group-overlap --groups foo,bar)

2/ Extend each command in Part 1 with a feature that one thinks would add value.

Notes:

- The inventory-api binary will start a server that listens on port 8080. Documentation for the api is served at [http://localhost:8080/]
- One may use any open-source language provided it can run on Mac OSX
  - Compile/run scripts, while not necessary, are appreciated
  - If using a compiled language, one must include the source files - we will recompile and use our build to test

*My code is located instructions, requirements, and invdb.py*

