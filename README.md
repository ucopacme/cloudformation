# [Programmatic creation of Cloudformation using sceptre](https://sceptre.cloudreach.com/latest/docs/index.html)


* for cloud9 deactiviate python alias in ~/.bashrc

  ```
  # User specific aliases and functions
  # alias python=python27
  ```

  ```
  unalias python
  ```

* use python virtual env, eg:

  ```
  virtualenv -p `which python3` ~/python/venv/sceptre
  ```

* get into python virtual environment

  ```
  source ~/python/venv/sceptre/bin/activate
  ```

* pre-reqs to install pip modules

  ```
  pip install -r requirements.txt
  ```

# Fun with sceptre

* You need to be in the sceptre directory 

  ```
  cd sceptre
  ```
* this validates and generates a template

  ```
  sceptre --var "team=my-team" --var "prj=my-app" --var "app=my-app" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml validate-template  test logging-bucket
  sceptre --var "team=my-team" --var "prj=my-app" --var "app=my-app" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml generate-template  test logging-bucket
  ```

* this launches/updates a stack based on the generated template
  ```
  sceptre --var "team=my-team" --var "prj=my-app" --var "app=my-app" --var "region=us-west-2"   --var "iam_role="  --var-file config/variables.yaml launch-stack  test logging-bucket
  ```

* get out of python virtual environment

  ```
  deactivate
  ```

