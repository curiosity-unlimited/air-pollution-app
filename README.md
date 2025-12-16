# Air Pollution App
- An educational application that allows users to retrieve and display air pollution data for locations around the world using OpenWeather's APIs.

## Features
- Two demo branches are available: `demo-edit-mode` and `demo-agent-mode`.
    - If you're working with Edit mode, you can compare your progress with `demo-edit-mode` branch.
    - If you're working with Agent mode, you can compare your progress with `demo-agent-mode` branch.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/curiosity-unlimited/air-pollution-app.git
   cd air-pollution-app
   ```

2. Fetch all the branches:
    ```
    git fetch --all
    ```

3. Check all the branches and make sure `demo-edit-mode` and `demo-agent-mode` are in the list:
    ```
    git branch -a
    ```

4. Create a new branch, `edit-mode` for example, if you're working on Edit mode:
    ```
    git checkout -b edit-mode
    ```

5. Create a new branch, `agent-mode` for example, if you're working on Agent mode:
    ```
    git checkout -b agent-mode
    ```

6. To compare your progress, you can first switch to `demo-edit-mode` or `demo-agent-mode` branch and checkout specific commit or step if necessary. Take Edit mode for example:
    ```
    git checkout demo-edit-mode
    git checkout <commit-hash>
    ```

## License

[MIT](LICENSE)