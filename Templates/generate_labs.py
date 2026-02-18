#!/usr/bin/env python3
"""Generate challenge-based DIY lab HTML for all 21 MS Demoland courses."""
import os

BASE = r"c:\Users\erikkuris\Git Directories\MS Demoland"

# ── Course definitions ───────────────────────────────────────────────
# Each course: (path_relative_to_BASE, title, tagline, duration, tasks[])
# Each task: (task_title, challenge_text, hints[], solution_text)

COURSES = [
    # ─── Developer / Beginner ────────────────────────────────────────
    {
        "path": "Developer/Beginner/Intro-to-VS-Code-and-GitHub-Copilot",
        "title": "AI Pair Programming - The Copilot Awakens",
        "tagline": "Get hands-on with GitHub Copilot in VS Code, from first activation to configuring your workspace and letting AI accelerate every keystroke",
        "duration": "30 Minutes",
        "prereqs": [
            "VS Code installed (latest stable)",
            "GitHub account with Copilot access",
            "Git CLI installed and authenticated",
        ],
        "tasks": [
            {
                "name": "Install and Activate Copilot",
                "challenge": "Install the GitHub Copilot and GitHub Copilot Chat extensions in VS Code, sign in with your GitHub account, and verify that Copilot is active by checking the status-bar icon.",
                "hints": [
                    "Open the Extensions panel (<kbd>Ctrl+Shift+X</kbd>) and search for <strong>GitHub Copilot</strong>.",
                    "After installing, click the Copilot icon in the status bar — it should show <em>Ready</em>.",
                    "If prompted, authorize the OAuth flow in your browser and return to VS Code.",
                ],
                "solution": "Install both <strong>GitHub Copilot</strong> and <strong>GitHub Copilot Chat</strong> from the Extensions marketplace. Click <em>Sign in to GitHub</em> when prompted, complete the browser OAuth flow, and confirm the status-bar icon shows a green check.",
            },
            {
                "name": "Configure Your Workspace",
                "challenge": "Create a <code>.vscode/settings.json</code> file in a new project folder that enables Copilot for all file types and sets your preferred suggestion behavior.",
                "hints": [
                    "Use <code>\"github.copilot.enable\": { \"*\": true }</code> to activate for all languages.",
                    "Set <code>\"editor.inlineSuggest.enabled\": true</code> to see ghost-text completions.",
                    "Add <code>\"github.copilot.chat.localeOverride\": \"en\"</code> if you want English responses.",
                ],
                "solution": "Create <code>.vscode/settings.json</code> with Copilot enabled for all file types, inline suggestions turned on, and any locale or editor preferences you want. Reload the window to confirm the settings take effect.",
            },
            {
                "name": "AI-Assisted Coding",
                "challenge": "Create a new JavaScript file, write a function comment describing a utility (e.g., \"calculate the factorial of n\"), and let Copilot generate the implementation. Then open Chat and ask it to add error handling.",
                "hints": [
                    "Start with a comment like <code>// Calculate the factorial of a non-negative integer n</code> and press <kbd>Enter</kbd>.",
                    "Accept the ghost-text suggestion with <kbd>Tab</kbd>.",
                    "Open Copilot Chat (<kbd>Ctrl+Shift+I</kbd>) and ask: <em>Add input validation and error handling to this function</em>.",
                ],
                "solution": "Write a descriptive comment, accept Copilot's inline suggestion for the function body, then use Chat to add <code>if (n &lt; 0) throw new Error()</code> and other guards. Verify the function works by running it in the terminal.",
            },
        ],
    },
    {
        "path": "Developer/Beginner/MCP-for-You-and-Me",
        "title": "MCP Integration - MCP for You and Me",
        "tagline": "Discover what the Model Context Protocol is, plug in GitHub's public MCP server, and work issues end-to-end without leaving your editor",
        "duration": "30 Minutes",
        "prereqs": [
            "VS Code with GitHub Copilot Chat installed",
            "GitHub account with repo access",
            "Node.js 18+ installed",
        ],
        "tasks": [
            {
                "name": "Understand MCP Basics",
                "challenge": "Read the MCP overview and explain in your own words (a) what the Model Context Protocol does, (b) who publishes MCP servers, and (c) how they connect to your editor.",
                "hints": [
                    "MCP is a standard that lets AI tools call external services for live data.",
                    "GitHub, third parties, and you can publish MCP servers.",
                    "VS Code discovers them via <code>mcp.json</code> or workspace settings.",
                ],
                "solution": "MCP is an open protocol that lets Copilot call external <em>tool servers</em> for live context — repository data, databases, APIs, etc. Servers are registered in <code>.vscode/mcp.json</code> and Copilot invokes their tools during chat sessions.",
            },
            {
                "name": "Connect the GitHub MCP Server",
                "challenge": "Add GitHub's public MCP server to your workspace so Copilot Chat can query your repos, issues, and PRs in real time.",
                "hints": [
                    "Create or edit <code>.vscode/mcp.json</code> in your project root.",
                    "The server entry needs a <code>command</code> (npx) and the package name <code>@github/mcp-server</code>.",
                    "Restart Copilot Chat after saving the file.",
                ],
                "solution": "Create <code>.vscode/mcp.json</code> with an entry for <code>@github/mcp-server</code> using the npx command, provide your GitHub token via an environment variable, and restart Chat. Verify by asking Copilot to list your recent issues.",
            },
            {
                "name": "Work Issues End-to-End",
                "challenge": "Using only Copilot Chat (with MCP), create an issue in your test repo, triage it by adding labels, make a code fix, and close the issue — all without touching the browser.",
                "hints": [
                    "Ask Chat: <em>Create an issue titled 'Fix login timeout' in my repo</em>.",
                    "Then: <em>Add the 'bug' and 'priority:high' labels to that issue</em>.",
                    "Finally, make the fix, push, and ask Chat to close the issue with a reference to your commit.",
                ],
                "solution": "Use Chat to create the issue, add labels, and close it — MCP calls the GitHub API behind the scenes. Push your code fix referencing the issue number, then confirm the issue is closed on GitHub.",
            },
        ],
    },
    {
        "path": "Developer/Beginner/Prompts-Instructions-Agents-and-Chats",
        "title": "Copilot Primitives - Prompts, Instructions, Skills, and Agents",
        "tagline": "Learn the building blocks of Copilot's interaction models, when to reach for each one, and how to craft prompts that deliver reliable results",
        "duration": "30 Minutes",
        "prereqs": [
            "VS Code with GitHub Copilot extensions",
            "A sample project with at least two files",
            "Familiarity with basic Copilot usage",
        ],
        "tasks": [
            {
                "name": "Craft Effective Prompts",
                "challenge": "Write three prompts for Copilot Chat that produce different results: one vague prompt, one specific prompt, and one with full context. Compare the quality of each response.",
                "hints": [
                    "Vague: <em>fix the bug</em>. Specific: <em>fix the null-check bug in auth.js line 42</em>.",
                    "Full context: include the file path, error message, and expected behavior.",
                    "Notice how more context leads to more accurate, actionable suggestions.",
                ],
                "solution": "Send all three prompts and observe the difference. The full-context prompt should produce a targeted fix, while the vague one may hallucinate or suggest irrelevant changes. Document the pattern: <strong>context + intent + constraints = reliable output</strong>.",
            },
            {
                "name": "Create Custom Instructions",
                "challenge": "Create a <code>.github/copilot-instructions.md</code> file for your project that sets coding standards, then create a <code>.instructions.md</code> file scoped to a specific folder.",
                "hints": [
                    "<code>.github/copilot-instructions.md</code> applies repo-wide — put coding style, framework rules here.",
                    "<code>.instructions.md</code> in a folder applies only to files in that folder.",
                    "Try instructions like: <em>Always use TypeScript strict mode</em> or <em>Prefer async/await over callbacks</em>.",
                ],
                "solution": "Create <code>.github/copilot-instructions.md</code> with your repo-wide standards. Then create <code>src/.instructions.md</code> with folder-specific rules. Ask Copilot a question about code in that folder and verify it follows both instruction files.",
            },
            {
                "name": "Build a Skill and Agent",
                "challenge": "Create a reusable <code>.prompt.md</code> skill file that packages a multi-step workflow, then wire it into a custom agent mode via <code>.agent.md</code>.",
                "hints": [
                    "A skill file (<code>.prompt.md</code>) is a reusable prompt template with YAML front matter.",
                    "An agent file (<code>.agent.md</code>) defines a persona with tool access and can reference skills.",
                    "Use <code>applyTo</code> in front matter to scope when the skill is available.",
                ],
                "solution": "Create <code>.github/skills/review.prompt.md</code> with a code-review workflow template. Create <code>.github/agents/reviewer.agent.md</code> that references the skill and has access to terminal and file tools. Switch to the agent in Chat and see it follow the workflow.",
            },
        ],
    },
    # ─── Developer / Intermediate ────────────────────────────────────
    {
        "path": "Developer/Intermediate/Agent-Potato-License-to-Chat",
        "title": "Full AI Stack - Agent Potato: License to Chat",
        "tagline": "Follow Agent Potato on a mission to build a complete React frontend and Node backend, from first feature to deployment, all in one session",
        "duration": "1.5 Hours",
        "prereqs": [
            "VS Code with GitHub Copilot extensions",
            "Node.js 18+ and npm installed",
            "Basic React and Express knowledge",
        ],
        "tasks": [
            {
                "name": "Scaffold the React Frontend",
                "challenge": "Use Copilot agent mode to generate a React application skeleton with routing, a layout component, and at least two page stubs.",
                "hints": [
                    "Ask agent mode: <em>Create a React app with React Router, a navbar layout, and Home + About pages</em>.",
                    "Let the agent run <code>npx create-react-app</code> or <code>npm create vite@latest</code>.",
                    "Review the generated files and ask for adjustments if the folder structure differs from your preference.",
                ],
                "solution": "Copilot should scaffold a Vite + React project with <code>react-router-dom</code>, a shared <code>Layout</code> component, and route definitions for Home and About pages. Verify by running <code>npm run dev</code>.",
            },
            {
                "name": "Build UI Components",
                "challenge": "Ask Copilot to create a form component (e.g., a to-do input) and a list component that displays items. Style them with CSS modules or Tailwind.",
                "hints": [
                    "Describe the component in natural language: <em>Create a TodoForm with an input and submit button</em>.",
                    "Ask for a <em>TodoList component that receives items as props and renders them in a styled list</em>.",
                    "Request styling: <em>Add Tailwind classes for spacing and hover effects</em>.",
                ],
                "solution": "Create <code>TodoForm.jsx</code> and <code>TodoList.jsx</code> components. Wire them together on the Home page with React state. The form should add items to the list on submit.",
            },
            {
                "name": "Create the Node Backend",
                "challenge": "Scaffold an Express API with a <code>/api/todos</code> route that supports GET and POST. Store data in memory for now.",
                "hints": [
                    "Ask Copilot to create <code>server/index.js</code> with Express, CORS, and JSON body parsing.",
                    "Use an in-memory array for todos until you add a database later.",
                    "Test with <code>curl http://localhost:3001/api/todos</code>.",
                ],
                "solution": "Create an Express server with GET and POST routes for <code>/api/todos</code>, an in-memory array, and CORS enabled. Run it on port 3001 and verify both endpoints respond correctly.",
            },
            {
                "name": "Connect Frontend to Backend",
                "challenge": "Wire the React app to call the Express API — fetch todos on load and post new ones from the form. Handle loading and error states.",
                "hints": [
                    "Use <code>fetch</code> or <code>axios</code> in a <code>useEffect</code> hook to GET todos on mount.",
                    "Update the form's <code>onSubmit</code> to POST to the API and refresh the list.",
                    "Add a loading spinner and error message for failed requests.",
                ],
                "solution": "The Home page should fetch todos from <code>http://localhost:3001/api/todos</code> on mount, display them in TodoList, and submit new ones via TodoForm. Loading and error states should render appropriately.",
            },
            {
                "name": "QA and Deploy",
                "challenge": "Ask Copilot to write three unit tests for your API, fix any issues it finds, then create a Dockerfile or deployment config for the full stack.",
                "hints": [
                    "Ask: <em>Write Jest tests for the GET and POST /api/todos endpoints</em>.",
                    "Run the tests and let Copilot fix any failures.",
                    "Ask for a <code>Dockerfile</code> that builds the React app and serves it alongside the API.",
                ],
                "solution": "Create <code>server/__tests__/todos.test.js</code> with tests for GET (empty list), POST (add item), and GET (list with item). Fix any failures. Generate a multi-stage Dockerfile that builds the frontend and serves it with the backend.",
            },
        ],
    },
    {
        "path": "Developer/Intermediate/Enterprise-Grade-Marmalade",
        "title": "Central Prompt Repos - Enterprise Grade Marmalade",
        "tagline": "Explore how central prompt repositories preserve institutional knowledge, standardize AI-assisted development, and get every developer productive from day one",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub org with admin access (or a test org)",
            "VS Code with GitHub Copilot extensions",
            "Familiarity with .instructions.md and .prompt.md files",
        ],
        "tasks": [
            {
                "name": "Set Up a Central Prompt Repository",
                "challenge": "Create a new GitHub repository dedicated to storing organization-wide Copilot prompts, instructions, and skills. Structure it with clear folders and a README.",
                "hints": [
                    "Name it something like <code>copilot-prompts</code> or <code>.github-copilot</code>.",
                    "Create folders: <code>instructions/</code>, <code>skills/</code>, <code>agents/</code>.",
                    "Write a README explaining the repo's purpose and contribution guidelines.",
                ],
                "solution": "Create the repo with <code>instructions/</code>, <code>skills/</code>, and <code>agents/</code> folders. Add a <code>README.md</code> explaining how to add and consume prompts. Include a <code>CODEOWNERS</code> file so prompt changes get reviewed.",
            },
            {
                "name": "Write Org-Level Instructions",
                "challenge": "Author a <code>copilot-instructions.md</code> file that encodes your organization's coding standards, security policies, and preferred patterns.",
                "hints": [
                    "Include rules like: <em>Always validate user input at API boundaries</em>.",
                    "Add framework-specific guidance: <em>Use React hooks, not class components</em>.",
                    "Keep instructions concise — Copilot performs better with focused, clear rules.",
                ],
                "solution": "Create <code>instructions/copilot-instructions.md</code> covering coding style (naming, formatting), security rules (input validation, no secrets in code), framework patterns (React hooks, async/await), and testing requirements (minimum coverage expectations).",
            },
            {
                "name": "Create Reusable Skills",
                "challenge": "Build at least two <code>.prompt.md</code> skill files — one for code review and one for documentation generation — that any developer in the org can use.",
                "hints": [
                    "A skill file has YAML front matter with <code>description</code> and optionally <code>applyTo</code>.",
                    "The body is a prompt template that Copilot follows when the skill is invoked.",
                    "Test each skill by referencing it in Chat mode.",
                ],
                "solution": "Create <code>skills/code-review.prompt.md</code> (reviews code for security, performance, and style) and <code>skills/generate-docs.prompt.md</code> (generates JSDoc/TSDoc from function signatures). Test both in Copilot Chat.",
            },
            {
                "name": "Distribute and Consume",
                "challenge": "Configure a consuming repository to pull instructions and skills from the central prompt repo, so every developer automatically gets the latest standards.",
                "hints": [
                    "Use git submodules or a simple script that copies files on <code>npm postinstall</code>.",
                    "Alternatively, reference the central repo in your <code>.vscode/settings.json</code>.",
                    "Verify by cloning the consuming repo fresh and checking that Copilot follows the org instructions.",
                ],
                "solution": "Add the central repo as a git submodule at <code>.copilot/</code> in the consuming repo, or use a GitHub Action that syncs files on push. Verify a fresh clone picks up the instructions by asking Copilot a question and confirming it follows the org rules.",
            },
        ],
    },
    {
        "path": "Developer/Intermediate/GitHub-Coding-Agent-Its-Alive",
        "title": "Org Agent Config - Coding Agent: It's Alive!",
        "tagline": "Configure organization-level custom instructions for the GitHub Coding Agent, then establish smooth handoff processes between your IDE and automated agents",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub org with Copilot enabled",
            "A test repository with at least one open issue",
            "VS Code with GitHub Copilot extensions",
        ],
        "tasks": [
            {
                "name": "Configure Org-Level Agent Instructions",
                "challenge": "Create a <code>.github/copilot-coding-agent.md</code> file in your repository that tells the GitHub Coding Agent how to set up the dev environment and which patterns to follow.",
                "hints": [
                    "Include setup steps: <em>Run npm install, then npm run build</em>.",
                    "Specify coding patterns: <em>Use TypeScript, prefer functional components</em>.",
                    "Add testing requirements: <em>Write tests for new functions, run npm test before committing</em>.",
                ],
                "solution": "Create <code>.github/copilot-coding-agent.md</code> with sections for environment setup (install commands, env vars), coding standards (style, patterns), testing (how to run tests, coverage expectations), and commit conventions (conventional commits format).",
            },
            {
                "name": "Create a Coding Agent Task",
                "challenge": "Assign an issue to the Coding Agent (Copilot) and watch it open a pull request with a proposed implementation.",
                "hints": [
                    "Label the issue or assign it to <code>copilot</code> (depending on your org setup); or just click <em>Code with Copilot</em>.",
                    "The agent reads your instruction file, checks out a branch, and pushes code.",
                    "Watch the PR appear — it may take a few minutes.",
                ],
                "solution": "Assign the issue to the Coding Agent. It creates a branch, follows your <code>copilot-coding-agent.md</code> instructions, implements the change, and opens a PR. Review the PR to see if it followed your coding standards.",
            },
            {
                "name": "Review and Iterate",
                "challenge": "Review the agent's PR, leave specific feedback comments, and trigger the agent to make follow-up changes based on your review.",
                "hints": [
                    "Use inline comments: <em>This function should handle null input — add a guard clause</em>.",
                    "The agent will read your review and push additional commits.",
                    "Be specific — vague feedback leads to vague fixes.",
                ],
                "solution": "Leave 2-3 specific review comments on the PR. The Coding Agent reads them and pushes follow-up commits addressing each comment. Approve and merge once the code meets your standards.",
            },
            {
                "name": "IDE to Agent Handoff",
                "challenge": "Start working on a feature in VS Code, reach a point where you want the agent to continue, and hand off the work by creating an issue with your progress and context.",
                "hints": [
                    "Commit your work-in-progress to a branch.",
                    "Create an issue describing what's done and what remains.",
                    "Assign the issue to the Coding Agent with a reference to your branch.",
                ],
                "solution": "Push your WIP branch, create a detailed issue linking to it (<em>Branch feature/xyz has the scaffolding — implement the API routes per the spec in docs/api.md</em>), and assign it to the agent. The agent picks up where you left off.",
            },
        ],
    },
    {
        "path": "Developer/Intermediate/GitHub-Copilot-CLI",
        "title": "Terminal AI - Copilot CLI: The Who, the How, and the Why",
        "tagline": "Meet the new Copilot CLI, learn how it differs from chat, and combine both for maximum productivity right in your terminal",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub CLI (<code>gh</code>) installed and authenticated",
            "GitHub Copilot license active",
            "Terminal access (PowerShell, bash, or zsh)",
        ],
        "tasks": [
            {
                "name": "Install and Configure Copilot CLI",
                "challenge": "Install the GitHub Copilot CLI extension for <code>gh</code>, authenticate, and run your first AI-assisted command.",
                "hints": [
                    "Run <code>gh extension install github/gh-copilot</code>.",
                    "Verify with <code>gh copilot --help</code>.",
                    "Try <code>gh copilot suggest 'list all open PRs'</code> to confirm it works.",
                ],
                "solution": "Install the extension, run <code>gh copilot suggest 'list all open PRs assigned to me'</code>, and execute the suggested command. You should see your open PRs listed in the terminal.",
            },
            {
                "name": "Explain and Suggest Commands",
                "challenge": "Use <code>gh copilot explain</code> to understand a complex command you've encountered, then use <code>gh copilot suggest</code> to generate three different shell commands you'd normally have to look up.",
                "hints": [
                    "Try: <code>gh copilot explain 'find . -name \"*.log\" -mtime +30 -delete'</code>.",
                    "Suggest examples: <em>compress all PNG files in a folder</em>, <em>find the largest 10 files</em>, <em>kill process on port 3000</em>.",
                    "Note how explain breaks down each flag and pipe.",
                ],
                "solution": "Use <code>explain</code> on a complex find/grep/awk command and read its breakdown. Then use <code>suggest</code> for 3 tasks you'd normally Google. Execute each to verify correctness.",
            },
            {
                "name": "CLI vs Chat — When to Use Each",
                "challenge": "Complete the same task (e.g., create a new branch, make a change, commit, and open a PR) once using only Copilot CLI and once using only Copilot Chat in VS Code. Document the differences.",
                "hints": [
                    "CLI excels at shell-level tasks: git operations, file management, process management.",
                    "Chat excels at code-level tasks: writing functions, refactoring, explaining code.",
                    "The overlap is in automation — both can script, but from different angles.",
                ],
                "solution": "CLI is fastest for git workflows, system commands, and quick one-liners. Chat is best for multi-file code changes, explanations, and iterative development. Document when to reach for each.",
            },
            {
                "name": "Build a Workflow",
                "challenge": "Create a shell script that uses Copilot CLI to automate a development workflow: suggest a git command, explain it, execute it, and log the result.",
                "hints": [
                    "Use <code>gh copilot suggest</code> with the <code>-s shell</code> flag for shell-only suggestions.",
                    "Pipe the output or capture it in a variable.",
                    "Combine with standard shell commands for a complete workflow script.",
                ],
                "solution": "Create a script that: (1) suggests a git stash command, (2) explains what it does, (3) executes it, and (4) logs the result to a file. This demonstrates combining Copilot CLI with shell scripting for automated workflows.",
            },
        ],
    },
    # ─── Developer / Enterprise ──────────────────────────────────────
    {
        "path": "Developer/Enterprise/Agent-HQ-Reporting-for-Duty",
        "title": "Agent Coordination - Agent HQ: Reporting for Duty",
        "tagline": "Launch agents from GitHub, Slack, and VS Code, assign them tasks, share context across platforms, and keep humans and AI working side by side",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub org with Copilot and Coding Agent enabled",
            "Slack or Teams workspace with Copilot app installed",
            "VS Code with GitHub Copilot extensions",
        ],
        "tasks": [
            {
                "name": "Launch Agents from GitHub",
                "challenge": "Trigger Copilot agents from GitHub Issues and Pull Requests — create an issue, assign it to an agent, and observe the automated PR it produces.",
                "hints": [
                    "Use the <em>Code with Copilot</em> button on an issue, or assign to <code>copilot</code>.",
                    "Ensure your repo has a <code>.github/copilot-coding-agent.md</code> for best results.",
                    "Watch the Actions tab for the agent's workflow run.",
                ],
                "solution": "Create a well-described issue, assign it to the Coding Agent, and watch it create a branch, implement the change, and open a PR. Review the PR to verify it follows the repo's coding standards.",
            },
            {
                "name": "Agents in Slack and Teams",
                "challenge": "Use the Copilot app in Slack or Teams to ask about your repository — pull a PR summary, check deployment status, and create an issue, all from chat.",
                "hints": [
                    "In Slack: <code>@GitHub what are the open PRs in my-org/my-repo?</code>",
                    "Ask for a summary: <em>Summarize PR #42 in my-org/my-repo</em>.",
                    "Create an issue: <em>Create an issue in my-org/my-repo titled 'Update README'</em>.",
                ],
                "solution": "From your chat platform, query open PRs, get a PR summary, check recent deployments, and create an issue. Verify each action reflects on GitHub.",
            },
            {
                "name": "Agents in VS Code",
                "challenge": "Use Copilot agent mode in VS Code to coordinate a multi-file change — refactor a module by splitting it into smaller files with proper imports.",
                "hints": [
                    "Switch to agent mode in Copilot Chat (select the agent mode dropdown).",
                    "Ask: <em>Split utils.js into separate files for string, date, and array utilities</em>.",
                    "The agent will create files, move functions, update imports, and run tests.",
                ],
                "solution": "Agent mode splits the module, creates new files, rewrites import statements across the project, and optionally runs tests to verify nothing broke. Review the proposed changes before accepting.",
            },
            {
                "name": "Cross-Platform Context Sharing",
                "challenge": "Start a task in Slack (create an issue), continue it in VS Code (implement the fix), and finish in GitHub (merge the PR). Document how context flows between platforms.",
                "hints": [
                    "Context flows through GitHub's data model: issues, PRs, branches, and commits.",
                    "Each platform reads the same data — the agent in VS Code sees the issue created from Slack.",
                    "Link everything: issue → branch → PR → merge.",
                ],
                "solution": "Create the issue from Slack, open VS Code and reference that issue in your Copilot Chat prompt, implement the fix, push, and merge the PR on GitHub. Context is shared through Git and GitHub's API — Copilot on each platform reads the same source of truth.",
            },
        ],
    },
    {
        "path": "Developer/Enterprise/MCP-Maximizer",
        "title": "Advanced MCP - MCP Maximizer",
        "tagline": "Connect MCP to internal and external services with secure authentication, and build seamless integrations between your enterprise tools and AI workflows",
        "duration": "1 Hour",
        "prereqs": [
            "VS Code with GitHub Copilot extensions",
            "Basic MCP knowledge (see MCP for You and Me)",
            "Access to at least one internal API or database",
        ],
        "tasks": [
            {
                "name": "Connect Internal Services",
                "challenge": "Configure an MCP server that connects to an internal API (e.g., your company's REST API, a database, or an internal tool) with proper authentication.",
                "hints": [
                    "Create an MCP server entry in <code>.vscode/mcp.json</code> with your internal service URL.",
                    "Use environment variables for credentials — never hardcode tokens.",
                    "Test the connection by asking Copilot Chat to query data from the service.",
                ],
                "solution": "Add an MCP server configuration for your internal API with authenticated access via environment variables. Verify Copilot can query live data from the service in Chat.",
            },
            {
                "name": "Connect External Services",
                "challenge": "Integrate a third-party MCP server (e.g., a database connector, cloud provider, or SaaS tool) alongside the GitHub MCP server.",
                "hints": [
                    "Check <a href='https://github.com/modelcontextprotocol/servers'>MCP server directory</a> for available servers.",
                    "Add multiple servers in <code>mcp.json</code> — they can coexist.",
                    "Copilot will choose the right server based on the tools it needs.",
                ],
                "solution": "Add a second MCP server (e.g., a Postgres connector or cloud provider) to <code>mcp.json</code>. Ask Copilot a question that requires data from both servers and watch it call the right tools.",
            },
            {
                "name": "Secure Authentication",
                "challenge": "Set up OAuth or token-based authentication for an MCP server, store credentials securely, and verify that no secrets are exposed in your workspace files.",
                "hints": [
                    "Use <code>env</code> entries in <code>mcp.json</code> to reference environment variables.",
                    "Store secrets in your OS keychain or a <code>.env</code> file that's in <code>.gitignore</code>.",
                    "Audit your workspace: <code>grep -r 'token\\|secret\\|password' .vscode/</code> should find nothing.",
                ],
                "solution": "Configure MCP authentication using environment variables referenced in <code>mcp.json</code>. Store actual values in a <code>.env</code> file (git-ignored) or OS keychain. Confirm no secrets are committed by running a grep audit.",
            },
            {
                "name": "Build a Custom Integration",
                "challenge": "Wire an MCP server into a complete enterprise workflow: query data from an internal service, use it to make a code change, and verify the result — all through Copilot Chat.",
                "hints": [
                    "Example: query your ticketing system for a bug, pull the relevant code, fix it, and update the ticket.",
                    "Chain MCP calls by asking multi-step questions in Chat.",
                    "The more context you give in your prompt, the better the integration works.",
                ],
                "solution": "Ask Copilot a multi-step question that triggers MCP calls: <em>Look up ticket PROJ-123, find the related code, fix the bug described in the ticket, and mark it as resolved</em>. Verify each step executed correctly.",
            },
        ],
    },
    {
        "path": "Developer/Enterprise/Multi-Agent-Multi-Repo-Roundup",
        "title": "Cross-Repo Agents - Multi-Agent, Multi-Repo Roundup",
        "tagline": "Pull patterns and examples from one repository to shape another, and coordinate multiple agents in your IDE with zero extra infrastructure",
        "duration": "1 Hour",
        "prereqs": [
            "Access to at least two related GitHub repositories",
            "VS Code with GitHub Copilot and MCP configured",
            "GitHub MCP server connected",
        ],
        "tasks": [
            {
                "name": "Pull Patterns Across Repos",
                "challenge": "Use Copilot to reference code from Repository A while working in Repository B — pull a design pattern, utility function, or API contract from one repo to use in another.",
                "hints": [
                    "Use <code>#</code> references in Chat to point to files in another repo via MCP.",
                    "Ask: <em>Show me the auth middleware pattern from our shared-utils repo</em>.",
                    "Apply the pattern to your current repo with adaptations.",
                ],
                "solution": "Use MCP + Chat to fetch code from the reference repo, adapt it to the current repo's conventions, and implement it. Verify the pattern is consistent across both repositories.",
            },
            {
                "name": "Multi-Repo Context",
                "challenge": "Configure your VS Code workspace to give Copilot awareness of multiple repositories simultaneously using multi-root workspaces or MCP.",
                "hints": [
                    "Open a multi-root workspace with both repos: <em>File → Add Folder to Workspace</em>.",
                    "Alternatively, use MCP to give Copilot access to repos it can't see locally.",
                    "Ask cross-repo questions: <em>How does the API in repo-A consume the SDK from repo-B?</em>",
                ],
                "solution": "Set up a multi-root workspace or configure MCP for remote repo access. Ask Copilot questions that span both repos and verify it synthesizes information from both sources.",
            },
            {
                "name": "Coordinate Multiple Agents",
                "challenge": "Run agents targeting different repositories simultaneously — assign issues in two repos to the Coding Agent and observe how they work independently.",
                "hints": [
                    "Create related issues in both repos (e.g., 'Add endpoint' in the API repo, 'Add client call' in the frontend repo).",
                    "Assign both to the Coding Agent.",
                    "The agents work independently — they don't coordinate automatically, so your issue descriptions must be self-contained.",
                ],
                "solution": "Assign issues in both repos to the Coding Agent. Each creates its own branch and PR. Review both PRs and verify the changes are compatible. If they need to reference each other, include that context in the issue description.",
            },
            {
                "name": "Merge Cross-Repo Results",
                "challenge": "After the agents complete their PRs, integrate the results: merge both PRs, verify compatibility, and resolve any conflicts that arise from parallel agent work.",
                "hints": [
                    "Review both PRs for API compatibility — do the types and endpoints match?",
                    "Merge the API repo first, then update the frontend repo's PR if needed.",
                    "Use Copilot Chat to help resolve any integration issues.",
                ],
                "solution": "Merge the backend PR first (it defines the contract). Test the frontend PR against the updated backend. Use Copilot to fix any integration issues, then merge the frontend PR. Document the cross-repo coordination process for your team.",
            },
        ],
    },
    {
        "path": "Developer/Enterprise/SDK-Have-It-Your-Way",
        "title": "Copilot SDK - Have It Your Way",
        "tagline": "Use the Copilot SDK to build AI-powered applications outside the editor, design multi-step workflows, and ship with a production-tested agent runtime",
        "duration": "1 Hour",
        "prereqs": [
            "Node.js 18+ or Python 3.10+ installed",
            "GitHub Copilot license with API access",
            "Basic experience building CLI or web applications",
        ],
        "tasks": [
            {
                "name": "Set Up the Copilot SDK",
                "challenge": "Install the Copilot SDK, configure authentication, and make your first API call to verify everything works.",
                "hints": [
                    "Install via npm or pip depending on your language choice.",
                    "Configure your GitHub token for authentication.",
                    "Make a simple completion request to verify the connection.",
                ],
                "solution": "Install the SDK, set your GitHub token as an environment variable, and run a simple test script that sends a prompt and prints the response. Verify you get a meaningful completion back.",
            },
            {
                "name": "Build a Basic AI Application",
                "challenge": "Create a CLI tool or simple web app that uses the Copilot SDK to answer questions about a codebase — point it at a local directory and ask it questions.",
                "hints": [
                    "Read files from the target directory and include them as context in your prompts.",
                    "Build a REPL loop: read user question → send to SDK with file context → print response.",
                    "Handle the streaming response for a good user experience.",
                ],
                "solution": "Build a CLI that reads files from a specified directory, sends them as context with the user's question to the Copilot SDK, and streams the response. Test it against your own project.",
            },
            {
                "name": "Design Multi-Step Workflows",
                "challenge": "Extend your application to support multi-step workflows: analyze code → identify issues → propose fixes → apply changes — all orchestrated by your SDK code.",
                "hints": [
                    "Chain SDK calls: first call analyzes, second call proposes fixes, third call generates patches.",
                    "Pass the output of each step as input to the next.",
                    "Add user confirmation between steps for safety.",
                ],
                "solution": "Create a pipeline that: (1) sends code for analysis, (2) takes the analysis and asks for fix proposals, (3) takes a selected fix and generates a diff, (4) applies the diff with user confirmation. Each step uses the SDK and passes context forward.",
            },
            {
                "name": "Production Deployment",
                "challenge": "Add proper error handling, rate limiting, logging, and a health check endpoint to your application. Package it for deployment.",
                "hints": [
                    "Wrap SDK calls in try/catch with retry logic for transient failures.",
                    "Add structured logging for each SDK call (prompt length, response time, tokens used).",
                    "Create a Dockerfile or serverless config for deployment.",
                ],
                "solution": "Add error handling (retry with backoff), structured logging, a <code>/health</code> endpoint, and rate limiting. Package in a Dockerfile with multi-stage build. Document environment variables and deployment steps in a README.",
            },
        ],
    },
    # ─── Developer / Add-Ons ─────────────────────────────────────────
    {
        "path": "Developer/Add-Ons/Agent-Wars-Return-of-the-Chat-ai",
        "title": "Chat Platform Agents - Agent Wars: Return of the Chat-ai",
        "tagline": "Trigger builds, assign issues, and get summaries without leaving Teams or Slack, bridging chat platforms and development tools through agentic workflows",
        "duration": "30 Minutes",
        "prereqs": [
            "Slack or Microsoft Teams workspace",
            "GitHub Copilot app installed in your chat platform",
            "A GitHub repository with recent activity",
        ],
        "tasks": [
            {
                "name": "Set Up Copilot in Teams or Slack",
                "challenge": "Install and configure the GitHub Copilot app in your Slack workspace or Teams tenant. Verify it can access your GitHub organization.",
                "hints": [
                    "Search for <em>GitHub</em> in your platform's app directory.",
                    "Authorize the app to access your GitHub org.",
                    "Test with a simple query: <em>@GitHub what repos are in my-org?</em>",
                ],
                "solution": "Install the GitHub app, complete the OAuth authorization for your org, and test by asking it to list repositories. You should see a formatted response with your repo names.",
            },
            {
                "name": "Trigger Builds and Assign Issues",
                "challenge": "From your chat platform, trigger a GitHub Actions workflow and create/assign an issue — without opening a browser.",
                "hints": [
                    "Ask: <em>@GitHub run the CI workflow on main in my-org/my-repo</em>.",
                    "Create an issue: <em>@GitHub create an issue in my-org/my-repo titled 'Fix login bug' and assign it to @username</em>.",
                    "Check GitHub to verify both actions completed.",
                ],
                "solution": "Trigger a workflow run and create an assigned issue, both from chat. Verify on GitHub that the workflow is running and the issue exists with the correct assignee.",
            },
            {
                "name": "Get Summaries and Updates",
                "challenge": "Use the chat app to pull a PR summary, check deployment status, and get a digest of recent repository activity.",
                "hints": [
                    "Ask: <em>@GitHub summarize PR #15 in my-org/my-repo</em>.",
                    "Ask: <em>@GitHub what deployed to production this week?</em>",
                    "Ask: <em>@GitHub what happened in my-org/my-repo today?</em>",
                ],
                "solution": "Pull a PR summary, deployment status, and activity digest — all from chat. The app queries GitHub's API and returns formatted responses. Share these in team channels to keep everyone informed without context-switching.",
            },
        ],
    },
    {
        "path": "Developer/Add-Ons/Review-Me-Review-Me-Not-Review-Me",
        "title": "Automated Code Review - Review Me, Review Me Not, Review Me",
        "tagline": "Automate PR reviews, run code quality scans, and remediate vulnerabilities end-to-end so your team ships secure code faster",
        "duration": "30 Minutes",
        "prereqs": [
            "GitHub repository with branch protection enabled",
            "GitHub Advanced Security or Copilot code review enabled",
            "At least one open PR to test with",
        ],
        "tasks": [
            {
                "name": "Enable Copilot Code Review",
                "challenge": "Configure Copilot as an automatic code reviewer on your repository so it reviews every PR that's opened.",
                "hints": [
                    "Go to repo Settings → Code review → enable Copilot code review.",
                    "Alternatively, add a review request rule in branch protection.",
                    "Open a test PR to trigger the review.",
                ],
                "solution": "Enable Copilot code review in repository settings. Open a new PR and observe Copilot leave review comments with suggestions. The review covers code quality, potential bugs, and style issues.",
            },
            {
                "name": "Run Code Quality Scans",
                "challenge": "Set up code scanning (CodeQL or similar) on your repo, trigger a scan, and interpret the results that appear on a PR.",
                "hints": [
                    "Enable code scanning in Security → Code scanning alerts.",
                    "Add a CodeQL workflow via <em>Actions → New workflow → CodeQL Analysis</em>.",
                    "Push a PR with a known issue (e.g., SQL concatenation) to see it flagged.",
                ],
                "solution": "Enable CodeQL analysis, trigger it on a PR with an intentional vulnerability (e.g., string concatenation in a query). Review the alert, understand the severity and remediation guidance.",
            },
            {
                "name": "Remediate Vulnerabilities",
                "challenge": "Take a code scanning alert, ask Copilot to fix it, apply the fix, and verify the alert is resolved on the next scan.",
                "hints": [
                    "Click <em>Generate fix</em> on the alert, or ask Copilot Chat: <em>Fix the SQL injection in db.js line 15</em>.",
                    "Apply the suggested fix (parameterized query, input validation, etc.).",
                    "Push the fix and wait for the scan to re-run — the alert should close.",
                ],
                "solution": "Use Copilot's auto-fix suggestion to remediate the vulnerability, push the fix, and confirm the code scanning alert resolves. Document the before/after for your team's security review process.",
            },
        ],
    },
    # ─── Non-Developer / Beginner ────────────────────────────────────
    {
        "path": "Non-Developer/Beginner/Copilot-and-Azure-DevOps",
        "title": "Azure DevOps + Copilot - Made Better Together",
        "tagline": "Bridge Azure DevOps and GitHub Copilot so you can manage sprints, tasks, and boards from either platform without switching tools",
        "duration": "1 Hour",
        "prereqs": [
            "Azure DevOps account with a project",
            "GitHub account with Copilot access",
            "Browser access to both platforms",
        ],
        "tasks": [
            {
                "name": "Link Azure DevOps and GitHub",
                "challenge": "Connect your Azure DevOps project to a GitHub repository so work items and code changes are linked across platforms.",
                "hints": [
                    "In ADO, go to Project Settings → GitHub connections.",
                    "Authorize GitHub and select the repositories to link.",
                    "Verify by referencing an ADO work item ID in a GitHub commit message.",
                ],
                "solution": "Create a GitHub connection in your ADO project settings, authorize access, and link your repositories. Push a commit with <code>AB#1234</code> in the message and verify the work item shows the linked commit.",
            },
            {
                "name": "Manage Sprints from GitHub",
                "challenge": "Use Copilot in GitHub to plan sprint work — create issues that map to ADO work items and organize them in a GitHub Project board.",
                "hints": [
                    "Create GitHub Issues with references to ADO work items: <em>Implements AB#1234</em>.",
                    "Use GitHub Projects to create a sprint board with custom fields.",
                    "Ask Copilot to help organize and prioritize the backlog.",
                ],
                "solution": "Create a GitHub Project board with sprint columns, add issues linked to ADO work items, and use Copilot to prioritize and estimate. The two-way link keeps both platforms in sync.",
            },
            {
                "name": "Sync Tasks and Boards",
                "challenge": "Set up a workflow that keeps status synchronized between ADO boards and GitHub Projects — when a task moves in one, it updates in the other.",
                "hints": [
                    "Use GitHub Actions with the Azure DevOps API to sync status changes.",
                    "Alternatively, use a third-party connector like Azure DevOps Sync.",
                    "Test by moving a work item in ADO and verifying it updates in GitHub.",
                ],
                "solution": "Create a GitHub Action that triggers on project item status changes and updates the corresponding ADO work item via the API (or vice versa). Verify bidirectional sync works by moving items on both boards.",
            },
            {
                "name": "Cross-Platform Workflows",
                "challenge": "Build a workflow that triggers an ADO pipeline from GitHub, or a GitHub Action from ADO, demonstrating true cross-platform automation.",
                "hints": [
                    "Use webhooks or API calls from GitHub Actions to trigger ADO pipelines.",
                    "Set up an ADO service hook that calls a GitHub Actions workflow via <code>workflow_dispatch</code>.",
                    "Include meaningful data in the trigger payload (PR number, branch, etc.).",
                ],
                "solution": "Create a GitHub Action that triggers an ADO pipeline on PR merge, passing the branch and commit info. Verify the ADO pipeline runs with the correct parameters. Document the cross-platform automation flow.",
            },
        ],
    },
    {
        "path": "Non-Developer/Beginner/Copilot-and-the-Thing",
        "title": "Unified Tooling - Copilot and the Thing",
        "tagline": "Consolidate scattered repositories, trackers, and knowledge bases into one workflow with Copilot as your central assistant",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub account with access to multiple repositories",
            "Familiarity with GitHub Issues and Projects",
            "Access to your team's documentation or wiki",
        ],
        "tasks": [
            {
                "name": "Consolidate Your Repositories",
                "challenge": "Audit your team's scattered repositories and create a plan to organize them — identify which can be consolidated, archived, or linked together.",
                "hints": [
                    "List all repos your team owns — look for duplicates, forks, and abandoned projects.",
                    "Use Copilot to analyze repo descriptions and READMEs for overlap.",
                    "Create a consolidation plan: keep, merge, archive, or delete.",
                ],
                "solution": "Generate a repository inventory, identify consolidation opportunities, and create a migration plan. Archive abandoned repos, merge duplicates, and link related repos via topics and descriptions.",
            },
            {
                "name": "Unify Your Trackers",
                "challenge": "Link issues, tasks, and boards from scattered tools into a single GitHub Project that serves as the team's source of truth.",
                "hints": [
                    "Create a GitHub Project with views for each team or workstream.",
                    "Import or link existing issues from other trackers.",
                    "Set up custom fields to capture metadata from the other systems (priority, sprint, etc.).",
                ],
                "solution": "Create a unified GitHub Project, import key work items, configure custom fields and views, and establish it as the single source of truth. Retire or redirect the old trackers.",
            },
            {
                "name": "Centralize Knowledge",
                "challenge": "Use Copilot to surface and organize institutional knowledge — find docs scattered in wikis, READMEs, and Slack threads, and consolidate them.",
                "hints": [
                    "Ask Copilot about your codebase — it already knows your READMEs and docs.",
                    "Use Copilot Chat to summarize long documents and extract key decisions.",
                    "Create a central documentation structure in your main repo.",
                ],
                "solution": "Use Copilot to audit existing documentation, summarize key content, and create a consolidated docs structure (e.g., <code>docs/</code> folder with architecture, setup, and runbook pages). Link from the main README.",
            },
            {
                "name": "Copilot as Your Central Assistant",
                "challenge": "Build a daily workflow where Copilot ties everything together — morning status check, task management, documentation updates, and end-of-day summary.",
                "hints": [
                    "Morning: Ask Copilot for open issues, PR status, and blockers.",
                    "During day: Use Copilot to help write specs, review PRs, and update docs.",
                    "End of day: Ask Copilot to summarize what was accomplished and what's pending.",
                ],
                "solution": "Create a daily routine using Copilot: start with a status query, manage tasks through GitHub Projects, use Chat for documentation, and end with a summary. Copilot becomes the unified interface to all your tools.",
            },
        ],
    },
    {
        "path": "Non-Developer/Beginner/GitHub-One-for-All",
        "title": "GitHub Platform Tour - One for All",
        "tagline": "Tour GitHub Enterprise, Actions, Issues, Projects, Code Quality, and Secret Scanning to see how the platform works as one unified system",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub Enterprise account (or free account for most features)",
            "A test repository to experiment with",
            "Browser access to GitHub.com",
        ],
        "tasks": [
            {
                "name": "Explore GitHub Enterprise Features",
                "challenge": "Navigate your organization's GitHub Enterprise settings — explore teams, permission models, audit logs, and enterprise policies.",
                "hints": [
                    "Go to your org's Settings → Member privileges, Teams, and Audit log.",
                    "Explore how teams map to repository access levels.",
                    "Check enterprise policies for Copilot, Actions, and security features.",
                ],
                "solution": "Tour the org settings, understand the team → repo → permission model, review audit logs for recent activity, and check which enterprise policies are enabled. Note which features your org has configured.",
            },
            {
                "name": "Actions and Automation",
                "challenge": "Create a simple GitHub Actions workflow that runs on push — it should lint code or run a basic check. Understand runners, triggers, and job steps.",
                "hints": [
                    "Create <code>.github/workflows/ci.yml</code> with a <code>push</code> trigger.",
                    "Use <code>runs-on: ubuntu-latest</code> and add steps for checkout and a simple command.",
                    "Push a change and watch the workflow run in the Actions tab.",
                ],
                "solution": "Create a CI workflow with checkout, setup, and a lint/test step. Push, watch it run, and inspect the logs. Understand that Actions automate any workflow triggered by GitHub events.",
            },
            {
                "name": "Issues and Projects",
                "challenge": "Set up a Project board with custom views, create issues with labels and milestones, and use bulk actions to organize a sprint.",
                "hints": [
                    "Create a Project from the Projects tab, choose the Board or Table layout.",
                    "Add custom fields: Priority (single select), Sprint (iteration), Estimate (number).",
                    "Create 5+ issues and organize them on the board.",
                ],
                "solution": "Create a Project board with Board and Table views, add custom fields, create issues with labels and milestones, and organize them into a sprint. Use bulk actions to move items between columns.",
            },
            {
                "name": "Code Quality and Secret Scanning",
                "challenge": "Enable Dependabot, code scanning, and secret scanning on your repository. Review the alerts and understand what each tool catches.",
                "hints": [
                    "Go to Settings → Code security and analysis.",
                    "Enable Dependabot alerts, Dependabot security updates, code scanning, and secret scanning.",
                    "Check the Security tab for any alerts on your test repo.",
                ],
                "solution": "Enable all security features, review any existing alerts (dependency vulnerabilities, code issues, exposed secrets), and understand the remediation workflow for each type. These tools form a unified security posture.",
            },
        ],
    },
    # ─── Non-Developer / Intermediate ────────────────────────────────
    {
        "path": "Non-Developer/Intermediate/Executives-Command-and-Conquer",
        "title": "Executive AI Strategy - Command and Conquer",
        "tagline": "Answer the big questions &mdash; what's possible, where are we, what does it cost &mdash; with on-demand reports and real-time insights powered by Copilot",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub Enterprise with Copilot usage data",
            "Access to organizational dashboards and metrics",
            "Basic understanding of AI adoption goals",
        ],
        "tasks": [
            {
                "name": "Assess AI Readiness",
                "challenge": "Use available Copilot metrics and organizational data to assess your team's current AI adoption level — who's using it, how often, and where are the gaps?",
                "hints": [
                    "Check Copilot usage metrics in your GitHub org's settings.",
                    "Look at seat assignment vs. active usage percentages.",
                    "Identify teams with high adoption and teams that haven't started.",
                ],
                "solution": "Pull Copilot usage data from org settings, calculate adoption rates by team, and identify gaps. Create a heatmap of adoption across the organization showing who needs enablement support.",
            },
            {
                "name": "Generate On-Demand Reports",
                "challenge": "Create a report that answers the three big questions: What's possible with AI right now? Where are we in our adoption journey? What does it cost?",
                "hints": [
                    "Use Copilot to draft the 'what's possible' section based on current capabilities.",
                    "Pull usage data for the 'where are we' section.",
                    "Calculate cost-per-seat and productivity gains for the 'what does it cost' section.",
                ],
                "solution": "Create a three-section report: (1) AI capabilities and use cases relevant to your org, (2) current adoption metrics and trends, (3) cost analysis with ROI projections. Use Copilot to draft prose and analyze data.",
            },
            {
                "name": "Real-Time Insights Dashboard",
                "challenge": "Design a dashboard (even a simple document or spreadsheet) that gives executives real-time visibility into AI adoption, productivity impact, and cost.",
                "hints": [
                    "Include metrics: active users, suggestions accepted, time saved estimates.",
                    "Add trend lines: week-over-week adoption changes.",
                    "Include cost: seats used vs. allocated, cost per developer per month.",
                ],
                "solution": "Build a dashboard with three panels: Adoption (users, acceptance rate, trends), Productivity (estimated time saved, code suggestions accepted), and Cost (seat utilization, per-developer cost, projected ROI).",
            },
            {
                "name": "Present to Stakeholders",
                "challenge": "Use Copilot to create a leadership-ready executive summary — a one-page brief with key metrics, insights, and recommended next steps.",
                "hints": [
                    "Ask Copilot to summarize your report into an executive brief format.",
                    "Include 3-5 key metrics, 2-3 insights, and 2-3 recommendations.",
                    "Keep it to one page — executives scan, they don't deep-read.",
                ],
                "solution": "Generate a one-page executive summary with a headline metric, a brief narrative, key data points in a table, and three prioritized recommendations. Use Copilot to refine the language for a leadership audience.",
            },
        ],
    },
    {
        "path": "Non-Developer/Intermediate/Operations-Enterprise-Scale",
        "title": "Ops at Scale - Dragon Scales? You Need Enterprise Scale!",
        "tagline": "Collate logs, correlate dashboards, and propose fixes at scale, then generate reliability reports that back up your operational plans",
        "duration": "1.5 Hours",
        "prereqs": [
            "Access to operational logs or monitoring dashboards",
            "GitHub account with Copilot access",
            "Familiarity with operational KPIs and SLAs",
        ],
        "tasks": [
            {
                "name": "Collate Logs at Scale",
                "challenge": "Use AI to aggregate and filter logs from multiple services — identify the most common errors, warning patterns, and anomalies across your stack.",
                "hints": [
                    "Export or access logs from your monitoring tool (Datadog, Splunk, Azure Monitor, etc.).",
                    "Ask Copilot to analyze log samples for common error patterns.",
                    "Group errors by service, severity, and frequency.",
                ],
                "solution": "Aggregate logs from multiple sources, use Copilot to identify the top 10 error patterns, group them by service and severity, and create a prioritized list for investigation.",
            },
            {
                "name": "Correlate Dashboards",
                "challenge": "Connect metrics from different dashboards to identify correlations — when Service A's latency spikes, does Service B's error rate increase?",
                "hints": [
                    "Export key metrics from your dashboards (latency, error rate, throughput).",
                    "Ask Copilot to identify correlations in the data.",
                    "Create a unified view that shows correlated metrics side by side.",
                ],
                "solution": "Pull metrics from multiple dashboards, use Copilot to find correlations (e.g., latency spike in auth → error spike in checkout), and document the dependency chain for your team.",
            },
            {
                "name": "AI-Proposed Fixes",
                "challenge": "Present an operational issue to Copilot and ask it to propose remediation steps — then validate the proposal against your team's runbooks.",
                "hints": [
                    "Describe the issue with full context: service, symptoms, timeline, impact.",
                    "Ask Copilot: <em>Propose remediation steps for this production issue</em>.",
                    "Compare the AI's proposal with your existing runbook — note gaps in either.",
                ],
                "solution": "Give Copilot a detailed incident description, review its remediation proposal, and cross-reference with your runbooks. Update the runbook if the AI identified steps you were missing.",
            },
            {
                "name": "Generate Reliability Reports",
                "challenge": "Create a reliability report that covers uptime, incident response times, error budgets, and SLA compliance — using AI to draft the narrative sections.",
                "hints": [
                    "Gather data: uptime percentages, MTTR, incident counts, SLA targets.",
                    "Ask Copilot to draft the executive summary and trend analysis.",
                    "Include recommendations for the next quarter.",
                ],
                "solution": "Build a reliability report with data tables and AI-drafted narratives covering: uptime vs. SLA, incident trends, MTTR improvements, and recommended investments. Present it as evidence backing your operational plans.",
            },
            {
                "name": "Build an Enterprise Runbook",
                "challenge": "Create a Copilot-assisted runbook for a recurring operational task — document the steps, add decision trees, and include AI-generated troubleshooting tips.",
                "hints": [
                    "Pick a common task: deployment rollback, database failover, certificate rotation.",
                    "Document each step with clear conditions and actions.",
                    "Ask Copilot to add troubleshooting tips for each step based on common failure modes.",
                ],
                "solution": "Create a structured runbook with numbered steps, decision points, and Copilot-generated troubleshooting sections. Store it in your repo's <code>docs/runbooks/</code> folder and link it from your incident response process.",
            },
        ],
    },
    {
        "path": "Non-Developer/Intermediate/Project-Manager-Power-Up",
        "title": "PM Toolkit - Project Manager: Power Up",
        "tagline": "Know what to look for, ask the right questions, give developers clear direction, and generate leadership-ready reports in minutes",
        "duration": "1.5 Hours",
        "prereqs": [
            "GitHub account with access to team repositories",
            "Familiarity with GitHub Issues and Projects",
            "Understanding of your team's development workflow",
        ],
        "tasks": [
            {
                "name": "Know What to Look For",
                "challenge": "Use Copilot and GitHub's built-in tools to identify blockers, risks, and code health signals in your project — without needing to read the code yourself.",
                "hints": [
                    "Check open PRs: how long have they been waiting? Are there merge conflicts?",
                    "Review issue labels and milestones for overdue items.",
                    "Look at code scanning alerts for unresolved security findings.",
                ],
                "solution": "Create a project health checklist: PR aging, blocked issues, failing CI, security alerts, and stale branches. Use GitHub's built-in views and Copilot Chat to surface these signals quickly.",
            },
            {
                "name": "Ask the Right Questions",
                "challenge": "Formulate three questions about your project's status that a Project Manager should ask weekly, then use Copilot to answer them with real data.",
                "hints": [
                    "Examples: <em>What's our velocity this sprint?</em> <em>Which issues are at risk?</em> <em>Who's overloaded?</em>",
                    "Use Copilot Chat with MCP to query live project data.",
                    "Turn the answers into actionable insights, not just data points.",
                ],
                "solution": "Establish 3-5 weekly questions (velocity, risk, capacity, quality, blockers), use Copilot to pull data for each, and document the insights. Turn this into a weekly routine that keeps you informed without attending every standup.",
            },
            {
                "name": "Give Clear Direction",
                "challenge": "Take an AI insight (e.g., 'PR #42 has been open for 7 days with 3 unresolved comments') and translate it into an actionable developer spec or request.",
                "hints": [
                    "Be specific: instead of <em>fix the PR</em>, say <em>resolve the 3 comments on PR #42 by Thursday</em>.",
                    "Include context: why it matters (blocks release), what 'done' looks like.",
                    "Use Copilot to help draft the request in the right tone.",
                ],
                "solution": "Draft 3 actionable requests from AI insights — each with what, why, when, and done criteria. Use Copilot to refine the wording for clarity. Deliver them via GitHub issue comments or team messages.",
            },
            {
                "name": "Generate Leadership Reports",
                "challenge": "Create a stakeholder-ready project report in under 10 minutes using Copilot — cover status, risks, metrics, and next steps.",
                "hints": [
                    "Ask Copilot: <em>Generate a project status report for [project name] covering this sprint</em>.",
                    "Include: overall status (green/yellow/red), key achievements, risks, and asks.",
                    "Format it for scanning: bullet points, bold headers, one-page max.",
                ],
                "solution": "Generate a one-page status report with Copilot: RAG status, sprint achievements (3-5 bullets), risks (2-3 items), metrics (velocity, burndown), and next steps. The entire process should take under 10 minutes.",
            },
            {
                "name": "Build Your PM Toolkit",
                "challenge": "Create a reusable set of Copilot prompts and workflows that you'll use weekly — save them as prompt files or bookmarked queries for ongoing use.",
                "hints": [
                    "Create a <code>.prompt.md</code> file for each recurring task: status report, risk assessment, capacity check.",
                    "Save your best prompts in a document or prompt library.",
                    "Set up a weekly calendar reminder with links to each prompt.",
                ],
                "solution": "Create a PM toolkit with 5+ reusable prompts: weekly status, risk scan, sprint health, capacity check, and stakeholder summary. Store them in your repo's <code>docs/pm-toolkit/</code> folder and schedule weekly use.",
            },
        ],
    },
    # ─── Non-Developer / Enterprise ──────────────────────────────────
    {
        "path": "Non-Developer/Enterprise/Security-Proving-Trust-in-the-System",
        "title": "AI Governance - Proving Trust in the System",
        "tagline": "Analyze, limit, and govern AI traffic by using AI to prove itself &mdash; transparency, source tracking, and governance you can show stakeholders",
        "duration": "1 Hour",
        "prereqs": [
            "GitHub Enterprise with Copilot enabled",
            "Admin access to org-level Copilot settings",
            "Familiarity with compliance and governance concepts",
        ],
        "tasks": [
            {
                "name": "Analyze AI Traffic",
                "challenge": "Review your organization's Copilot usage data — understand what's being used, by whom, how often, and in what contexts.",
                "hints": [
                    "Go to org Settings → Copilot → Usage to see activity data.",
                    "Look at metrics like active users, suggestions accepted/rejected, and languages used.",
                    "Identify patterns: which teams use it most? Least? For what tasks?",
                ],
                "solution": "Pull usage data from org Copilot settings, break it down by team and usage pattern, and identify the top use cases. Document who's using AI, how often, and for what — this is the foundation of your governance report.",
            },
            {
                "name": "Set Limits and Policies",
                "challenge": "Configure content exclusions and usage policies — restrict Copilot from accessing sensitive files, repos, or patterns in your organization.",
                "hints": [
                    "Use org-level content exclusion rules to block sensitive paths (e.g., <code>**/secrets/**</code>).",
                    "Configure which repos have Copilot access and which don't.",
                    "Set policies for Chat context: what data can agents access?",
                ],
                "solution": "Configure content exclusions for sensitive paths and repos, set org-level policies for Copilot access, and document the policy decisions. Test by verifying Copilot doesn't suggest from excluded content.",
            },
            {
                "name": "Source Tracking and Transparency",
                "challenge": "Demonstrate to a stakeholder how Copilot's suggestions can be traced — show where suggestions come from and how content filtering works.",
                "hints": [
                    "Copilot's code referencing feature shows when suggestions match public code.",
                    "Content exclusions prevent training on or suggesting from specified files.",
                    "The audit log records Copilot-related events for compliance.",
                ],
                "solution": "Show the code referencing feature (matching public code alert), explain content exclusion enforcement, and pull audit log entries for Copilot events. This demonstrates transparency in how AI interacts with your code.",
            },
            {
                "name": "Build a Governance Report",
                "challenge": "Create a governance report that you can show stakeholders — covering usage, policies, transparency measures, and risk mitigations for AI in your organization.",
                "hints": [
                    "Structure: Executive summary, usage metrics, policies in place, transparency features, risk mitigations.",
                    "Use Copilot to draft the narrative sections.",
                    "Include specific examples: <em>Policy X prevents Y risk</em>.",
                ],
                "solution": "Create a stakeholder-ready governance report: usage overview, active policies (with examples), transparency mechanisms, risk assessment, and recommendations. This is your proof that AI is being used responsibly.",
            },
        ],
    },
    {
        "path": "Non-Developer/Enterprise/The-AI-is-Mightier-than-the-Sword",
        "title": "Multi-Agent Research - The AI is Mightier than the Sword",
        "tagline": "Assemble a fleet of specialized AI agents that research, debate, and surface the best answers to questions beyond any single person's scope",
        "duration": "1 Hour",
        "prereqs": [
            "VS Code with GitHub Copilot extensions",
            "Familiarity with Copilot Chat and agent modes",
            "A complex research question or problem to solve",
        ],
        "tasks": [
            {
                "name": "Design Specialized Agents",
                "challenge": "Create two or more agent definitions (<code>.agent.md</code> files) with distinct research roles — e.g., a 'Devil's Advocate' and a 'Solution Architect' — each with different instructions and perspectives.",
                "hints": [
                    "Define clear personas: what does each agent specialize in?",
                    "Give them different instructions: one challenges ideas, another proposes solutions.",
                    "Use YAML front matter to configure tools and context each agent can access.",
                ],
                "solution": "Create agent files like <code>devils-advocate.agent.md</code> (challenges assumptions, finds weaknesses) and <code>solution-architect.agent.md</code> (proposes designs, evaluates trade-offs). Each has distinct system instructions that shape its response style.",
            },
            {
                "name": "Enable Agent Debate",
                "challenge": "Present a complex question to your agents and have them 'debate' — run the same question through each agent and compare their responses. Identify where they disagree.",
                "hints": [
                    "Ask a question with no single right answer: <em>Should we migrate to microservices?</em>",
                    "Run it through the Devil's Advocate first, then the Solution Architect.",
                    "Document where they disagree and why — the disagreement is where the insight lives.",
                ],
                "solution": "Present the same question to both agents, collect their responses, and create a comparison table of arguments for and against. The divergence points reveal the most important considerations for your decision.",
            },
            {
                "name": "Provide Context at Scale",
                "challenge": "Feed a large body of knowledge (documentation, reports, data) into your agent conversations and see how it improves the quality and specificity of their responses.",
                "hints": [
                    "Use <code>#file</code> references to include relevant documents in your prompts.",
                    "Try with and without context — notice the difference in specificity.",
                    "For very large contexts, summarize first, then deep-dive on key sections.",
                ],
                "solution": "Include relevant documents via file references, compare contextual vs. non-contextual responses, and demonstrate how grounding agents in real data produces actionable (not generic) insights.",
            },
            {
                "name": "Surface the Best Answers",
                "challenge": "Aggregate the outputs from your multi-agent research into a final recommendation — use a third agent or your own judgment to synthesize the best answer.",
                "hints": [
                    "Create a 'synthesizer' agent that takes the outputs of the other agents as input.",
                    "Or manually review, weigh the arguments, and draft a recommendation.",
                    "Structure the final output: Context → Arguments → Recommendation → Next Steps.",
                ],
                "solution": "Synthesize the multi-agent outputs into a structured recommendation document: problem statement, key arguments from each perspective, synthesized recommendation with reasoning, and concrete next steps. This is the power of multi-agent research — better answers than any single perspective.",
            },
        ],
    },
]


