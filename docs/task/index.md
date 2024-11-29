# Task runner

## Make[file]

!!! note "Makefile"

    [Makefile](https://www.gnu.org/software/make/manual/make.html)
    is a tool which controls the generation of executables
    and other non-source files of a program from the program's source files.

We can use it to run some commands concisely:
```makefile
run_doc_server:
	mkdocs serve

run_local_gunicorn:
	gunicorn package.app.main:app --worker-class uvicorn.workers.UvicornWorker
```



## Task[file]

!!! note "Taskfile"

    [Task](https://taskfile.dev/) is a task runner / build tool that aims to be simpler and easier to use than, for example,
    [GNU Make](https://www.gnu.org/software/make/).

```yaml
version: '3'

tasks:
  run:
    cmds:
      - streamlit run home.py
  build:
    cmds:
      - bash docker_build.sh
```


## Poetry `scripts`

!!! note "Poetry `scripts`"

    The [`scripts` section](https://python-poetry.org/docs/pyproject/#scripts)
    of the `pyproject.toml` file allows you to define commands that can be executed with `poetry run`.


```toml
[tool.poetry.scripts]
my_package_cli = 'my_package.console:run'
```

## Duty

!!! note "Duty"

    [pawamoy/duty](https://pawamoy.github.io/duty/) is a simple task runner.
    Which is inspired by [Invoke](https://github.com/pyinvoke/invoke).


![](https://pawamoy.github.io/duty/demo.svg)

## Typer

!!! note "Typer"

    [tiangolo/typer](https://typer.tiangolo.com/) is a library for building CLI applications
    that users will love using and developers will love creating. Based on Python 3.6+ type hints.

```bash
$ python main.py --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────╮
│ --install-completion          Install completion  │
│                               for the current     │
│                               shell.              │
│ --show-completion             Show completion for │
│                               the current shell,  │
│                               to copy it or       │
│                               customize the       │
│                               installation.       │
│ --help                        Show this message   │
│                               and exit.           │
╰───────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────╮
│ goodbye                                           │
│ hello                                             │
╰───────────────────────────────────────────────────╯

// When you create a package you get ✨ auto-completion ✨ for free, installed with --install-completion

// You have 2 subcommands (the 2 functions): goodbye and hello
```

## Just

!!! note "Just"

    [casey/just](https://github.com/casey/just) is a handy way to save and run project-specific commands.


![](https://raw.githubusercontent.com/casey/just/master/screenshot.png)
