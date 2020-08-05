# Inventory API

------
This is an open-ended problem with no definitive solution so you should aim to provide a simple but robust solution which others could easily use and extend. We ask you to complete this challenge within 48 hours of downloading it, but don’t expect you to spend more than a few hours on it.
Your solution should be implemented in any open-source language using only commonly available libraries. Defensive coding against malformed inputs is not required and terse simplicity should be favored where possible. Unit-tests are not required though your code should be structured in a way that would support them.
Your submission should include:
•         source code
•         instructions on how to build and execute your code
•         ideas for further improvements you’d make if given more time
To accept please:
•         download the challenge from here
•         email your solution to me when ready to submit
!! Please return the solution within 48 hours of clicking the link above !!

You have access to an API that gives you a variety of information about the nodes (inventory-api).

Do the following:

1/ Write an API client that consumes the API and is able to do the following:

- Shows the total CPU, memory, and disk space of each group and allows us to limit to top-k results (invdb group-resources --limit 5)
- Checks for group overlap. Given two groups, print all nodes that are in both. (invdb group-overlap --groups foo,bar)

2/ Extend each command in Part 1 with a feature that you think would add value.

3/ (Discussion Only)

- What would you add to the inventory API to make it more useful?
- What is another feature you would add to the client to help examine the current inventory?
- What other uses are there for this type of API in large-scale infrastructure?

Notes:

- The inventory-api binary will start a server that listens on port 8080. Documentation for the api is served at [http://localhost:8080/]
- You may use any open-source language of your choice, provided it can run on Mac OSX
  - Compile/run scripts, while not necessary, are appreciated
  - If you are using a compiled language, you must include the source files - we will recompile and use our build to test
- You will have 48 hours to upload a solution from when you downloaded this assignment, but you should spend a maximum of three hours working on it
- Please put answers to discussion questions in a flat-text file (txt, md, rst, etc...) in the parent directory of the submission
