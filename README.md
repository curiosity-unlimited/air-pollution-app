# Air Pollution App
- An educational application that allows users to retrieve and display air pollution data for locations around the world.

## Features
- Two demo branches are available: `demo/agent-mode` and `demo/plan-agent-mode`.
    - If you're working with Agent mode, you can compare your progress with `demo/agent-mode` branch.
    - If you're working with Plan/Agent mode, you can compare your progress with `demo/plan-agent-mode` branch.

## Getting Started
1. Fork the Repository on GitHub
    1. Go to the repository: https://github.com/curiosity-unlimited/air-pollution-app.git
    2. Click the "Fork" button in the top-right corner
    3. **IMPORTANT: Please uncheck the "Copy the DEFAULT branch only" option when forking in order to copy all branches into the new fork.**
    4. GitHub will create a copy under your account: https://github.com/YOUR-USERNAME/air-pollution-app

2. Clone the repository from YOUR fork (not the original):
    ```bash
    # Replace YOUR-USERNAME with your GitHub Account
    git clone https://github.com/YOUR-USERNAME/air-pollution-app
    cd air-pollution-app
    ```

3. Fetch all branches and tags so that you can see both the initial code and the instructor's implementation:
    ```bash
    git fetch origin --tags
    ```

4. Check all branches and make sure all `demo` branches are in the list:
    ```bash
    git branch -a
    ```

5. Make sure you're on the `main` branch:
    ```bash
    git checkout main
    ```

6. Create a new branch, `develop/agent-mode` and `develop/plan-agent-mode`, for example, for your own work:
    ```bash
    git checkout -b develop/agent-mode
    git checkout -b develop/plan-agent-mode
    ```

7. To compare your progress with the instructor's:
    ```bash
    # List all milesones
    git tag -n
    # Compare with a specific milestone
    git diff your-branch-name..tag-name
    # See all differences between your work and the reference
    git diff your-branch-name..demo/agent-mode
    git diff your-branch-name..demo/plan-agent-mode
    ```

8. For a more comprehensive guide, please follow instructions in [`CONTRIBUTING.md`](./CONTRIBUTING.md)

## License

[MIT](LICENSE)