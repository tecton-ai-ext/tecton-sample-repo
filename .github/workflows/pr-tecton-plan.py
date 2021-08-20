name: Tecton Feature Repo CI/CD

on:
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      TECTON_API_KEY: ${{ secrets.TECTON_API_KEY }}
      API_SERVICE: https://app.tecton.ai/api
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Set up Python 3.7.10
      uses: actions/setup-python@v2
      with:
        python-version: 3.7.10

    - name: Install pypandoc for databricks-connect
      run: pip install pypandoc

    - name: Install the Tecton CLI
      run: pip install --no-cache-dir 'tecton[pyspark]'

    - name: Run tecton plan
      run: tecton plan --no-safety-check
      working-directory: feature_repo

    - name: extra
      run: echo "YAY"