def generate_html(course):
    """Generate the lab-format HTML for a single course."""
    title = course["title"]
    tagline = course["tagline"]
    duration = course["duration"]
    prereqs = course["prereqs"]
    tasks = course["tasks"]

    # Build prerequisites list items
    prereq_items = "\n".join(f"          <li>{p}</li>" for p in prereqs)

    # Build task sections
    task_sections = []
    for i, task in enumerate(tasks, 1):
        hint_items = "\n".join(f"              <li>{h}</li>" for h in task["hints"])
        section = f"""
    <!-- ============================================================
         TASK {i} — {task["name"]}
         ============================================================ -->
    <section class="slide slide--section">
      <div class="slide-inner">
        <span class="badge badge--blue">Task {i}</span>
        <h2>{task["name"]}</h2>
      </div>
    </section>

    <!-- Task {i}: Challenge + Hints -->
    <section class="slide slide--content">
      <div class="slide-inner">
        <h2>Challenge</h2>
        <p>{task["challenge"]}</p>
        <details>
          <summary><strong>Hints</strong> (expand when needed)</summary>
          <ul>
{hint_items}
          </ul>
        </details>
      </div>
    </section>

    <!-- Task {i}: Solution -->
    <section class="slide slide--content">
      <div class="slide-inner">
        <h2>Solution</h2>
        <p>{task["solution"]}</p>
      </div>
    </section>"""
        task_sections.append(section)

    tasks_html = "\n".join(task_sections)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} &mdash; MS Demoland</title>
  <link rel="stylesheet" href="/css/primer-brand.css" />
</head>
<body>

  <div class="slide-deck">

    <!-- ============================================================
         TITLE SLIDE
         ============================================================ -->
    <section class="slide slide--title">
      <div class="slide-inner">
        <img src="/img/ms-github-logo.svg" alt="Microsoft + GitHub" class="brand-logo" />
        <span class="badge">Hands-On &middot; {duration}</span>
        <h1>{title}</h1>
        <p class="subtitle">{tagline}</p>
      </div>
    </section>

    <!-- ============================================================
         PREREQUISITES
         ============================================================ -->
    <section class="slide slide--content">
      <div class="slide-inner">
        <h2>Prerequisites</h2>
        <ul>
{prereq_items}
        </ul>
      </div>
    </section>
{tasks_html}

    <!-- ============================================================
         LAB COMPLETE
         ============================================================ -->
    <section class="slide slide--section">
      <div class="slide-inner">
        <span class="badge badge--green">Lab Complete &mdash; Nice Work!</span>
        <h2>Wrap-Up &amp; Next Steps</h2>
      </div>
    </section>

    <!-- ============================================================
         CLOSING
         ============================================================ -->
    <section class="slide slide--title">
      <div class="slide-inner">
        <img src="/img/ms-github-logo.svg" alt="Microsoft + GitHub" class="brand-logo" />
        <h1>Well Done!</h1>
        <p class="subtitle">You've completed the lab. Share your results or open an issue if you hit a snag.</p>
      </div>
    </section>

  </div>

  <script type="module" src="/js/slides.js"></script>
</body>
</html>
"""
    return html


def main():
    success = 0
    errors = []
    for course in COURSES:
        filepath = os.path.join(BASE, course["path"], "index.html")
        try:
            html = generate_html(course)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            success += 1
            print(f"  OK  {course['path']}")
        except Exception as e:
            errors.append((course["path"], str(e)))
            print(f"  FAIL {course['path']}: {e}")

    print(f"\n{'='*50}")
    print(f"Written: {success}/{len(COURSES)}")
    if errors:
        print("Errors:")
        for path, err in errors:
            print(f"  {path}: {err}")


if __name__ == "__main__":
    main()
